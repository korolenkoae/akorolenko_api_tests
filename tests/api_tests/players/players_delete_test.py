import allure

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response


@allure.feature("DELETE")
class TestPlayerDeleteApi:
    @allure.story("Удаление пользователей")
    def test_delete_players(self):
        # Arrange
        nickname = random_string(10)
        result: Response = Api.post_new_player(nickname, "Red Testing Mafia", "Alina Korolenko")
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
        response_json = result.json()
        id_player = response_json["id"]
        # Act
        result: Response = Api.delete_players(id_player=id_player)
        # Assert
        response_json_del = result.json()
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        with allure.step("Проверяем что в ответе сообщение об удалении пользователя с id_player"):
            assert response_json_del["message"] == f"Player with ID {id_player} deleted successfully"
