from django.db import models

# Create your models here.
class Classes(models.Model):
    classno = models.CharField(max_length = 15, blank = False, primary_key = True)
    subcode = models.CharField(max_length = 7, blank = False)

    def __str__(self):
        return self.classno

class Subject(models.Model):
    subcode = models.CharField(max_length = 7, blank = False, primary_key = True)
    subname = models.CharField(max_length = 50, blank = False)
    classno = models.ForeignKey(Classes, on_delete = models.CASCADE)

    def __str__(self):
        return str((self.subcode,self.subname))

class Notes(models.Model):
    classno = models.ForeignKey(Classes, blank = False, on_delete = models.CASCADE)
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)

class Videos(models.Model):
    classno = models.ForeignKey(Classes, blank = False, on_delete = models.CASCADE)
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)

class Books(models.Model):
    classno = models.ForeignKey(Classes, blank = False, on_delete = models.CASCADE)
    subcode = models.ForeignKey(Subject, blank = False, on_delete = models.CASCADE)
    skey = models.CharField(max_length = 100)     #SearchKey
    title = models.CharField(max_length = 100, blank = False)
    author = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000, blank = False)

    def __str__(self):
        return (self.title)
