import os

import psycopg2 as psycopg2
from dotenv import load_dotenv

from all_date import race_info

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
                                        two_6month_escaped REAL)

            """
    cursor.execute(sql)
    connection.commit()
    connection.close()


def add_data(data, place_name, race_number, first_text, one_3month_1win, two_3month_1win, three_3month_1win,
             four_3month_1win, five_3month_1win, six_3month_1win, second_text, one_3month_2win, two_3month_2win,
             three_3month_2win, four_3month_2win, five_3month_2win, six_3month_2win, kimarite_text, one_6month_escape,
             two_6month_escaped):
    # Connectionを貼る
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
          f"VALUES (" \
          f"'20220207', '桐生', '1R', '1着率', 0.0, 15.4, 14.3, 0.0, 0.0, 0.0, " \
          f"'2連対率', 20.0, 23.1, 35.7, 42.9, 0.0, 0.0, '決まり手', 18.8, 57.1)"

    cursor.execute(sql)

    connection.commit()

    connection.close()


def main():
    init_db()

    (data, place_name, race_number, first_text, one_3month_1win, two_3month_1win, three_3month_1win, four_3month_1win,
     five_3month_1win, six_3month_1win, second_text, one_3month_2win, two_3month_2win, three_3month_2win,
     four_3month_2win, five_3month_2win, six_3month_2win, kimarite_text, one_6month_escape,
     two_6month_escaped) = ['20220207', '桐生', '1R', '1着率', 0.0, 15.4, 14.3, 0.0, 0.0, 0.0, '2連対率', 20.0, 23.1, 35.7,
                            42.9, 0.0, 0.0, '決まり手', 18.8, 57.1]

    add_data(data, place_name, race_number, first_text, one_3month_1win, two_3month_1win, three_3month_1win,
             four_3month_1win, five_3month_1win, six_3month_1win, second_text, one_3month_2win, two_3month_2win,
             three_3month_2win, four_3month_2win, five_3month_2win, six_3month_2win, kimarite_text, one_6month_escape,
             two_6month_escaped)

if __name__ == "__main__":
    main()

# def get_connection():
#     """コネクションを貼る関数"""
#     dsn = os.environ.get("DATABASE_URL")
#     return psycopg2.connect(dsn)


# def cursor_execute(sql, params=()):
#     """sqlを実行する関数 select文なら実行結果を返す"""
#     with get_connection() as conn:
#         with conn.cursor() as cur:
#             # cur.execute(sql)
#             cur.execute(sql, params)
#             if sql.split(" ")[0] == "SELECT":
#                 customers = cur.fetchall()
#                 return customers


# def init_db():
#     """データベースの初期化を行う関数"""
#     with open('schema.sql', encoding="utf-8") as f:
#         cursor_execute(f.read())


# def get_all_customers():
#     sql = "SELECT * FROM customers;"
#     customers = cursor_execute(sql)
#     return customers


# def add_customer(name, age):
#     sql = "INSERT INTO customers VALUES (%(name)s, %(age)s);"
#     params = {"name": name, "age": age}
#     cursor_execute(sql, params)


# if __name__ == '__main__':
#     init_db()

# print(init_db.__doc__)
