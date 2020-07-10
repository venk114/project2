from django.shortcuts import render
from django.views.generic import View
import json
from app7.models import CousreModel
from django.http import HttpResponse
from app7.naveen import CourseForm
from django.core.serializers import serialize

class InsertOneCourse(View):
    def post(self,request):
        data = request.body
        dict_data = json.loads(data)
        #CousreModel(name=dict_data["name"],fee= dict_data["fee"]).save()
        cf = CourseForm(dict_data)
        if cf.is_valid():
            cf.save()
            json_data = json.dumps({"meassage":"Cousre is succesfully saved"})
        else:
            json_data = json.dumps({"message":cf.errors})
        return HttpResponse(json_data,content_type="application/json")

    def get(self,request,pid):
        try:
           res = CousreModel.objects.get(idno=pid)
           json_data = serialize("json",[res])
        except CousreModel.DoesNotExist:
            json_data = json.dumps({"message":"product does not exist"})
        return HttpResponse(json_data,content_type="application/json")

    def put(self,request):
        pass
    def delete(self,request,pid):
        try:
           res = CousreModel.objects.get(idno=pid)
           res.delete(pid)
           json_data = json.dumps({"message":"product is deleted succesfully"})
        except CousreModel.DoesNotExist:
            json_data = json.dumps({"message":"given course id not there"})
        return HttpResponse(json_data,content_type="application/json")

