import mysql.connector

from mysql.connector.cursor import MySQLCursorBuffered


class DbConnector(object):
    def __init__(self):
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

    def get_max_club_id(self):
        sql_max_id = "SELECT MAX(id) FROM players_club"
        self.cursor.execute(sql_max_id)
        max_id_row = self.cursor.fetchone()
        if max_id_row is not None:
            max_id = max_id_row[0]
            new_id_club = max_id
        else:
            new_id_club = None
        return new_id_club
