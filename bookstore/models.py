from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    uploaded_by = models.CharField(max_length=100,null=True,blank=True)
    user = models.CharField(max_length=100,null=True,blank=True)
    pdf = models.FileField(upload_to='bookapp/pdfs')
    cover = models.ImageField(upload_to='bookapp/covers/',null=True,blank=True)
    


    def  __str__(self):
       return f'{self.title}  by  {self.auther}'

  
