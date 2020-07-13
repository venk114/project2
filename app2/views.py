from django.shortcuts import render
from project2.settings import covid_19_file
import json

def showIndex(request):
    dict_data = json.loads(open(covid_19_file).read())
    states = [x for x in dict_data]
    states.pop(0)
    return render(request,"index.html",{"data":states})


def open_state(request):
    sname = request.GET.get("state_name")
    
    dict_data = json.loads(open(covid_19_file).read())
    return render(request,"state.html",{"sname":sname,"data":dict_data[sname]})

