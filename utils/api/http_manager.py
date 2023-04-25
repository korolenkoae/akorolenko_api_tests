import requests


class HttpManager:
    @staticmethod
    def create_headers():
        headers = {
            "content-type": "application/json",
        }
        return headers

    get_token_headers = {"Content-Type": "application/x-www-form-urlencoded", "accept": "*/*"}
    cookie = ""

    @staticmethod
    def auth(url, user, password):
        result = requests.post(url, auth=(user, password))
        HttpManager.cookie = {"JSESSIONID": result.cookies.get("JSESSIONID")}
        return result

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpManager.create_headers(), cookies=HttpManager.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpManager.create_headers(), cookies=HttpManager.cookie)
        return result

    @staticmethod
    def post_file(url, file, headers=None):
        files = {"file": open(file, "rb")}
        result = requests.post(url, files=files, headers=headers, cookies=HttpManager.cookie)
        return result

    @staticmethod
    def delete(url):
        result = requests.delete(url, headers=HttpManager.create_headers(), cookies=HttpManager.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpManager.create_headers(), cookies=HttpManager.cookie)
        return result
