import json

from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import Comment

class CommentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Comment(
                comment_user    = data['comment_user'],
                comment_text    = data['comment_text'],
            ).save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({"message" : "INVALID ERROR"}, status = 400)


    def get(self, request):
        data = json.loads(request.body)
        fix_user_text = []
        comment_context = Comment.objects.values()

        for i in range(len(comment_context)):
            if comment_context[i]['comment_user'] == data['comment_user']:
                fix_user_text.append(comment_context[i]['comment_text'])

        return JsonResponse({data['comment_user'] : fix_user_text}, status = 200)