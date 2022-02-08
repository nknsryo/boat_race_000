import csv
import os

import psycopg2 as psycopg2
from dotenv import load_dotenv

load_dotenv()


def init_db():
    # Connectionを貼る
    dsn = os.environ.get('DATABASE_URL')
    connection = psycopg2.connect(dsn)

    cursor = connection.cursor()

    with open('schema.sql', encoding='utf-8') as f:
        cursor.execute(f.read())

    connection.commit()

    connection.close()


def add_data():
    dsn = os.environ.get('DATABASE_URL')
    connection = psycopg2.connect(dsn)

    cursor = connection.cursor()

    # CSVファイルを開く
    with open('test_02.csv', 'rt', encoding='utf_8_sig') as fp:
        # CSVを読み込む
        reader = csv.reader(fp)

        # 一行ずつ処理する
        for row in reader:
            data = row[0]
            place_name = row[1]
            race_number = row[2]
            first_text = row[3]
            one_3month_1win = row[4]
            two_3month_1win = row[5]
            three_3month_1win = row[6]
            four_3month_1win = row[7]
            five_3month_1win = row[8]
            six_3month_1win = row[9]
            second_text = row[10]
            oen_3month_2win = row[11]
            two_3month_2win = row[12]
            three_3month_2win = row[13]
            four_3month_2win = row[14]
            five_3month_2win = row[15]
            six_3month_2win = row[16]
            third_text = row[17]
            one_3month_3win = row[18]
            two_3month_3win = row[19]
            three_3month_3win = row[20]
            four_3month_3win = row[21]
            five_3month_3win = row[22]
            six_3month_3win = row[23]
            kimarite_text = row[24]
            one_6month_escape = row[25]
            one_6month_escaped = row[26]

            cursor.execute('''INSERT INTO all_race_data (data,place_name,race_number,
                    first_text,one_3month_1win,two_3month_1win,three_3month_1win,four_3month_1win,five_3month_1win,six_3month_1win,
                    second_text,oen_3month_2win,two_3month_2win,three_3month_2win,four_3month_2win,five_3month_2win,six_3month_2win,
                    third_text,one_3month_3win,two_3month_3win,three_3month_3win,four_3month_3win,five_3month_3win,six_3month_3win,
                    kimarite_text,one_6month_escape,one_6month_escaped)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
                data, place_name, race_number, first_text, one_3month_1win, two_3month_1win, three_3month_1win,
                four_3month_1win, five_3month_1win, six_3month_1win, second_text, oen_3month_2win, two_3month_2win,
                three_3month_2win, four_3month_2win, five_3month_2win, six_3month_2win, third_text, one_3month_3win,
                two_3month_3win, three_3month_3win, four_3month_3win, five_3month_3win, six_3month_3win,
                kimarite_text, one_6month_escape, one_6month_escaped
            ))

    with open('add_info.sql', encoding='utf-8') as add:
        cursor.execute(add.read())

    connection.commit()

    connection.close()

    #
    # sql = f"INSERT INTO all_race_data(" \
    #       data," \
    #       place_name," \
    #       race_number," \
    #       first_text," \
    #       one_3month_1win," \
    #       two_3month_1win," \
    #       three_3month_1win," \
    #       four_3month_1win," \
    #       five_3month_1win," \
    #       six_3month_1win," \
    #       second_text," \
    #       one_3month_2win," \
    #       two_3month_2win," \
    #       three_3month_2win," \
    #       four_3month_2win," \
    #       five_3month_2win," \
    #       six_3month_2win," \
    #       kimarite_text," \
    #       one_6month_escape," \
    #       two_6month_escaped" \
    #       )" \
    #       f"VALUES ({race_info[0]},{race_info[2]},{race_info[3]},{race_info[4]},{race_info[5]}," \
    #       f"{race_info[6]},{race_info[7]},{race_info[8]},{race_info[9]},{race_info[10]}," \
    #       f"{race_info[11]},{race_info[12]},{race_info[13]},{race_info[14]},{race_info[15]}," \
    #       f"{race_info[16]},{race_info[17]},{race_info[18]},{race_info[19]})"

# def main():
#     init_db()
#     add_data()
#
# if __name__ == "__main__":
#     main()
