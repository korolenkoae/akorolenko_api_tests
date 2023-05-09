import allure

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response


@allure.feature("PUT")
class TestClubPutApi:
    @allure.story("Редактирование пользователей")
    def test_put_players(self):
        # Arrange
        nickname = random_string(10)
        result: Response = Api.post_new_player(nickname, club="Red Testing Mafia", name="Alina Korolenko")
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
        response_json = result.json()
        put_id_player = response_json["id"]
        put_nickname = random_string(10)
        put_club = random_string(10)
        put_name = random_string(10)
        # Act
        result: Response = Api.put_players(
            put_id_player=put_id_player, nickname=put_nickname, club=put_club, name=put_name
        )
        # Assert
        response_json_put = result.json()
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        with allure.step("Проверяем что в ответе сообщение об обновлении пользователя с put_id_player"):
            assert response_json_put["message"] == f"Player with ID {put_id_player} updated successfully"

        Api.delete_players(id_player=put_id_player)  # удаляем созданного пользователя после теста
