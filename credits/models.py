from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, default=False)
    current_credits = models.IntegerField()
    mail_id = models.EmailField(max_length=254,default=False)
    Phone_num = models.IntegerField()

    
    def __str__(self):
        return self.name + str(self.current_credits)

class Record(models.Model):
    Name_Of_Sender = models.CharField(max_length=50)
    Name_Of_Receiver = models.CharField(max_length=50)
    Transfer_Amount = models.IntegerField()
    Sender_Updated_Balance = models.IntegerField()
    Receiver_Updated_Balance = models.IntegerField()