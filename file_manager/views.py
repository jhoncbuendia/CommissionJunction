from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.
import urllib2
import urllib
import time
import gzip
import uuid
import csv
import sys
import re
import os
import gzip 

def get_csv(request):
	try:
		archivo = request.GET.get('file', ' ')
		#download_path = '/home/jhon/files/'
		download_path = '/home/jhoncbuendia/files/'
		base_url = 'http://datatransfer.cj.com/datatransfer/files/4177550/outgoing/productcatalog/146580/'
		test_url = 'http://datatransfer.cj.com/datatransfer/files/4177550/outgoing/productcatalog/146580/Amiclubwear-Product_Catalog.txt.gz'
		username = '4177550'
		password = '?c3zZasB'
		
		

		p = urllib2.HTTPPasswordMgrWithDefaultRealm()
		p.add_password(None, base_url+archivo, username, password)
		handler = urllib2.HTTPBasicAuthHandler(p)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)
		response = urllib2.urlopen(base_url+archivo).read()

		#grabando csv
		file_ = open(download_path+str(archivo), 'w')
		file_.write(response)
		file_.close()

		#descomprimiendo csv
		f = gzip.open(download_path+str(archivo), 'rb')
		open(download_path+"uncompressed.txt", "wb").write(f.read())
		#print a.read()

		#print response
		#req = urllib2.Request("http://datatransfer.cj.com/datatransfer/files/4177550/outgoing/productcatalog/146580/Amiclubwear-Product_Catalog.txt.gz", data)
		#response = urllib2.urlopen(req)
		#result = response.read()
		#print result
		return HttpResponse("file downloaded "+ str(archivo))
	except urllib2.HTTPError, e:
		print download_path+str(archivo)
		return HttpResponse("error downloading file: "+str(e.args))



def import_csv_view(request):
	return render(request, 'file_manager/import_csv.html')



def import_csv_action( request):
	try:
		cursor = connection.cursor()
		cursor.callproc('import_csv')
		data = cursor.fetchall()
		
		return HttpResponse("file imported successfully ")
	except Exception, e:	
		return HttpResponse("error importing file: "+str(e.args))

