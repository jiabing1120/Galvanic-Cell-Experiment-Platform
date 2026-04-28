#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
原电池虚拟交互实验室 - Python 桌面版
双击运行或命令行: python seawater_lab.py
自动打开浏览器，无需安装任何第三方库。
"""

import http.server
import webbrowser
import threading
import os
import sys
import socket

# ========== 配置 ==========
PORT = 8080
HTML_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seawater-battery-lab-v8.html")


def find_free_port(start=8080):
    """找一个空闲端口"""
    port = start
    while port < 9000:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
        port += 1
    return start


def main():
    if not os.path.exists(HTML_FILE):
        print(f"[错误] 找不到文件: {HTML_FILE}")
        print("请确保 seawater-battery-lab-v8.html 与本脚本在同一目录下。")
        input("按 Enter 键退出...")
        sys.exit(1)

    port = find_free_port(PORT)

    # 切换到 HTML 文件所在目录
    os.chdir(os.path.dirname(os.path.abspath(HTML_FILE)))

    # 创建 HTTP 服务器
    handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer(("127.0.0.1", port), handler)

    print("=" * 50)
    print("   🔋 原电池虚拟交互实验室")
    print("   Python 桌面版 v1.0")
    print("=" * 50)
    print(f"\n   服务地址: http://127.0.0.1:{port}")
    print(f"   按 Ctrl+C 或关闭此窗口退出\n")

    # 在后台启动服务器
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    # 自动打开浏览器
    webbrowser.open(f"http://127.0.0.1:{port}/seawater-battery-lab-v8.html")

    # 等待用户退出
    try:
        input("   按 Enter 键退出...\n")
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        httpd.shutdown()
        print("   已退出。")


if __name__ == "__main__":
    main()
