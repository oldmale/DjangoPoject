from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
