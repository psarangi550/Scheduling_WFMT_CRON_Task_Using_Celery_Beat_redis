from django.db import models

# Create your models here.
class Test_Email_Schedule(models.Model):
    hour=models.IntegerField()
    minute=models.IntegerField()
    
    def __str__(self):
        return "{}.{}".format(self.hour, self.minute)
    