from django.db import models

class News(models.Model):
    title = models.CharField(max_length=90,blank=False,null=False)
    description =  models.TextField(max_length=4048,blank=False,null=False)
    image  =  models.ImageField(upload_to='uploads/', )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return  self.title

class Category(models.Model):
    title = models.CharField(max_length=30,blank=False,null=False)
    def __str__(self):
        return self.title