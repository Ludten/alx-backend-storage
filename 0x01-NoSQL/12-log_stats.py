#!/usr/bin/env python3
"""
stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    print(
        """\tmethod GET: {}
    \tmethod POST: {}
    \tmethod PUT: {}
    \tmethod PATCH: {}
    \tmethod DELETE: {}
        """.format(
            nginx_collection.count_documents({"method": "GET"}),
            nginx_collection.count_documents({"method": "POST"}),
            nginx_collection.count_documents({"method": "PUT"}),
            nginx_collection.count_documents({"method": "PATCH"}),
            nginx_collection.count_documents({"method": "DELETE"})
        )
    )
    print("{} status check".format(nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})))
