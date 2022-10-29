import os
import requests
import urllib.parse

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

from helpers import apology, login_required#, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
#app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///menu.db")

@app.route("/")
@login_required
def index():
    #user_id = session["user_id"]
    return render_template("index.html")

@app.route("/smenu", methods=["GET", "POST"])
@login_required
def menu_search():
    #pause_minute = db.execute("SELECT minute FROM menu")
    #pause_wayou = db.execute("SELECT wayou FROM menu")
    pause_taste = db.execute("SELECT taste FROM menu")
    pause_main_ingredient = db.execute("SELECT name FROM ingredients")
    pause_ingredient_1 = db.execute("SELECT name FROM ingredients")
    pause_ingredient_2 = db.execute("SELECT name FROM ingredients")
    return render_template("smenu.html", pause_taste=pause_taste, pause_main_ingredient=pause_main_ingredient, pause_ingredient_1=pause_ingredient_1, pause_ingredient_2=pause_ingredient_2)

@app.route("/smenu/result", methods=["GET", "POST"])
@login_required
def menu_search_result():
    if request.method == "POST":
        #pause_minute = request.form.get("pause_minute")
        #pause_wayou = request.form.get("pause_wayou")
        pause_taste = request.form.get("pause_taste")
        pause_main_ingredient = request.form.get("pause_main_ingredient")
        pause_ingredient_1 = request.form.get("pause_ingredient_1")
        pause_ingredient_2 = request.form.get("pause_ingredient_2")

        is_valid = True

        #if not pause_minute:
        #    flash("調理時間を入力してください.")
        #    is_valid = False

        #if not pause_wayou:
        #    flash("和洋を入力してください.")
        #    is_valid = False

        if not pause_taste:
            flash("味の特徴を入力してください.")
            is_valid = False

        if not pause_main_ingredient:
            flash("メイン使用食材を入力してください.")
            is_valid = False

        if not pause_ingredient_1:
            flash("使用食材1を入力してください.")
            is_valid = False

        if not pause_ingredient_2:
            flash("使用食材2を入力してください.")
            is_valid = False


        #try:
        #   アイディアとしてはメイン食材、食材1、食材2、味の特徴、が一致する対象をメニュー提案するものとする
        #   メニュー名は一意的に決まるはず
        #   name = db.execute("SELECT name FROM menu WHERE ...")
        #   wayou = pause_wayou
        #   taste = pause_taste
        #   overview = db.execute("SELECT overview FROM menu WHERE ...")
        #   seasoning_1 = db.execute("SELECT name FROM seasonings WHERE ...")
        #   seasoning_2 = db.execute("SELECT name FROM seasonings WHERE ...")
        #   main_ingredient = pause_main_ingredient
        #   ingredient_1 = pause_ingredient_1
        #   ingredient_2 = pause_ingredient_2
        ##   ingredient_3 = db.execute("SELECT name FROM ingredients WHERE ...")
        #   return render_template("smenul.html", name=name, minute=minute, wayou=wayou, taste=taste, overview=overview, seasoning_1=seasoning_1, seasoning_2=seasoning_2, main_ingredient=main_ingredient, ingredient_1=ingredient_1, ingredient_2=ingredient_2)#, ingredient_3=ingredient_3)
        #except:
        #   存在しなかった場合は、味の特徴が一致するものを調理時間順に献立名のみ表示（買い出し食材の提案は後回し）
        #   メニュー名は複数該当する
        #   failed_name = db.execute("SELECT name FROM menu WHERE taste = ?", pause_taste)
        #   failed_taste = pause_taste
        #   return render_template("smenul.html", failed_name=failed_name, failed_taste=failed_taste)

        return render_template("smenul.html")


    else:
        return redirect("/")


