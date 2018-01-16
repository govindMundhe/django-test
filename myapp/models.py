from django.db import models
from django.utils import timezone
# Create your models here.
class Item (models.Model):
    item_name = models.CharField(max_length = 200)
    details = models.CharField(max_length = 100)
    price = models.IntegerField()
    

    def __str__(self):
        return 'Name: {} '.format (self.item_name)


class Orders (models.Model):
    item_name = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_date = models.DateField(default = timezone.now)
    added_time = models.TimeField(default = timezone.now)

@property
def total(self):
    return self.quantity * Item.price

    def __str__(self):
	    return '{} , ID: {} '.format (self.item_name,self.id)