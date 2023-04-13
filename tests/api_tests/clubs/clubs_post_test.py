import allure

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response


@allure.feature("POST")
class TestClubPostApi:
    @allure.story("Создание нового клуба")
    def test_post_club(self):
        # Arrange
        club_name = random_string(10)
        # Act
        result: Response = Api.post_new_club("Moscow", club_name)
        # Arrange
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
