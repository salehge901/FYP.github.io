from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Extend(models.Model):
    user_type = models.CharField(max_length= 15)
    company_name = models.CharField(max_length= 50)
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.user, self.user_type)
    
    
