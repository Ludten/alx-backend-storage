#!/usr/bin/env python3
"""
lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Return a list of all documents in a collection
    """
    if mongo_collection.find().count() == 0:
        return []
    return mongo_collection.find()
