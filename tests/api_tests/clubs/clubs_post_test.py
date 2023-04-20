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
        result: Response = Api.post_new_club(city="Moscow", club_name=club_name)
        response_json = result.json()
        id_club = response_json["id"]
        # Arrange
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
        with allure.step(f"Проверяем что в ответе параметр id={id_club}"):
            assert response_json["id"] == id_club

        Api.delete_clubs(id_club=id_club)  # удаляем созданный клуб после теста
