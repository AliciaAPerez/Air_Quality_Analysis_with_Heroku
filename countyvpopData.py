import csv
import pandas as pd
import json

def pull_csv_cvp():
    file = "static/Data/countyvpop.csv"

    cvp = pd.read_csv(file)

    cvp_json = cvp.to_json(orient="records")

    return cvp_json
