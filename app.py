# author : fatma feyza seyrek
import re
from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from sqlalchemy import true

app = Flask(__name__)
db = MongoClient('localhost').get_database('octopus')


@app.route('/', methods=['GET'])
def get_home():
    return jsonify({
        'app_name': 'Tren Rezervasyonu',


        "Tren":
            {
                "Ad": "Başkent Ekspres",
                "Vagonlar":
                     [
                            {"_id": "Vagon_1", "Ad": "Vagon1", "Kapasite": 100, "DoluKoltukAdet": 50},
                            {"_id": "Vagon_2", "Ad": "Vagon2", "Kapasite": 90, "DoluKoltukAdet": 80},
                            {"_id": "Vagon_3", "Ad": "Vagon3", "Kapasite": 80, "DoluKoltukAdet": 80},
                    ]
            },
            "RezervasyonYapilacakKisiSayisi": 3,
            "KisilerFarkliVagonlaraYerlestirilebilir": true


    })


@app.route('/Vagonlar', methods=['GET'])
def get_stations():
    stations = list(db.stations.find())
    return jsonify(stations)


@app.route('/Vagonlar/<id>', methods=['GET'])
def get_station(id):
    station = list(db.stations.find_one({"_id":id}))
    if station is not None:
        return jsonify(station)
    else:
        error_response = jsonify({"error": "{} veritabanında yok.".format(id)})
        error_response.status_code = 400
        return error_response 


@app.route('/Vagonlar', methods=['POST'])
def get_station():
    json_data = request.get_json()
    try:
        station_id = "".join(re.findall(r'[a-zA-Z]', json_data["Ad"])).lower()
        station_name = json_data["Ad"]
        station_capacity = json_data["Kapasite"]
        db.stations.insert(
            {"_id": station_id, "Ad": station_name, "Kapasite": station_capacity})
        return jsonify({"id": station_id})
    except KeyError as e:
        error_response = jsonify({"error": "RezervasyonYapilabilir./n YerleşimAyrinti{}".format(e)})
        error_response.status_code = 400
        return error_response



@app.route('/Vagonlar/<id>', methods=['POST'])
def get_station(id):
    json_data = request.get_json()
    db.stations.insert(
        {"_id": id},
        {"$set":

          {
                "RezervasyonYapilabilir": true,
                "YerlesimAyrinti": [
                    {"VagonAdi": "Vagon 1", "KisiSayisi": 2},
                    {"VagonAdi": "Vagon 2", "KisiSayisi": 1}
                ]
          }

         }
    )
    return jsonify({"id": id})



