from flask import (
    Flask,
    render_template_string,
    render_template,
    jsonify,
    request,
    redirect)

from flask import current_app
from app import app
from flask_sqlalchemy import SQLAlchemy
from models import *

db = SQLAlchemy(app)
Sites = create_classes_site(db)
County = create_classes_county(db)

# County = create_classes(db)

def get_SQL_AQ_census_query():
    results = db.session.query(Sites.CBSA_Name, Sites.Latitude,Sites.Longitude).all()
    # print(results)
    # site_no = [result[0] for result in results]
    CBSA_Name = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    AQ_cenus_query = [{
        # "site_no": site_no,
        "CBSA_Name": CBSA_Name,
        "Latitude": lat,
        "Longitude": lon,
    }]
    print(AQ_cenus_query)
    return AQ_cenus_query

get_SQL_AQ_census_query()