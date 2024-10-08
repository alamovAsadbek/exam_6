from django.db import models


class FeedbackModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey('UserModel', on_delete=models.CASCADE, null=True)
