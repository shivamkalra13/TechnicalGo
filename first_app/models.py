from django.db import models

# Create your models here.
class Classes(models.Model):
    CLASS_CHOICES = [               #List of tuple to provide specific choices in 'classno' field.
        ('1-8','1-8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('engg','engg'),
        ('ca','ca'),
        ('bsc','bsc')
    ]
    classno = models.CharField(
    max_length = 15,
    choices = CLASS_CHOICES,
    default = '12')
    subcode = models.CharField(max_length = 7, blank = False)

    def __str__(self):
        return str(self.classno)+","+str(self.subcode)

class Subject(models.Model):
    subcode = models.CharField(max_length = 7, blank = False, primary_key = True)
    subname = models.CharField(max_length = 50, blank = False)
    classno = models.ForeignKey(Classes, blank = False, on_delete = models.CASCADE, default='12')

    def __str__(self):
        return str((self.subcode,self.subname))

class Notes(models.Model):
    classno = models.ForeignKey(Classes, blank = False, on_delete = models.CASCADE, default='12')
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)

class Videos(models.Model):
    classno = models.ForeignKey(Classes, blank = False, on_delete = models.CASCADE, default='12')
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)

class Books(models.Model):
    classno = models.ForeignKey(Classes, blank = False, on_delete = models.CASCADE, default='12')
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    author = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)
