#!/usr/bin/python3

import firebase_admin
import cgi
from random import uniform, randint
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import GeoPoint
from datetime import datetime, timezone

def generate_status() -> str:
    """
    INPUT: None.
    OUTPUT: str -> random status safe or missing
    """
    if randint(0,1):
        return "Safe"
    return "Missing"

def generate_coords() -> dict:
    """
    INPUT: None
    OUTPUT: dict -> randon latitude and longitude values
    """
    return {"latitude": uniform(-90,90), "longitude": uniform(-180,180)}

def filldb() -> dict:
    """
    INPUT: None
    OUTPUT: dict -> Random data uploaded to db

    This function fill the data base with generated random values.
    """
    data = {
        k : {
            u"Device_name": f"Prototype {k}",
            u"Status":generate_status(),
            u"Actual_position":GeoPoint(**generate_coords()),
            u"Historic":{
                f"{i}":{
                    "Position":GeoPoint(**generate_coords()),
                    "Date":datetime.now(tz=timezone.utc)
                }for i in range(1, randint(1,10))
                # f"TS {j}":generate_coords() for j in range(randint(1,10))
            }
        } for k in range(1, 5)
    }
    for i in data:
        db.collection(u'GPS').document(f'{i}').set(data[i])   

    return data

def get_info(idd: float, parameter : str):
    """
    INPUT:
        idd: int <- the id of the wanted device
        parameter: str <- Info to get
    OUTPUT: if Historic exists: value of parameter
            else: False
    Function to retrive info from the db
    """
    doc_ref = db.collection(u"GPS").document(f"{idd}")
    doc = doc_ref.get()
    if doc.exists:
        if parameter != "full":
            if "Historic" not in doc.to_dict() and parameter == "Historic":
                return {}
            return doc.to_dict()[f"{parameter}"]
        return doc.to_dict()
    return False

def update_parameter(idd: float, parameter : str, value):
    """
    INPUT:
        idd: int <- the id of the wanted device
        parameter: str <- Info to get
        value: str <- Info to update
    OUTPUT: None

    """
    data = get_info(idd, "full")
    data[parameter] = value
    db.collection(u"GPS").document(f"{idd}").set(data)

def assing_id() -> float:
    """
    INPUT: None
    OUTPUT: float -> new id

    Function to generate a new id into the db
    """
    
    docs = db.collection(u"GPS").stream()
    ids = []

    for doc in docs:
        # print(f"{doc.id}")
        ids.append(float(doc.id))

    ids.sort()
    new_id = max(ids)+1
    empty_field = {
        "Actual_position":None,
        "Device_name": f"Prototype {new_id}",
        "Status":"Safe"
    }
    db.collection(u"GPS").document(f"{new_id}").set(empty_field)
    return new_id

def parser(idd : float, latitude : float, longitude : float):
    status = get_info(idd, "Status")
    
    if status:
        update_parameter(idd, "Actual_position", GeoPoint(latitude= latitude, longitude = longitude))
        if status == "Missing":
            Hist = get_info(idd, "Historic")

            Hist[f"{len(Hist)+1}"] = {
                u"Position": GeoPoint(latitude= latitude, longitude = longitude),
                u"Date": datetime.now(tz=timezone.utc)
            }
            update_parameter(idd, "Historic", Hist)

    else:
        data = {
            u"Device_name": f"Prototype {idd}",
            u"Status": "Safe",
            u"Actual_position": GeoPoint(latitude= latitude, longitude = longitude),
        }
        db.collection(u"GPS").document(f"{idd}").set(data)
        return data

def send_info(args) -> bool:
    #print(args)
    #if not {'idd', 'latitude', 'longitude'} == set(args.keys()): # checking format 
    #    print("Incorrect parameters")
    #    return False

    try:
        data = {i:float(args[i][0]) for i in args}
    except:
        print("Not float parameters")
        return False

    # print(data)
    # parser(**data)
    # return True
    if ({'idd', 'latitude', 'longitude'} == set(args.keys())):
        print(data)
        parser(**data)
        return True
    elif not args: # if its empty
        print(assing_id())
        return True
    return False


# Use a service account
cred = credentials.Certificate('auth.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
# with open("data2.json", 'r') as f:
#     f = json.loads(f.read())
#     print(f)

# data = {
#     u"username": "test",
#     u"Actual_position":GeoPoint(**generate_coords()),
#     u"Fecha": datetime.now(tz=timezone.utc),
#     u"hist":{
#         "Fecha":datetime.now(tz=timezone.utc),
#         "Lugar":GeoPoint(**generate_coords())
#     }
# }
print('Content-Type: text/plain')
print('')

args = cgi.parse()
#print(bool(args))

send_info(args)

