CREATE TABLE users (
    id INTEGER,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE UNIQUE INDEX username ON users (username);

CREATE TABLE menu(
    id INTEGER NOT NULL,
    name TEXT,
    minute INTEGER,
    wayou BOOLEAN DEFAULT(FALSE),
    taste TEXT,
    overview TEXT,
    seasoning1_id INTEGER NOT NULL,
    seasoning2_id INTEGER NOT NULL,
    main_ingredient_id INTEGER NOT NULL,
    ingredient1_id INTEGER NOT NULL,
    ingredient2_id INTEGER NOT NULL,
    ingredient3_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(seasoning1_id) REFERENCES seasonings(id),
    FOREIGN KEY(seasoning2_id) REFERENCES seasonings(id),
    FOREIGN KEY(main_ingredient_id) REFERENCES ingredients(id),
    FOREIGN KEY(ingredient1_id) REFERENCES ingredients(id),
    FOREIGN KEY(ingredient2_id) REFERENCES ingredients(id),
    FOREIGN KEY(ingredient3_id) REFERENCES ingredients(id)
);

CREATE TABLE seasonings(
    id INTEGER NULL,
    name TEXT,
    flag BOOLEAN DEFAULT(FALSE),
    PRIMARY KEY(id)
);

CREATE TABLE ingredients(
    id INTEGER NOT NULL,
    name TEXT,
    flag BOOLEAN DEFAULT(FALSE),
    element TEXT,
    PRIMARY KEY(id)
);





























--献立テーブル
CREATE TABLE menu(
    id INTEGER NOT NULL,
    name TEXT,
    minute INTEGER,
    wayou BOOLEAN DEFAULT(FALSE),
    taste TEXT,
    overview TEXT,
    seasoning1_id INTEGER NOT NULL,
    seasoning2_id INTEGER NOT NULL,
    main_ingredient_id INTEGER NOT NULL,  --this means like meat
    --ingredient_name1 TEXT,
    --ingredient_name2 TEXT,
    --ingredient_name3 TEXT,
    ingredient1_id INTEGER NOT NULL,
    ingredient2_id INTEGER NOT NULL,
    ingredient3_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(seasoning1_id) REFERENCES seasonings(id),
    FOREIGN KEY(seasoning2_id) REFERENCES seasonings(id),
    FOREIGN KEY(main_ingredient_id) REFERENCES ingredients(id),
    FOREIGN KEY(ingredient1_id) REFERENCES ingredients(id),
    FOREIGN KEY(ingredient2_id) REFERENCES ingredients(id),
    FOREIGN KEY(ingredient3_id) REFERENCES ingredients(id)
);


--調味料一覧テーブル
CREATE TABLE seasonings(
    id INTEGER NULL,
    name TEXT,
    flag BOOLEAN DEFAULT(FALSE),
    PRIMARY KEY(id)
);


--食材一覧テーブル
CREATE TABLE ingredients(
    id INTEGER NOT NULL,
    name TEXT,
    flag BOOLEAN DEFAULT(FALSE),
    element TEXT, --肉（硬め部位）、肉（柔らかめ部位）、野菜（硬め）、野菜（柔らかめ）、その他
    --menu_recognize_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    --FOREIGN KEY(menu_recognize_id) REFERENCES menu(id)
);



--献立の名前、調理時間、和洋、味の傾向、概要を表示

--SELECT name, minute, wayou, taste, overview
--FROM menu
--WHERE seasoning1_id = (
--SELECT id
--FROM seasonings
--WHERE flag = TRUE)
--AND seasonig2_id = (
--SELECT id
--FROM seasonings
--WHERE flag = TRUE)
--AND main_ingredient_id = (
--SELECT id
--FROM ingredients
--WHERE flag = TRUE);


--if menu is exisited, code is like below


--購入を促す食品の要素を出力

--SELECT element
--FROM ingredients
--JOIN menu
--ON ingredients.id = ingredient1_id
--OR ingredients.id = ingredient2_id
--OR ingredients.id = ingredient3_id
--WHERE flag = FALSE





--全体の概要
--ユーザーに、現在使用したい食材の名前・味付け、を選択させ入力として受け取る
--献立名・調理時間・和洋・使用食材名前・使用調味料名前・献立の概要、を出力
--購入すべきレコメンド商品を食材の属性で出力


--DBは自分で設定する？？？

--flagは食品を自分が所持しているかどうかの判定のために導入し、TRUEは所持している状態、FALSEは所持していない状態のためユーザーに購入を促す対象となる
--wayouも同様にTRUE・FALSEで判定しており、TRUEは和、FALSEは洋、を表す




















--購入を促す食品の要素を出力(sub)

--SELECT element
--FROM ingredients
--JOIN menu
--ON name = menu.ingredient1_id
--OR name = menu.ingredient2_id
--OR name = menu.ingredient3_id
--WHERE flag = FALSE
