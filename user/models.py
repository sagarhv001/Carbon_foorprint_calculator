from django.db import models

# Create your models here
class User_Details(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics',default='default.jpg')
    goal = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class User_History(models.Model):
    name = models.ForeignKey(User_Details, on_delete=models.CASCADE)
    date = models.DateField()
    daily_emsn = models.IntegerField()
    food_emsn = models.IntegerField()
    travel_emsn= models.IntegerField()
    energy_emission = models.IntegerField()
    total_emsn = models.IntegerField()

    def __str__ (self):
        return self.id_no
    
class goal(models.Model):
    name = models.ForeignKey(User_Details, on_delete=models.CASCADE)
    gl_daily_emsn = models.IntegerField()
    gl_travel_emsn = models.IntegerField()
    gl_energy_emsn = models.IntegerField()
    gl_food_emsn = models.IntegerField()

    def __str__ (self):
        return self.id_no

class Average(models.Model):
    daily_emsn = models.IntegerField()
    travel_emsn = models.IntegerField()
    energy_emsn = models.IntegerField()
    food_emsn = models.IntegerField()
    total_emsn = models.IntegerField()
    
    def __str__ (self):
        return self.daily_emsn

