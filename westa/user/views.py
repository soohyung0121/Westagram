import json
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(user_id = data['user_id']).exists() :
                return JsonResponse({"message" : "USER_ALREADY_EXIST"}, status = 401)
            User(
                user_id=data['user_id'],  # user_name 으로 이름 변경해야 함, id는 숫자같은 느낌이 남
                email=data['email'],
                password=data['password'],
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
                if data['password'] == User.objects.get(user_id = data['user_id']).password:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, status = 200)