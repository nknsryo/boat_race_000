import os

import psycopg2 as psycopg2
from dotenv import load_dotenv

from all_data_to_db import race_info

load_dotenv()


def init_db():
    # Connectionを貼る
    dsn = os.environ.get('DATABASE_URL')
    connection = psycopg2.connect(dsn)

    # カーソルオブジェクトを作る
    cursor = connection.cursor()

    # SQLを準備
    sql = """DROP TABlE IF EXISTS all_race_data;
            CREATE TABLE IF NOT EXISTS all_race_data(
                                        data TEXT,
                                        place_name TEXT,
                                        race_number TEXT,
                                        first_text TEXT,
                                        one_3month_1win REAL,
                                        two_3month_1win REAL,
                                        three_3month_1win REAL,
                                        four_3month_1win REAL,
                                        five_3month_1win REAL,
                                        six_3month_1win REAL,
                                        second_text TEXT,
                                        one_3month_2win REAL,
                                        two_3month_2win REAL,
                                        three_3month_2win REAL,
                                        four_3month_2win REAL,
                                        five_3month_2win REAL,
                                        six_3month_2win REAL,
                                        kimarite_text TEXT,
                                        one_6month_escape REAL,
                                        two_6month_escaped REAL
                                        )

            """
    cursor.execute(sql)
    connection.commit()
    connection.close()


def add_data():
    dsn = os.environ.get('DATABASE_URL')
    connection = psycopg2.connect(dsn)

    cursor = connection.cursor()

    sql = f"INSERT INTO all_race_data(" \
          f"data," \
          f"place_name," \
          f"race_number," \
          f"first_text," \
          f"one_3month_1win," \
          f"two_3month_1win," \
          f"three_3month_1win," \
          f"four_3month_1win," \
          f"five_3month_1win," \
          f"six_3month_1win," \
          f"second_text," \
          f"one_3month_2win," \
          f"two_3month_2win," \
          f"three_3month_2win," \
          f"four_3month_2win," \
          f"five_3month_2win," \
          f"six_3month_2win," \
          f"kimarite_text," \
          f"one_6month_escape," \
          f"two_6month_escaped" \
          f")" \
          f"VALUES ({race_info[0]},{race_info[2]},{race_info[3]},{race_info[4]},{race_info[5]}," \
          f"{race_info[6]},{race_info[7]},{race_info[8]},{race_info[9]},{race_info[10]}," \
          f"{race_info[11]},{race_info[12]},{race_info[13]},{race_info[14]},{race_info[15]}," \
          f"{race_info[16]},{race_info[17]},{race_info[18]},{race_info[19]})"

    cursor.execute(sql)

    connection.commit()

    connection.close()


def main():
    init_db()


if __name__ == "__main__":
    main()
