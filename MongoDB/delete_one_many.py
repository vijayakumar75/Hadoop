import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
scores = db.scores


print "update_one reporting for duty"

def add_reviewer_update_one(student):
    try:
        score = scores.find_one({"student" : student })
        record_id = score['_id']

        print record_id

        result = scores.delete_many({"student" : student})
        print result.deleted_count
        
    except Exception as e:
        print "exception is " , type(e) , e

add_reviewer_update_one(1)
    


