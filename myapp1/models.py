from django.db import models

# Create your models here.
class Patient(models.Model):
    userid = models.CharField(max_length=20,primary_key=True)
    fullname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.userid

    class meta:
        verbose_name_plurel = "Patient"
        db_table = 'Patient'