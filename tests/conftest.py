import os
import string
import random

SELENOID_URL = "https://localhost:8000/"
url = os.environ.get("SELENOID_URL", SELENOID_URL)


def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