@app.route("/rseasoning", methods=["GET", "POST"])
@login_required
def seasoning_register():
    if request.method == "POST":
        seasoning_name = request.form.get("seasoning_name")
        flag = request.form.get("flag")

        is_valid = True

        if not seasoning_name:
            flash("調味料名を入力してください.")
            is_valid = False

        if not flag:
            flash("所有有無を入力してください.")
            is_valid = False

        #try:
        #    db.execute("INSERT INTO seasonings (name, flag) VALUES (?, ?)", seasoning_name, flag)
        #    return redirect(url_for("register_confirmation"))
        #except:
        #    flash("この調味料は既に登録済みです.")
        #    is_valid = False
        #    return redirect(url_for("seasoning_register"))

        return redirect("/")  #ここを消すだけ
    else:
        return render_template("rseasoning.html")

@app.route("/ringredient", methods=["GET", "POST"])
@login_required
def ingredient_register():
    if request.method == "POST":
        ingredient_name = request.form.get("ingredient_name")
        flag = request.form.get("flag")
        element = request.form.get("element")

        is_valid = True

        if not ingredient_name:
            flash("食材名を入力してください.")
            is_valid = False

        if not flag:
            flash("所有有無を入力してください.")
            is_valid = False

        if not element:
            flash("食材要素を入力してください.")
            is_valid = False

        #try:
        #    db.execute("INSERT INTO ingredients (name, flag, element) VALUES (?, ?, ?)", ingredient_name, flag, element)
        #    return redirect(url_for("register_confirmation"))
        #except:
        #    flash("この食材は既に登録済みです.")
        #    is_valid = False
        #    return redirect(url_for("ingredient_register"))

        return redirect("/")  #ここを消すだけ
    else:
        return render_template("ringredient.html")

@app.route("/rmenu", methods=["GET", "POST"])
@login_required
def menu_register():
    if request.method == "POST":
        menu_name = request.form.get("menu_name")
        minute = request.form.get("minute")
        wayou = request.form.get("wayou")
        taste = request.form.get("taste")
        overview = request.form.get("overview")
        seasonings_1 = request.form.get("seasonings_1")
        seasonings_2 = request.form.get("seasonings_2")
        main_ingredients = request.form.get("main_ingredients")
        ingredients_1 = request.form.get("ingredients_1")
        ingredients_2 = request.form.get("ingredients_2")
        ingredients_3 = request.form.get("ingredients_3")

        is_valid = True

        if not menu_name:
            flash("メニュー名を入力してください.")
            is_valid = False

        if not minute:
            flash("調理時間を入力してください.")
            is_valid = False

        if not wayou:
            flash("和洋を選択してください.")
            is_valid = False

        if not taste:
            flash("味の特徴を入力してください.")
            is_valid = False

        if not overview:
            flash("メニュー概要を入力してください.")
            is_valid = False

        if not seasonings_1:
            flash("使用調味料1を入力してください.")
            is_valid = False

        if not seasonings_2:
            flash("使用調味料2を入力してください.")
            is_valid = False

        if not main_ingredients:
            flash("メイン使用食材を入力してください.")
            is_valid = False

        if not ingredients_1:
            flash("使用食材1を入力してください.")
            is_valid = False

        if not ingredients_2:
            flash("使用食材2を入力してください.")
            is_valid = False

        if not ingredients_3:
            flash("使用食材3を入力してください.")
            is_valid = False

        seasoning1_id = db.execute("SELECT id FROM seasonings WHERE name = ?", seasonings_1)
        seasoning2_id = db.execute("SELECT id FROM seasonings WHERE name = ?", seasonings_2)
        main_ingredient_id = db.execute("SELECT id FROM ingredients WHERE name = ?", main_ingredients)
        ingredient1_id = db.execute("SELECT id FROM ingredients WHERE name = ?", ingredients_1)
        ingredient2_id = db.execute("SELECT id FROM ingredients WHERE name = ?", ingredients_2)
        ingredient3_id = db.execute("SELECT id FROM ingredients WHERE name = ?", ingredients_3)

        #try:
        #    db.execute("INSERT INTO menu (name, minute, wayou, taste, overview, seasoning1_id, seasoning2_id, main_ingredient_id, ingredient1_id, ingredient2_id, ingredient3_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", menu_name, minute, wayou, taste, overview, seasoning1_id, seasoning2_id, main_ingredient_id, ingredient1_id, ingredient2_id, ingredient3_id)
        #    return redirect(url_for("menu_list"))
        #except:
        #    flash("このメニューは既に登録済みです.")
        #    is_valid = False
        #    return redirect(url_for("menu_register"))

        return redirect("/") #ここを消すだけ

    else:
        #user_id = session["user_id"]
        #ingredients = db.execute("SELECT username FROM users")
        seasonings_1 = db.execute("SELECT name FROM seasonings")
        seasonings_2 = db.execute("SELECT name FROM seasonings")
        main_ingredients = db.execute("SELECT name FROM ingredients")
        ingredients_1 = db.execute("SELECT name FROM ingredients")
        ingredients_2 = db.execute("SELECT name FROM ingredients")
        ingredients_3 = db.execute("SELECT name FROM ingredients")
        return render_template("rmenu.html", seasonings_1=seasonings_1, seasonings_2=seasonings_2, main_ingredients=main_ingredients, ingredients_1=ingredients_1, ingredients_2=ingredients_2, ingredients_3=ingredients_3)


