# Script send results and generete allure report for Allure Server kochetkov-ma / allure-server
# https://github.com/kochetkov-ma/allure-server
# https://hub.docker.com/r/kochetkovma/allure-server

import sys
import requests
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="send-allure-reports, ver.0.1 beta\n",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-n", "--name", required=True, type=str)
    parser.add_argument("-b", "--browser", required=True, type=str)
    parser.add_argument("-p", "--priority", required=True, type=str)
    parser.add_argument("-i", "--id", required=True, type=str)
    parser.add_argument("-h", "--host", required=True, type=str)
    args = parser.parse_args()
    report_file = {"allureResults": ("allure-results.zip", open("allure-results.zip", "rb"), "application/zip")}
    sys.stdout.write(f"Send allure results: {args.host}\n")
    s = requests.Session()
    upload_response = s.post(f"{args.host}/api/result", files=report_file, timeout=(60 * 3, 60 * 5), verify=False)
    sys.stdout.write(f"Upload results response: {upload_response.text} \n")
    sys.stdout.write(f"Send request for generate report: {args.host}\n")
    generate_body = {
        "reportSpec": {
            "path": [f"{args.name}", f"{args.browser}", f"{args.priority}"],
            "executorInfo": {"buildName": f"#{args.id}"},
        },
        "results": [upload_response.json()["uuid"]],
        "deleteResults": False,
    }
    generate_response = s.post(f"{args.host}/api/report", json=generate_body, timeout=(60 * 3, 60 * 5), verify=False)
    sys.stdout.write(f"Generate report response: {generate_response.text} \n")
    if generate_response.status_code != 201:
        sys.exit(-1)


if __name__ == "__main__":
    main()
