import json
from django.views import View
from django.http import JsonResponse
from .models import User

class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User(
                user_id     = data['user_id'],          # user_name 으로 이름 변경해야 함, id는 숫자같은 느낌이 남
                email       = data['email'],
                password    = data['password'],
            )

            # if User.objects.filter(user_id=data['user_id']).exists() == True: #이미 == 전까지 트루임, 굳이 없어도 됨
            if User.objects.filter(user_id = data['user_id']).exists() :
                return JsonResponse({"message" : "이미 존재하는 아이디입니다."}, status = 401)

            else:
                # User.objects.create(user_id = data['user_id'], email = data['email'], password = data['password'])
                user.save()
                return JsonResponse({"message" : "회원으로 가입되셨습니다."}, status = 200)
        except KeyError:
            return JsonResponse({'message' : "INVALID ERROR"}, status = 400)

    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        if User.objects.filter(user_id = data['user_id'], password = data['password']).exists() : #user_id, password and 처리가 된다고 합니다.
            return JsonResponse({"message": "로그인에 성공하셨습니다."}, status = 200)
        else:
            return JsonResponse({"message" : "아이디나 비밀번호가 일치하지 않습니다."}, status = 401)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, status = 200)