@app.route("/rconfirmation", methods=["GET", "POST"])
@login_required
def register_confirmation():
    if request.method == "POST":
        delete_seasoning_name = request.form.get("s_choice")
        delete_ingredient_name = request.form.get("i_choice")

        db.execute("UPDATE seasonings SET flag = False WHERE name = ?", delete_seasoning_name)
        db.execute("UPDATE ingredients SET flag = False WHERE name = ?", delete_ingredient_name)

        seasoning_name = db.execute("SELECT name FROM seasonings WHERE flag = True")
        ingredient_name = db.execute("SELECT name FROM ingredients WHERE flag = True")
        return render_template("rconfirmation.html", seasoning_name=seasoning_name, ingredient_name=ingredient_name)
    else:
        seasoning_name = db.execute("SELECT name FROM seasonings WHERE flag = True")
        ingredient_name = db.execute("SELECT name FROM ingredients WHERE flag = True")
        return render_template("rconfirmation.html", seasoning_name=seasoning_name, ingredient_name=ingredient_name)

@app.route("/lmenu", methods=["GET", "POST"])
@login_required
def menu_list():
    if request.method == "POST":
        return redirect("/")
    else:
        menu_name = db.execute("SELECT name FROM menu")
        return render_template("lmenu.html", menu_name=menu_name)


#@app.route("/timeline", methods=["GET", "POST"])
#@login_required
#def timeline():
#    if request.method == "POST":
#        return redirect("/")
#    else:
#        return render_template("timeline.html")




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        is_valid = True

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("ユーザー名の取得ができませんでした.")
            is_valid = False
            #return apology("ユーザー名の取得ができませんでした.", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("パスワードの取得ができませんでした.")
            is_valid = False
            #return apology("パスワードの取得ができませんでした.", 403)


        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))


        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("無効なユーザー名/パスワードです.")
            is_valid = False
            #return apology("無効なユーザー名/パスワードです.", 403)



        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        is_valid = True

        if not username:
            flash("ユーザー名を入力してください.")
            is_valid = False
            #return apology("ユーザー名を入力してください.")
        elif not password:
            flash("パスワードを入力してください.")
            is_valid = False
            #return apology("パスワードを入力してください.")
        elif not confirmation:
            flash("確認パスワードを入力してください.")
            is_valid = False
            #return apology("確認パスワードを入力してください.")

        if password != confirmation:
            flash("パスワードが一致しません.")
            is_valid = False
            #return apology("パスワードが一致しません.")

        hash = generate_password_hash(password)


        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect(url_for("login"))
        except:
            flash("このユーザー名は既に登録済みです.")
            is_valid = False
            #return apology("このユーザー名は既に登録済みです.")


    else:
        return render_template("register.html")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
