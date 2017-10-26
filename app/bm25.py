# -*- coding: utf-8 -*-
import operator
from math import log
from underthesea import word_sent
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from pymongo import MongoClient
Client = MongoClient('localhost')



liststring = []
for Document in Client.liststringxxx.Documents.find():
	liststring.append(Document['key'])



def tachtu(x):
	dem = 0
	list_tu = []
	for i in range(len(x)):
		if x[i] == ' ':
			a = ""
			for j in range(dem,i):
				a = a + x[j]
			list_tu.append(a)
			dem = i+1
			print(" ")
	a = ""
	for k in range(dem,len(x)):
		a = a + x[k]
	list_tu.append(a)
	return list_tu

def xacsuat(a,b):
		dem = 0
		for i in b:
			if a == i:
				dem = dem + 1
		return dem

def TF(b):
	list_f = []
	for  i in b:
		dem = 0
		for j in b:
			if i == j:
				dem = dem + 1
		list_f.append(dem)
	list_f.sort()
	return list_f[len(list_f) - 1]


def avgdl(y):
	dem = 0
	for i in y:
		dem = dem + len(i)
	z = dem/float(len(y))
	return z


# IDF
def sovanban(a, b):
	dem = 0
	for i in b:
		for j in i:
			if a == j:
				dem = dem + 1
				break
	return dem

def IDF(a, b):
	if (sovanban(a, b) == 0) | (sovanban(a, b) == len(b)):
		x = log(len(b) / (sovanban(a, b) + 1))
	else:
		x = log(len(b) / sovanban(a, b))
	return x

# BM25
def BM25(f, D, avgdl, idf):
	x = (idf * f * (1.2 + 1)) / float((f + 1.2 *(1 - 0.75 + (0.75 * D)/avgdl )))
	return x



def timkiem(tukhoa):
	#tukhoa = unicode(tukhoa, errors='replace')
	tukhoa = word_sent(tukhoa, format="text")
	y = tachtu(tukhoa)

	liststring1 = []
	for string in liststring:
		string = word_sent(string, format="text")
		liststring1.append(tachtu(string))

	
	list_bm25 = []
	for i in liststring1:
		bm25 = 0
		for j in y:
			xacsuat1 = (xacsuat(j, i) / TF(i))
			D = len(i)
			avgdl1 = avgdl(liststring1)
			idf1 = IDF(j, liststring1)
			bm25 = bm25 + BM25(xacsuat1, D, avgdl1, idf1)
		list_bm25.append(bm25)

	dict = {}
	for j in range(len(liststring)):
		dict[liststring[j]] = list_bm25[j]

	sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
	sorted_x.reverse()
	lists = []
	for i in sorted_x:
		if i[1] != 0:
			lists.append(i[0])
	return lists



