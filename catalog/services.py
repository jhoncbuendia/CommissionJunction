from django.shortcuts import render
from django.db import connection
import json
from django.http import HttpResponse
from bson import json_util
# Create your views here.


def catalog_service_search(request):
	try:
		tag = request.GET.get('tag', ' ')
		parameters = tag.split( )

		try:
			p0 = parameters[0]
		except Exception, e:
			p0 = ' '

		try:
			p1 = parameters[1]
		except Exception, e:
			p1 = p0

		try:
			p2 = parameters[2]
		except Exception, e:
			p2 = p1

		try:
			p3 = parameters[3]
		except Exception, e:
			p3 = p2

		try:
			p4 = parameters[4]
		except Exception, e:
			p4 = p3


		cursor = connection.cursor()
		cursor.callproc('search_product', (p0, p1, p2, p3, p4))
		data = cursor.fetchall()
		
		return HttpResponse(data[0])
	except Exception, e:	
		return HttpResponse("error getting json: "+str(e.args))

	
