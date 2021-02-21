from django.db import models
from multiselectfield import MultiSelectField

MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))

class CommunistParty(models.Model):
    name = models.CharField(max_length=80)
    acronym = models.CharField(max_length=20, null=True, blank=True)
    trend = MultiSelectField(choices=MY_CHOICES, default='hola')

    description = models.TextField()
    logo = models.ImageField(upload_to='') 
    url = models.CharField(max_length=80)

    foundation_date = models.DateField()
    ambit = models.CharField(max_length=80)

    def __str__(self):
        return self.name
