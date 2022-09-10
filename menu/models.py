from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Description(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Descriptions'

    def __str__(self):
        if len(self.text) > 100:
            return f'{self.text[:100]}...'
        else:
            return self.text
