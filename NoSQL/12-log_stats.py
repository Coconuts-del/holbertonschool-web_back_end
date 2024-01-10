#!/usr/bin/env python3
"""  provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def main():
    """ Connect to MongoDB
        Count total number of logs
        Count logs for each HTTP method
        Count logs with method=GET and path=/status """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in http_methods:
        method_counts[method] = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_counts[method]}")
    status_check_count = collection.count_documents(
                         {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    main()
