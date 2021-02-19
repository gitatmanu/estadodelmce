from django.db import models

class CommunistParty(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    logo = models.ImageField(upload_to='') 
    url = models.CharField(max_length=80)

    foundation_date = models.DateField(auto_now_add=True)
    ambit = models.CharField(max_length=80)

    def __str__(self):
        return self.name
