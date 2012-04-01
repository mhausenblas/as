"""
Imports the content of a CSV (with header row) into a CouchDB database.
based on http://stackoverflow.com/questions/5238387/how-to-import-csv-tsv-data-to-couch-db

Usage:

 python fill_datastore.py as-input.csv https://dequilibrium.cloudant.com as
"""
from couchdbkit import Server, Database
from couchdbkit.loaders import FileSystemDocsLoader
from restkit import BasicAuth
from csv import DictReader
import sys, subprocess, math, os

cloudant_username = 'xxx';
cloudant_password = 'xxx';

def parse_doc(doc):
	for k,v in doc.items():
		if (isinstance(v,str)):
			#print k, v, v.isdigit()
			# #see if this string is really an int or a float
			if v.isdigit()==True: #int
				doc[k] = int(v)
			else: #try a float
				try:
					if math.isnan(float(v))==False:
						doc[k] = float(v) 
				except:
					pass
	return doc


def upload(db, docs):
	db.bulk_save(docs)
	del docs
	return list()


def upload_file(fname, uri, dbname):
	print 'Upload contents of %s to %s/%s' % (fname, uri, dbname)
	theServer = Server(uri, filters=[BasicAuth(cloudant_username, cloudant_password)])
	db = theServer.get_or_create_db(dbname)
	reader = DictReader(open(fname, 'rU'), dialect = 'excel')
	docs = list()
	checkpoint = 100
	for doc in reader:
		newdoc = parse_doc(doc) 
		docs.append(newdoc)
		if len(docs)%checkpoint==0:
			docs = upload(db,docs)
	docs = upload(db,docs)

if __name__=='__main__':
	filename = sys.argv[1]
	uri = sys.argv[2]
	dbname = sys.argv[3]
	try:
		upload_file(filename, uri, dbname)
	except: pass