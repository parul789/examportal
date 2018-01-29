from django.db import models
from django.contrib.auth.models import AbstractUser

USERTYPE = (('Student', 'Student'), ('Admin', 'Admin'))


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    updated_by = models.CharField(max_length=20, null=True, blank=True)


class User(AbstractUser):
    user_type = models.CharField(max_length=20, choices=USERTYPE)

    class Meta(AbstractUser.Meta):
        ordering = ['id']

    def __str__(self):
        return "{}{}".format(self.first_name if self.first_name else "Guest", self.id)
