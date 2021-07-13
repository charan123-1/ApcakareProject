from django.db import models

# Create your models here.
class excel(models.Model):
    num = models.CharField(default=0, max_length=200)
    userid  =  models.CharField(max_length=30, default='charan')
    n1 = models.CharField(default=0,max_length=200)
    n2 = models.CharField(default=0,max_length=200)
    n3 = models.CharField(default=0,max_length=200)
    n4 = models.CharField(default=0,max_length=200)
    n5 = models.CharField(default=0,max_length=200)
    n6 = models.CharField(default=0,max_length=200)
    n7 = models.CharField(default=0,max_length=200)
    n8 = models.CharField(default=0,max_length=200)
    n9 = models.CharField(default=0,max_length=200)
    n10 = models.CharField(default=0,max_length=200)
    n11 = models.CharField(default=0,max_length=200)
    n12 = models.CharField(default=0,max_length=200)
    n13 = models.CharField(default=0,max_length=200)

    class Meta:
        db_table = 'excel'