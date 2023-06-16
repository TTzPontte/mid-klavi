import os
import json
import threading
import requests
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4).pprint
def read_json_file(file_path):
    encodings = ['utf-8', 'utf-16', 'latin-1']  # Add more encodings as needed

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                data = json.load(file)
            return data
        except UnicodeDecodeError:
            continue

    # If no successful decoding is achieved, raise an exception or handle the error as needed
    raise ValueError("Unable to decode the JSON file with available encodings.")


def send_request(url, payload):
    # print(f"Payload: {payload}")
    response = requests.post(url, json=payload)
    print("---------------------")
    # pp(f"Response for payload {payload['data']['report_type']}: {response.status_code}, {response.text}")
    pp(response.json())

def main():
    url = "http://127.0.0.1:3000/create"  # Replace with your desired URL

    payload_directory = "../../events/sample"
    payload_files = [f for f in os.listdir(payload_directory) if f.endswith('.json')]

    threads = []
    for file_name in payload_files:
        for name in ['income']:
            if name in file_name:
                file_path = os.path.join(payload_directory, file_name)
                payload = read_json_file(file_path)
                thread = threading.Thread(target=send_request, args=(url, payload))
                threads.append(thread)
                thread.start()

    for thread in threads:
        thread.join()

    print("Done")


if __name__ == "__main__":
    main()
