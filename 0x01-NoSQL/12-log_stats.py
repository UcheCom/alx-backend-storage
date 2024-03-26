#!/usr/bin/env python3
"""Script provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Provides some stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx
    print("{} logs".format(nginx_coll.est_document_count()))
    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in method:
        print("\tmethod {}: {}".format(
            m,
            nginx_coll.count_documents({'method': m})

    print("{} status check".format(
        nginx_coll.count_documents({'method': 'GET', 'path': '/status'})))
