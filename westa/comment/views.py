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
        comment_context = Comment.objects.filter(comment_user=data['comment_user']).values('comment_text')
        return JsonResponse({data['comment_user']: list(comment_context)}, status=200)