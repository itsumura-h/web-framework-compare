from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField('email', max_length=255, db_index=True)
    password = models.CharField('password', max_length=255)

    def __str__(self):
        return self.email
