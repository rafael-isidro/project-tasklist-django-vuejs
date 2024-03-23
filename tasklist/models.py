from django.db import models
from django.contrib.auth import get_user_model

class Tasklist(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)

class Meta:
    ordering = ['-id']
    def __str__(self) -> str:
        return self.title