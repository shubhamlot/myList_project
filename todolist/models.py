from django.db import models
from datetime import datetime
from django.utils import timezone

class User(models.Model):
	UserId = models.AutoField(primary_key=True)
	Username = models.CharField(max_length=20)
	RefId = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.RefId

class Task(models.Model):
	Owner = models.ForeignKey(User, on_delete=models.CASCADE)
	TaskName = models.CharField(max_length=10)
	Discription = models.TextField(default="");
	Date = models.DateTimeField(default=datetime.now())

