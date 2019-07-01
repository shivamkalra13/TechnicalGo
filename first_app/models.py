from django.db import models

# Create your models here.
class Subject(models.Model):
    class_names = ['1-8','9','10','11','12','Engineering','CA','B.Sc']
    CLASS_CHOICES = [               #List of tuple to provide specific choices in 'classno' field.
        ('1-8','1-8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('Engineering','Engineering'),
        ('CA','CA'),
        ('B.Sc','B.sc')
    ]
    subcode = models.CharField(max_length = 7, blank = False, primary_key = True)
    subname = models.CharField(max_length = 50, blank = False)
    classno = models.CharField(
    max_length = 15,
    choices = CLASS_CHOICES,
    default = '12')

    def __str__(self):
        return str((self.subcode,self.subname))

class Notes(models.Model):
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)

class Videos(models.Model):
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)

class Books(models.Model):
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    author = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)
