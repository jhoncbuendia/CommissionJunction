from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import models
from bson import json_util
from time import gmtime, strftime




class ListView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListView, self).dispatch(*args, **kwargs)

    def get(self, request):
        lists_objects = models.ListModel.objects.all()
        
        response = {}
        lists =  []
        list_aux = {}
        for l in lists_objects:
             list_aux['pk'] = l.pk
             list_aux['name'] = l.name
             list_aux['productos'] = l.productos
             list_aux['created'] = l.created.strftime("%D %H:%M")
             print "fecha"
             print list_aux['created']
             lists.append(list_aux)
             list_aux = {}

        return HttpResponse(json.dumps(lists,default=json_util.default),
                                    content_type='application/json')

    def put(self, request):
        try:

            data = json.loads(request.body)
            pk = data["list_pk"]
            products = data["products"]

            try:
                lista = models.ListModel.objects.get(pk = int(pk))
                lista.productos = json.dumps(products)
                lista.save()

                lists_objects = models.ListModel.objects.all()
        
                response = {}
                lists =  []
                list_aux = {}
                for l in lists_objects:
                    list_aux['pk'] = l.pk
                    list_aux['name'] = l.name
                    list_aux['productos'] = l.productos
                    list_aux['created'] = l.created.strftime("%D %H:%M")
                    print "fecha"
                    print list_aux['created']
                    lists.append(list_aux)
                    list_aux = {}

                return HttpResponse(json.dumps(lists,default=json_util.default),
                                    content_type='application/json')

                #return HttpResponse("lista modificada con exito")

            except Exception, e:
                return HttpResponse("Producto no encontrado")

            print data
            return HttpResponse("ok")
        except Exception, e:
            return HttpResponse("peticion invalida")

    def post(self, request):
        data = request.body
        try:
            list_data=  json.loads(data)
            list = models.ListModel()
            list.name = list_data['name']
            list.productos = json.dumps(list_data['products'])
            list.save()

        #print data
            return HttpResponse("Lista creada con exito");
        except Exception, e:
            return HttpResponse(str(e.args))

class ListBaseView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListBaseView, self).dispatch(*args, **kwargs)

    def get(self, request, pk):
        try:
            data = []
            list_aux = {}
            list = models.ListModel.objects.get(pk = int(pk))
            list_aux['pk'] = list.pk
            list_aux['name'] = list.name
            list_aux['productos'] = json.loads(list.productos)
            list_aux['created'] = list.created.strftime("%D %H:%M")
            data.append(list_aux)
            return HttpResponse(json.dumps(data,default=json_util.default),
                                    content_type='application/json')
        except Exception, e:
            print e
            return HttpResponse("Lista no encontrada")


    def delete(self, request, pk):
        try:
            list = models.ListModel.objects.get(pk = int(pk))
            list.delete()
            lists_objects = models.ListModel.objects.all()
        
            response = {}
            lists =  []
            list_aux = {}
            for l in lists_objects:
                list_aux['pk'] = l.pk
                list_aux['name'] = l.name
                list_aux['productos'] = l.productos
                list_aux['created'] = l.created.strftime("%D %H:%M")
                print "fecha"
                print list_aux['created']
                lists.append(list_aux)
                list_aux = {}

            return HttpResponse(json.dumps(lists,default=json_util.default),
                                    content_type='application/json')
        except Exception, e:
            return HttpResponse("Lista no encontrada")