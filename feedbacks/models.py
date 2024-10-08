from django.db import models


class FeedbackModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey('UserModel', on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    see = models.IntegerField(default=0)

    choices = (
        ('offer', 'Offer'),
        ('problem', 'Problem')
    )
    feedback_type = models.CharField(max_length=20, choices=choices)
