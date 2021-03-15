import os
import psycopg2

from flask import (
    Flask,
    render_template_string,
    render_template,
    jsonify,
    request,
    redirect)

from models import create_classes
from currentAQIData import get_csv
from timelapse import *

app = Flask(__name__)
# # Menu(app=app)


# # DATABASE_URL will contain the database connection string: HEROKU
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///AirQuality.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # Connects to the database using the app config
db = SQLAlchemy(app)

Sites = create_classes(db)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/countyvpop")
def countryvpop():
    return render_template("countyvpop.html")

@app.route("/current")
def current():
    currentAQIData = get_csv()
    return render_template("current.html", currentAQIData=currentAQIData)

@app.route("/historical_form")
def historical_form():
    return render_template("historical_form.html")

@app.route("/historical_map")
def historical_map():
    return render_template("historical_map.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/sources")
def sources():
    return render_template("sources.html")

@app.route("/timelapse")
def timelapse():
    details = get_timelapse()
    return render_template(
        'timelapse.html',
        map_id = details[0],
        hdr_txt=details[1],
        script_txt = details[2]
    )

@app.route("/yearlyvpop")
def yearlyvpop():
    return render_template("yearlyvpop.html")

@app.route("/currentAQIData")
def csv():
    return get_csv()

@app.route("/timelapseData")
def timelapseData():
    return get_timelapse()

@app.route("/db_test")
def db_test():
    results = db.session.query(Sites).all()
    print(results)
    # aq_data = [{
    #     "site_no": site_no,
    #     "CBSA_Name": CBSA_Name,
    #     "Latitude": Latitude,
    #     "Longitude": Longitude,
    # }]
    # print(aq_data)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

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

if __name__ == '__main__':
    app.run(debug=True)