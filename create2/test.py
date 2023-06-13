import json
import threading

import requests


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def send_request(url, payload):
    print("payload: ", payload)
    response = requests.post(url, json=payload)
    print("\n---------------------")
    print(f"Response for payload {payload['data']['report_type']}: {response.status_code}, {response.text}")


def main():
    url = "https://api-portaldev.pontte.com.br/document_interpreter/v1/OpenFinance/create"
    payload1 = read_json_file("../events/paylods/category_checking.json")
    payload2 = read_json_file("../events/paylods/income.json")

    threads = [
        threading.Thread(target=send_request, args=(url, payload1)),
        threading.Thread(target=send_request, args=(url, payload2)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Done")


if __name__ == "__main__":
    main()
