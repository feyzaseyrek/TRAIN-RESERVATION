import datetime
from pymongo import MongoClient
from sqlalchemy import true

class Vagonlar(object):
    pass



trips = [
    {
        "_id": "6f8af364-7408-48a2-b922-e861467c0e59",

        "stops" : [
            {
                "station_id": "Vagon_1",
                "platform": "1",
                "remaining_seats": 50
            },
            {
                "station_id": "Vagon_2",
                "platform": "2",
                "remaining_seats": 10
            },
            {
                "station_id": "Vagon_3",
                "platform": "3",
                "remaining_seats": 0
            }
        ]

    }
]


def main():
    client = MongoClient('localhost:27017')
    stations_coll = client['octopus']['Vagonlar']
    stations_coll.delete_many({})
    lines_coll = client['octopus']['lines']
    lines_coll.delete_many({})
    trips_coll = client['octopus']['trips']
    trips_coll.delete_many({})
    for station in Vagonlar:
        stations_coll.insert(station)

    for trip in trips:
        trips_coll.insert(trip)

if __name__ == '__main__':
    main()