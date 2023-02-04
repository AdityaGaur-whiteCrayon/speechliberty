from django.db import models
from BlogAdmin.models import BlogMaster

'''class RegisterMaster(models.Model):
    FullName = models.CharField(max_length=50,default='')
    Emailid = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    Createdate=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Email id is "+self.emailid + " Password "+self.password + " Mobile no is "+self.mobile + " fullname is "+ self.fullname + " Date is "+ str(self.createdate)
'''

class CommentMaster(models.Model):
    Blogid=models.ForeignKey(BlogMaster,on_delete=models.CASCADE)
    Emailid = models.EmailField(max_length=50)
    Comments = models.CharField(max_length=500,)
    Createdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Blogid id is "+ str(self.Blogid)+ " Email "+self.Emailid + "Comments is "+self.Comments + " Date is "+ str(self.Createdate)
    


class ContactMaster(models.Model):
    FullName = models.CharField(max_length=50,default='')
    Emailid = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=80,)
    Comments = models.CharField(max_length=500,)
    Createdate=models.DateTimeField(auto_now_add=True)
 