from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from logica import users
import json
from WEB.Logica import users


@csrf_exempt
# Create your views here.
def index(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['content']
    nick_name = body['nick_name']
    full_name = body['full_name']
    
    try:
        response = {
            "status": "success",
            "code": 200,
            "data": created
        }
    except Exception as e:
        response = {
            "status": "error",
            "code": 500,
            "data": str(e)
        }
    return JsonResponse(response)