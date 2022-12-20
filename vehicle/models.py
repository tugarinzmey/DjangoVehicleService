from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class Mechanic(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    skill = models.CharField(max_length=500,null=True)
    salary=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Request(models.Model):

    vehicle_no = models.CharField(max_length=6,null=False)
    vehicle_name = models.CharField(max_length=40,null=False)

    problem_description = models.CharField(max_length=1000,null=False)
    date=models.DateField(auto_now=True)
    cost=models.PositiveIntegerField(null=True)

    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)

    stat=(('Обрабатывается','Обрабатывается'),('Подтверждена','Подтверждена'),('В ремонте','В ремонте'),('Ремонт завершен','Ремонт завершен'),('Готово!','Готово!'))
    status=models.CharField(max_length=50,choices=stat,default='Обрабатывается',null=True)

    def __str__(self):
        return self.problem_description

class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40)
    message=models.CharField(max_length=500)
