from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cname = models.CharField(max_length=100)
    cage = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.timestamp}"
