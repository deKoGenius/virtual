from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self, name, age, gender, password=None):
        if not name:
            raise ValueError('there is no user_name')

        user = self.model(
            name=name,
            age=age,
            gender=gender
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, age, gender, password):
        user = self.create_user(
            name=name,
            age=age,
            gender=gender,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    gender = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManger()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['age', 'gender']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin