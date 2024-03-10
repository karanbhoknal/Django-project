from django.db import models

# Create your models here.
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    
    
class RegisterModel(models.Model):
 
    # fields of the model
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    contactnumber = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    confirmpassword = models.CharField(max_length = 200)
    description = models.CharField(null= True,max_length = 200)
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.firstname #, self.lastname, self.email, self.contactnumber, self.password, self.confirmpassword



    

class BasicModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    

