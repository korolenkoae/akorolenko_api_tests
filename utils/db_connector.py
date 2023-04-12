from db_wrapper import DbWrapper


class DbConnector(DbWrapper):
    def __init__(self):
        super().__init__(
            host="127.0.0.1",
            user="test_user",
            password="queen",
            database="mafia_api_db",
        )
