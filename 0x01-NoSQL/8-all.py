#!/usr/bin/env python3
"""Function lists all documents in a collection"""


def list_all(mongo_collection):
    """Lists all collections"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
