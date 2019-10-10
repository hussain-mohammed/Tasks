from django.db import models

# Create your models here.
class Books(models.Model):
    bookname = models.CharField(max_length=50,primary_key=True)
    author = models.CharField(max_length=50)
    publisheddate = models.DateField()
    Noofbooks = models.IntegerField()
    rackno = models.IntegerField()

    def __str__(self):
        return self.bookname