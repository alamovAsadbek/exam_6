from django.db import models


class UserModel(models.Model):
    full_name = models.CharField(max_length=100)
    linkedin_url = models.URLField(max_length=200)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='team_avatars/')
    password = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
