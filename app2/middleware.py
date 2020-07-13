import requests
import json
class Covid19Middleware:
     def __init__(self,get_response):
        self.get_response = get_response
        response = requests.get("https://api.covid19india.org/state_district_wise.json")
        print(response.status_code)
        dict_data = json.loads(response.text)
        json.dump(dict_data,open("app2/raw/covid.json","w"))
        print("data written to the file")

     def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        print("i am call")
        return response
