import requests
import time
headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': '',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'baggage': 'sentry-environment=production,sentry-release=88da3a24bf1546fd9824631c12ead4b5,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=3b325a8709c75374cd5531ff533bd72f,sentry-sample_rand=0.9756898109671025',
    'sentry-trace': '3b325a8709c75374cd5531ff533bd72f-a0318167eadd4c1a',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'content-type': 'application/json',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import modal\nimport time\nimport subprocess, tempfile, os\n\n# ---- Khởi tạo app ----\napp = modal.App("nodejs-workers")\n\n# ---- Build image ----\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .pip_install("cupy-cuda12x")\n    .apt_install("git", "curl", "gnupg")\n    .run_commands(\n        "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n        "apt-get install -y nodejs"\n    )\n)\n\n# ---- Worker ----\n@app.function(image=image, timeout=3600, concurrency_limit=10)\ndef run_tool(cookies: str):\n    # Clone repo nếu chưa có\n    if not os.path.exists("ha1"):\n        subprocess.run(\n            ["git", "clone", "https://github.com/vudeptrai79006-jpg/tool.git"],\n            check=True\n        )\n\n    # Ghi cookies ra file tạm\n    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:\n        f.write(cookies)\n        cookie_path = f.name\n\n    # Chạy Node.js tool trong thư mục repo\n    process = subprocess.Popen(\n        ["node", "app.js", "--cookies", cookie_path],\n        cwd="ha1"\n    )\n    process.wait()\n\n# ---- Entry point ----\n@app.local_entrypoint()\ndef main():\n    cookies_list = [\n        \'{"session":"se-111"}\',\n        \'{"session":"se-222"}\',\n        \'{"session":"se-333"}\',\n    ]\n\n    i = 0\n    while True:\n        cookies = cookies_list[i % len(cookies_list)]\n        print(f"🚀 Spawn worker {i} với cookies: {cookies}")\n        run_tool.spawn(cookies)\n        i += 1\n        time.sleep(5)  # giãn cách spawn',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 16,
        'cols': 93,
    },
}

response = requests.post('https://modal.com/api/playground/vudeptrai79006/run', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import modal\\nimport time\\nimport subprocess, tempfile, os\\n\\n# ---- Khởi tạo app ----\\napp = modal.App(\\"nodejs-workers\\")\\n\\n# ---- Build image ----\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .pip_install(\\"cupy-cuda12x\\")\\n    .apt_install(\\"git\\", \\"curl\\", \\"gnupg\\")\\n    .run_commands(\\n        \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n        \\"apt-get install -y nodejs\\"\\n    )\\n)\\n\\n# ---- Worker ----\\n@app.function(image=image, timeout=3600, concurrency_limit=10)\\ndef run_tool(cookies: str):\\n    # Clone repo nếu chưa có\\n    if not os.path.exists(\\"ha1\\"):\\n        subprocess.run(\\n            [\\"git\\", \\"clone\\", \\"https://github.com/vudeptrai79006-jpg/tool.git\\"],\\n            check=True\\n        )\\n\\n    # Ghi cookies ra file tạm\\n    with tempfile.NamedTemporaryFile(\\"w\\", delete=False, suffix=\\".json\\") as f:\\n        f.write(cookies)\\n        cookie_path = f.name\\n\\n    # Chạy Node.js tool trong thư mục repo\\n    process = subprocess.Popen(\\n        [\\"node\\", \\"app.js\\", \\"--cookies\\", cookie_path],\\n        cwd=\\"ha1\\"\\n    )\\n    process.wait()\\n\\n# ---- Entry point ----\\n@app.local_entrypoint()\\ndef main():\\n    cookies_list = [\\n        \'{\\"session\\":\\"se-111\\"}\',\\n        \'{\\"session\\":\\"se-222\\"}\',\\n        \'{\\"session\\":\\"se-333\\"}\',\\n    ]\\n\\n    i = 0\\n    while True:\\n        cookies = cookies_list[i % len(cookies_list)]\\n        print(f\\"🚀 Spawn worker {i} với cookies: {cookies}\\")\\n        run_tool.spawn(cookies)\\n        i += 1\\n        time.sleep(5)  # giãn cách spawn","modalEnvironment":"main","winsize":{"rows":16,"cols":93}}'.encode()
#response = requests.post('https://modal.com/api/playground/vudeptrai79006/run', headers=headers, data=data)


def main():
    while True:
        try:
            resp = requests.post(url, cookies=cookies, headers=headers, json=json_data, timeout=20)
            print(f"📡 Status: {resp.status_code}")
            if resp.ok:
                print(resp.text[:200])  # in ra 200 ký tự đầu của response
        except Exception as e:
            print(f"❌ Lỗi: {e}")

        time.sleep(5)  # đợi 5s rồi gửi lại


if __name__ == "__main__":
    main()
