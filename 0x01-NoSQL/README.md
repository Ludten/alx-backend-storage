# NoSQL
> Each file in this repository holds code that illustrates NoSQL
> specific to DBMS.

## Description of what each file shows:
* 0-list_databases: A script that lists all databases in MongoDB.

* 1-use_or_create_database: A script that creates or uses the database `my_db`

* 2-insert: A script that inserts a document in the collection `school`:

	- The document must have one attribute `name` with value “Holberton school”
	- The database name will be passed as option of `mongo` command

* 3- all: A script that lists all documents in the collection `school`:

	- The database name will be passed as option of `mongo` command

* 4-match: A script that lists all documents with `name="Holberton school"` in the collection `school`:

	- The database name will be passed as option of `mongo` command

* 5-count: A script that displays the number of documents in the collection `school`:

	- The database name will be passed as option of `mongo` command

* 6-update: A script that adds a new attribute to a document in the collection `school`:

	- The script should update only document with `name="Holberton school"` (all of them)
	- The update should add the attribute `address` with the value “972 Mission street”
	- The database name will be passed as option of `mongo` command

* 7-delete: A script that deletes all documents with `name="Holberton school"` in the collection `school`:

	- The database name will be passed as option of `mongo` command

* 8-all.py: Python function that lists all documents in a collection:

	- Prototype: `def list_all(mongo_collection):`
	- Return an empty list if no document in the collection
	- `mongo_collection` will be the `pymongo` collection object

* 9-insert_school.py: A Python function that inserts a new document in a collection based on `kwargs`:

	- Prototype: `def insert_school(mongo_collection, **kwargs):`
	- `mongo_collection` will be the `pymongo` collection object
	- Returns the new `_id`

* 10-update_topics.py: A Python function that changes all topics of a school document based on the name:

	- Prototype: `def update_topics(mongo_collection, name, topics):`
	- `mongo_collection` will be the `pymongo` collection object
	- `name` (string) will be the school name to update
	- `topics` (list of strings) will be the list of topics approached in the school

* 11-schools_by_topic.py: A Python function that returns the list of school having a specific topic:

	- Prototype: `def schools_by_topic(mongo_collection, topic):`
	- `mongo_collection` will be the `pymongo` collection object
	- `topic` (string) will be topic searched

* 12-log_stats.py: A Python script that provides some stats about Nginx logs stored in MongoDB:

	- Database: `logs`
	- Collection: `nginx`
	- Display (same as the example):
		- first line: `x logs` where `x` is the number of documents in this collection
		- second line: `Methods`:
		- 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
		- one line with the number of documents with:
			- `method=GET`
			- `path=/status`

	You can use this dump as data sample: [dump.zip](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/6/645541f867bb79ae47b7a80922e9a48604a569b9.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230117T000825Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=abf7b3862efa4a43d3a54f2b368ad45be3e41111c6dfc1876a75390bb1ec772d)

* 100-find: A script that lists all documents with `name` starting by `Holberton` in the collection `school`:

	- The database name will be passed as option of `mongo` command

* 101-students.py: A Python function that returns all students sorted by average score:

	- Prototype: `def top_students(mongo_collection):`
	- `mongo_collection` will be the `pymongo` collection object
	- The top must be ordered
	- The average score must be part of each item returns with key = `averageScore`

* 102-log_stats.py: Improve `12-log_stats.py` by adding the top 10 of the most present IPs in the collection nginx of the database `logs`:

	- The IPs top must be sorted
