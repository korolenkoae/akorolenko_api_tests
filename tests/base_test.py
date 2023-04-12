import os


class BaseTest:
    API_URL = "http://localhost:8000"
    apiurl = os.environ.get("API_URL", API_URL)
