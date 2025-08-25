import requests
import time

# === Cookies copy từ F12 ===
cookies = {
    'INGRESSCOOKIE': '1756138140.637.344.358970|9de6a539c14bab7f9073ed2b75abad44',
    'modal-csrf-token': 'ziZO8j9FIEJ1cwpnRvctEzDpxk94bT',
    'modal-session': 'se-rTs8miUne8ydHYWaWzpbfV:xx-Ccmpp2PP2KKSi2GQRxBsUb',
    'ajs_anonymous_id': 'e40f2e27-bb9b-456c-a62e-98521fdc63e3',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%220198e1fd-773e-718d-ba8c-9f4aaf12ff38%22%2C%22%24sesid%22%3A%5B1756138213072%2C%220198e1fd-773d-7f27-919a-15536991e14a%22%2C1756138141500%5D%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fplayground%22%7D%7D',
}

# === Headers copy từ F12 ===
headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://modal.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

# === URL API (copy từ cURL) ===
url = "https://modal.com/api/playground/phamquanghuyfb010/run"

# === Payload (code bạn muốn chạy) ===
json_data = {
    'tutorial': 'get_started',
    'code': 'print("Hello from Modal CMD tool!")',
    'modalEnvironment': 'main',
    'winsize': {'rows': 16, 'cols': 93},
}


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
