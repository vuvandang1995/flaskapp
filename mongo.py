# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost')
db = client.liststringxxx
clients = db.Documents


xxx = db.Documents.insert_many(
	[
		{
			"key": "tìm lại bầu trời"
		},
		{
			"key": "chỉ anh hiểu em"
		},
		{
			"key": "hãy tin anh lần nữa"
		},
		{
			"key": "bầu trời của con"
		}
	]
)
