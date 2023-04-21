import mysql.connector
from mysql.connector.cursor import MySQLCursorBuffered


class DbConnector():

    def __init__(self) -> object:
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="test_user",
            password="queen",
            database="mafia_api_db",
        )
        self.cursor = self.conn.cursor(buffered=True, cursor_class=MySQLCursorBuffered)

    def get_first_club(self):
        sql_club = "SELECT club_name FROM players_club ORDER BY id ASC LIMIT 1"
        self.cursor.execute(sql_club)
        club_row = self.cursor.fetchone()
        if club_row is not None:
            club_name = club_row[0]
        else:
            club_name = None
        return club_name

    def get_first_player(self):
        sql_club = "SELECT nickname FROM players_player ORDER BY id ASC LIMIT 1"
        self.cursor.execute(sql_club)
        player_row = self.cursor.fetchone()
        if player_row is not None:
            nickname = player_row[0]
        else:
            nickname = None
        return nickname


db = DbConnector()
print(db.get_first_player())
