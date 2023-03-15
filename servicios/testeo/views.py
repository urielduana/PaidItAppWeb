from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from logica import users
import json
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
# Create your views here.
def index(request):
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    # content = body['content']
    # nick_name = body['nick_name']
    # full_name = body['full_name']
    nick_name = request.POST.get('nick_name')
    full_name = request.POST.get('full_name')

    try:
        user = users.create_user(nick_name=nick_name, full_name=full_name)
        # user.save()
        response = {
            "status": "success",
            "code": 200,
            "data": "User saved successfully"
        }
    except Exception as e:
        response = {
            "status": "error",
            "code": 400,
            "data": str(e)
        }
    return JsonResponse(response)
