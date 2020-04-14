from django.db import models

class Comment(models.Model):
    comment_user    = models.CharField(max_length=200)
    comment_text    = models.TextField()
    published_at    = models.DateTimeField(auto_now_add = True)
    created_at      = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'