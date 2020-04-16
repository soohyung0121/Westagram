import json
import bcrypt
import jwt

from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(user_id = data['user_id']).exists() :
                return JsonResponse({"message" : "USER_ALREADY_EXIST"}, status = 401)
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            User(
                user_id     = data['user_id'],
                email       = data['email'],
                password    = hashed_password
            ).save()
            return HttpResponse(status = 200)
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)

    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(user_id = data['user_id']).exists() :
                if bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(user_id=data['user_id']).password.encode('utf-8')):
                    access_token = jwt.encode({'user_id' : User.objects.get(user_id = data['user_id']).id}, 'secret', algorithm = 'HS256')
                    return JsonResponse({"access-token" : access_token.decode('utf-8')}, status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, status = 200)