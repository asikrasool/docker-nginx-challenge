from notification import send
import os
# from pymongo import MongoClient
import pymongo
def get_invalid_attempts():



    DATABASE_NAME = os.environ["MONGODB_DATABASE"]
    DATABASE_HOST = os.environ["MONGODB_HOSTNAME"]

    DATABASE_USERNAME = os.environ["MONGODB_USERNAME"]
    DATABASE_PASSWORD = os.environ["MONGODB_PASSWORD"]

    CONNECTION_STRING = "mongodb://flaskuser:flaskuser@"+ DATABASE_HOST +":27017/"
    # CONNECTION_STRING = """mongodb://DATABASE_USERNAME:DATABASE_PASSWORD@DATABASE_HOST:27017/"""
    client = pymongo.MongoClient(CONNECTION_STRING)

    db=client[DATABASE_NAME]
    access=db.get_collection("access")
    result_1 = access.find({
        "response" : { "$eq" : 401}
    })
    return result_1

    
if __name__ == "__main__":    
    
    documents = get_invalid_attempts()
    invalid=list(documents)
    if len(invalid) > 0:
        print("Sending Email")
        send(len(invalid))
    else:
        print("No email sent")

        
