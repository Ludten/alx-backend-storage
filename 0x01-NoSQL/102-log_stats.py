#!/usr/bin/env python3
"""
stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def top_ips(mongo_collection):
    """
    returns all ip sorted by count
    """
    return mongo_collection.aggregate([
        {
            "$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, req_count))
    print("{} status check".format(nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})))
    print('IPs:')
    top_ip = top_ips(nginx_collection)
    for ip in top_ip:
        print("\t{}: {}".format(ip.get('_id'), ip.get('count')))
