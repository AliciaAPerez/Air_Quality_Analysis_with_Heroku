import os
import psycopg2
from flask import Flask
from flask import render_template_string
from flask import render_template
# from flask import flask_menu
# from flask_menu import Menu, register_menu
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Menu(app=app)


# DATABASE_URL will contain the database connection string: HEROKU
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connects to the database using the app config
# db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

# def tmpl_show_menu():
#     return render_template_string(
#         """
#         {%- for item in current_menu.children %}
#             {% if item.active %}*{% endif %}{{ item.text }}
#         {% endfor -%}
#         """)

# @app.route('/')
# @register_menu(app, '.', 'Home')
# def index():
#     return tmpl_show_menu()

# @app.route('/first')
# @register_menu(app, '.first', 'First', order=0)
# def first():
#     return tmpl_show_menu()

# @app.route('/second')
# @register_menu(app, '.second', 'Second', order=1)
# def second():
#     return tmpl_show_menu()

# if __name__ == '__main__':
#     app.run(debug=True)