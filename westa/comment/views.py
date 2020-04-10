import json

from django.views import View
from django.http import JsonResponse

from .models import Comment

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)

        Comment(
            comment_user         = data['comment_user'],
            comment_text         = data['comment_text'],
        ).save()

        return JsonResponse({"message" : "good"}, status = 200)

    def get(self, request):
        data = json.loads(request.body)

        fix_user_text = []
        comment_context = Comment.objects.values()

        for i in range(len(comment_context)):
            if comment_context[i]['comment_user'] == data['comment_user']:
                fix_user_text.append(comment_context[i]['comment_text'])

        return JsonResponse({'soo' : fix_user_text}, status = 200)