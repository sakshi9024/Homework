from django.db import models

class Student():
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.TextField()
    phone_no = models.IntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to="media",null=True,blank=True)
