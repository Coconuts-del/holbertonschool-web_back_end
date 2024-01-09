#!/usr/bin/env python3
"""  provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def main():
    # Connect to MongoDB
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Count total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    # Count logs for each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    # Count logs with method=GET and path=/status
    status_check_count = collection.count_documents(
                         {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    main()