import requests
import time
cookies = {
    'INGRESSCOOKIE': '1756141966.845.344.364170|9de6a539c14bab7f9073ed2b75abad44',
    'ajs_anonymous_id': '56cedb4a-72be-4e66-b8e6-58ca3880e304',
    'modal-session': 'se-qhecgHy5DrlVD9DIRhYuwj:xx-aw51KOQMZXfO1VDdUR1iOu',
    'ajs_user_id': 'us-bSR2mwgiQjKIe4oeimWpp1',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%22us-bSR2mwgiQjKIe4oeimWpp1%22%2C%22%24sesid%22%3A%5B1756143901365%2C%220198e237-e282-7101-b652-08924292e3bf%22%2C1756141970048%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fplayground%22%7D%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=88da3a24bf1546fd9824631c12ead4b5,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=9b8e1ccf32857e01beae882f8ad2300d,sentry-sample_rand=0.4835639969331188',
    'content-type': 'application/json',
    'origin': 'https://modal.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '9b8e1ccf32857e01beae882f8ad2300d-9aee49b55f625b1d',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'INGRESSCOOKIE=1756141966.845.344.364170|9de6a539c14bab7f9073ed2b75abad44; ajs_anonymous_id=56cedb4a-72be-4e66-b8e6-58ca3880e304; modal-session=se-qhecgHy5DrlVD9DIRhYuwj:xx-aw51KOQMZXfO1VDdUR1iOu; ajs_user_id=us-bSR2mwgiQjKIe4oeimWpp1; ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog=%7B%22distinct_id%22%3A%22us-bSR2mwgiQjKIe4oeimWpp1%22%2C%22%24sesid%22%3A%5B1756143901365%2C%220198e237-e282-7101-b652-08924292e3bf%22%2C1756141970048%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fplayground%22%7D%7D',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import modal\nimport time\nimport subprocess, tempfile, os\n\n# ---- Khởi tạo app ----\napp = modal.App("nodejs-workers")\n\n# ---- Build image ----\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .pip_install("cupy-cuda12x")\n    .apt_install("git", "curl", "gnupg", "ca-certificates")\n    .run_commands(\n        "update-ca-certificates",\n        "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n        "apt-get install -y nodejs"\n    )\n)\n\n# ---- Worker ----\n@app.function(image=image, timeout=3600, concurrency_limit=10)\ndef run_tool(cookies: str):\n    repo_dir = "ha1"\n\n    # Clone repo nếu chưa có (clone thẳng vào \'ha1\' để khớp với cwd)\n    if not os.path.exists(repo_dir):\n        subprocess.run(\n            ["git", "clone", "https://github.com/vudeptrai79006-jpg/tool.git", repo_dir],\n            check=True\n        )\n\n    # Ghi cookies ra file tạm\n    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:\n        f.write(cookies)\n        cookie_path = f.name\n\n    try:\n        # Chạy Node.js tool trong thư mục repo\n        process = subprocess.Popen(\n            ["node", "app.js", "--cookies", cookie_path],\n            cwd=repo_dir\n        )\n        process.wait()\n        if process.returncode != 0:\n            raise RuntimeError(f"Node.js exited with code {process.returncode}")\n    finally:\n        # Dọn file tạm\n        if os.path.exists(cookie_path):\n            os.remove(cookie_path)\n\n# ---- Entry point ----\n@app.local_entrypoint()\ndef main():\n    cookies_list = [\n        \'{"session":"se-111"}\',\n        \'{"session":"se-222"}\',\n        \'{"session":"se-333"}\',\n    ]\n\n    i = 0\n    while True:\n        cookies = cookies_list[i % len(cookies_list)]\n        print(f"🚀 Spawn worker {i} với cookies: {cookies}")\n        run_tool.spawn(cookies)\n        i += 1\n        time.sleep(5)  # giãn cách spawn',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 16,
        'cols': 93,
    },
}

response = requests.post('https://modal.com/api/playground/vudeptrai79006/run', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import modal\\nimport time\\nimport subprocess, tempfile, os\\n\\n# ---- Khởi tạo app ----\\napp = modal.App(\\"nodejs-workers\\")\\n\\n# ---- Build image ----\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .pip_install(\\"cupy-cuda12x\\")\\n    .apt_install(\\"git\\", \\"curl\\", \\"gnupg\\", \\"ca-certificates\\")\\n    .run_commands(\\n        \\"update-ca-certificates\\",\\n        \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n        \\"apt-get install -y nodejs\\"\\n    )\\n)\\n\\n# ---- Worker ----\\n@app.function(image=image, timeout=3600, concurrency_limit=10)\\ndef run_tool(cookies: str):\\n    repo_dir = \\"ha1\\"\\n\\n    # Clone repo nếu chưa có (clone thẳng vào \'ha1\' để khớp với cwd)\\n    if not os.path.exists(repo_dir):\\n        subprocess.run(\\n            [\\"git\\", \\"clone\\", \\"https://github.com/vudeptrai79006-jpg/tool.git\\", repo_dir],\\n            check=True\\n        )\\n\\n    # Ghi cookies ra file tạm\\n    with tempfile.NamedTemporaryFile(\\"w\\", delete=False, suffix=\\".json\\") as f:\\n        f.write(cookies)\\n        cookie_path = f.name\\n\\n    try:\\n        # Chạy Node.js tool trong thư mục repo\\n        process = subprocess.Popen(\\n            [\\"node\\", \\"app.js\\", \\"--cookies\\", cookie_path],\\n            cwd=repo_dir\\n        )\\n        process.wait()\\n        if process.returncode != 0:\\n            raise RuntimeError(f\\"Node.js exited with code {process.returncode}\\")\\n    finally:\\n        # Dọn file tạm\\n        if os.path.exists(cookie_path):\\n            os.remove(cookie_path)\\n\\n# ---- Entry point ----\\n@app.local_entrypoint()\\ndef main():\\n    cookies_list = [\\n        \'{\\"session\\":\\"se-111\\"}\',\\n        \'{\\"session\\":\\"se-222\\"}\',\\n        \'{\\"session\\":\\"se-333\\"}\',\\n    ]\\n\\n    i = 0\\n    while True:\\n        cookies = cookies_list[i % len(cookies_list)]\\n        print(f\\"🚀 Spawn worker {i} với cookies: {cookies}\\")\\n        run_tool.spawn(cookies)\\n        i += 1\\n        time.sleep(5)  # giãn cách spawn","modalEnvironment":"main","winsize":{"rows":16,"cols":93}}'.encode()
#response = requests.post('https://modal.com/api/playground/vudeptrai79006/run', cookies=cookies, headers=headers, data=data)
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
