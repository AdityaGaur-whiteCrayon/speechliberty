from django.db import models

class Regadmin(models.Model):
	emailid = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	createdate=models.DateTimeField()
	def __str__(self):
		return "Email id is "+self.emailid + " Password "+self.password +" Date is "+ str(self.createdate)

Category_CHOICES = (
    ('Gaming','Gaming'),
    ('News','News'),
    ('Terrorisam','Terrorisam'),
    ('Country','Country'),
    ('Global-Issues','Global-Issues'),
    ('Social-Media','Social-Media'),
)

class BlogMaster(models.Model):
    Topic = models.CharField(max_length=50, unique=True)
    Category = models.CharField(max_length=50,choices=Category_CHOICES, default='Social-Media' )
    Intro = models.CharField(max_length=100, )
    Description = models.CharField(max_length=800,)
    Varified = models.BooleanField(default=False)
    createdate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self
              