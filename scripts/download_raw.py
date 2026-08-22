"""下载 Airoha JIRA 服务台工单的原始 HTML 到 raw/ 目录。

用法:
    python scripts/download_raw.py 15 100 200 ...     # 下载指定工单号
    python scripts/download_raw.py --range 15 760     # 下载范围（后续全量用）

前置条件:
    cookies.txt 必须存在于项目根目录（Netscape 格式，浏览器导出）
"""
import argparse
import os
import random
import re
import sys
import time
from pathlib import Path

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 目标网站 SSL 证书链不完整（实测 "unable to get local issuer certificate"）
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

BASE_URL = "https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-{id}"
ROOT = Path(__file__).resolve().parent.parent
COOKIE_FILE = ROOT / "cookies.txt"
RAW_DIR = ROOT / "raw"
LOGIN_TITLE_PATTERN = re.compile(r"Log into", re.IGNORECASE)


def load_cookies(path: Path) -> dict:
    """解析 Cookie 文件，返回 {name: value}。

    支持两种格式：
      1. Netscape 格式（Cookie-Editor 导出的 cookies.txt，Tab 分隔）
      2. HTTP Cookie 头格式（浏览器 DevTools 复制的 "name=value; name=value"）
    """
    cookies = {}
    if not path.exists():
        print(f"[错误] 未找到 {path}，请先导出浏览器 Cookie 并保存为 cookies.txt")
        sys.exit(1)
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "\t" in line:  # Netscape 格式
            parts = line.split("\t")
            if len(parts) >= 7:
                cookies[parts[5]] = parts[6]
        elif "=" in line:  # HTTP Cookie 头格式
            for item in line.split(";"):
                item = item.strip()
                if "=" in item:
                    name, _, value = item.partition("=")
                    name, value = name.strip(), value.strip()
                    if name:
                        cookies[name] = value
    if not cookies:
        print("[错误] cookies.txt 中没有解析到任何 Cookie，请检查格式")
        sys.exit(1)
    print(f"[信息] 已加载 {len(cookies)} 个 Cookie")
    return cookies


def fetch_one(session: requests.Session, ticket_id: int, max_retries: int = 3) -> str:
    """下载单个工单页面，返回 HTML 文本；失败抛出异常。"""
    url = BASE_URL.format(id=ticket_id)
    for attempt in range(1, max_retries + 1):
        try:
            resp = session.get(url, timeout=30, verify=False)
            resp.raise_for_status()
            text = resp.text
            # 登录失效检测：Jira 登录页标题为 "Log into Atlassian ..."
            match = re.search(r"<title>(.*?)</title>", text, re.DOTALL | re.IGNORECASE)
            if match and LOGIN_TITLE_PATTERN.search(match.group(1)):
                raise PermissionError("会话已失效（页面跳转到登录页），请更新 cookies.txt")
            return text
        except PermissionError:
            raise
        except Exception as e:
            if attempt == max_retries:
                raise
            wait = 2 ** attempt + random.uniform(0, 1)
            print(f"  [重试 {attempt}] 工单 {ticket_id}: {e}，{wait:.1f}s 后重试")
            time.sleep(wait)


def main():
    parser = argparse.ArgumentParser(description="下载 Airoha JIRA 工单原始 HTML")
    parser.add_argument("ids", nargs="*", type=int, help="工单号列表（不带 MIUIX1565- 前缀）；与 --range 二选一，--range 优先")
    parser.add_argument("--range", nargs=2, type=int, metavar=("START", "END"), help="下载范围内的所有工单")
    parser.add_argument("--delay", type=float, default=1.5, help="请求间隔秒数（默认 1.5）")
    args = parser.parse_args()

    if args.range:
        start, end = args.range
        ids = list(range(start, end + 1))
    else:
        ids = args.ids

    cookies = load_cookies(COOKIE_FILE)
    session = requests.Session()
    session.cookies.update(cookies)
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    })

    RAW_DIR.mkdir(exist_ok=True)
    ok = fail = 0
    for i, ticket_id in enumerate(ids, 1):
        out = RAW_DIR / f"MIUIX1565-{ticket_id}.html"
        if out.exists():
            print(f"[跳过] {i}/{len(ids)} MIUIX1565-{ticket_id}（已存在）")
            continue
        try:
            html = fetch_one(session, ticket_id)
            out.write_text(html, encoding="utf-8")
            print(f"[成功] {i}/{len(ids)} MIUIX1565-{ticket_id} ({len(html)//1024} KB)")
            ok += 1
        except PermissionError as e:
            print(f"[停止] {e}")
            sys.exit(2)
        except Exception as e:
            print(f"[失败] MIUIX1565-{ticket_id}: {e}")
            fail += 1
        time.sleep(args.delay + random.uniform(0, 1))  # 礼貌抓取：随机延迟

    print(f"\n完成：成功 {ok}，失败 {fail}。原始 HTML 已保存到 raw/ 目录")
    if fail:
        print("失败工单后续可用同一命令重试（已下载的会自动跳过）")


if __name__ == "__main__":
    main()
