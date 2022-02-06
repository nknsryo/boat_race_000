

-- もしテーブルが存在したら削除
DROP TABlE IF EXISTS all_race_data;

-- もしテーブルがなかったら作成  customers--テーブル名
CREATE TABLE IF NOT EXISTS all_race_data(
    data TEXT,
    place_name TEXT,
    race_number INTEGER,
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

--  テストデータの挿入
--INSERT INTO
--    -- customers(name, age)とかにするとカラム指定ができる。
--    customers
--VALUES
--    ('Bob', 15),
--    ('Tom', 57),
--    ('Ken', 76)
--    ;
