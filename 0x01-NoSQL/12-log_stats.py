#!/usr/bin/env python3
"""Script provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Provides some stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_col = client.logs.nginx
    print("{} logs".format(nginx_col.est_document_count()))
    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in method:
        count = nginx_col.count_documents({'method': m})
        print("\tmethod {}: {}".format(method, count))
    stat_get = nginx_col.count_documents({'method': 'GET', 'path': '/status'})
    print("{} status check".format(stat_get))
