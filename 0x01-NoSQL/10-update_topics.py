#!/usr/bin/env python3
"""Module changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """This updates the topics of the collections"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
