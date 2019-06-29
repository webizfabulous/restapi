from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Api(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    