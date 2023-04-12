import allure

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response


@allure.feature("POST")
class TestMetaApi:
    @allure.story("Создание нового игрока")
    def test_post_player(self):
        # Arrange
        nickname = random_string(10)
        # Act
        result: Response = Api.post_new_player(nickname, "Red Testing Mafia", "Alina Korolenko")
        print(result.request.body)
        print(result.json())

        # Arrange
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
