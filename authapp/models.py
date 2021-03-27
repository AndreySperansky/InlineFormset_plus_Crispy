from django.db import models
from django.contrib.auth.models import AbstractUser




class InfojobUser(AbstractUser):

    EMPLOYEE = 'EMPLOYEE'
    EMPLOYER = 'EMPLOYER'
    ROLE = [(EMPLOYEE, 'Employee'), (EMPLOYER, 'Employer')]

    username = models.CharField(max_length=150, verbose_name='пользователь', unique=True)
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар', blank=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=250, verbose_name='пароль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='cоздано')
    user_role = models.CharField(max_length=25, choices=ROLE, default=EMPLOYEE, verbose_name='роль')

    def __str__(self):
        return f"{self.username} {self.email} {self.user_role}"

