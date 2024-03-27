#!/usr/bin/env python3
"""Module is an improved script that provides some stats about Nginx logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    """This improves and adds top 10 of the most present IPs
       in the collection nginx of the database logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    ng_col = client.logs.nginx
    print("{} logs".format(ng_col.estimated_document_count()))
    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for meth in method:
        count = ng_col.count_documents({'method': meth})
        print("\tmethod {}: {}".format(method, count))
    stat_get = col.count_documents({'method': 'GET', 'path': "/status"})
    print("{} status check".format(stat_get))
    print("IPs:")
    top_ips = ng_col.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    for ip in top_ips:
        print("\t{}: {}".format(ip.get('ip'), ip.get('count')))
