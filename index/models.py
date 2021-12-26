from django.core.checks import messages
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.models import User
# Create your models here.

# class signup(models.Model):
#     name = models.CharField(max_length=20,default='')
#     user_name = models.CharField(max_length=50,primary_key=True)
#     password = models.CharField(max_length=20)
#     email = models.EmailField()
#     phnumber = models.IntegerField(max_length=10)

#     def __str__(self) -> str:
#         return self.user_name
class policeDetails(models.Model):
    sname=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    psemail=models.EmailField()
    psnumber=models.IntegerField()
    def __str__(self):
        return self.sname

class complaint(models.Model):
    cid = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=DO_NOTHING)
    victims_fname = models.CharField(max_length=20)
    victims_lname = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=500)
    subject = models.TextField(max_length=50)
    idproof_number = models.CharField(max_length=30)
    idprooof = models.FileField(upload_to='data/id/')
    vedio = models.FileField(upload_to='data/vids/')
    image = models.FileField(upload_to='data/imgs/')
    message = models.TextField(max_length=50)
    gender=models.CharField(max_length=50,default='NA',null=True)

    def __str__(self) -> str:
        return str(self.cid)+') '+self.victims_fname+' '+self.victims_lname+' <- '+str(self.user_name)
        
class contactusmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mssg=models.TextField()
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name+":"+self.subject



