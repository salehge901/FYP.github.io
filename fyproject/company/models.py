from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_discription = models.CharField(max_length=800)
    pos_tdate = models.DateTimeField(auto_now_add=True, blank=True)
    job_status =models.BooleanField(default=True)
    
    def __str__(self):
        return "%s %s" % (self.job_title, self.user)


class QuestionBank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=800)
    pos_tdate = models.DateTimeField(auto_now_add=True, blank=True)
    question_status =models.BooleanField(default=True)
    
    def __str__(self):
        return "%s %s %s" % (self.job_title, self.user, self.question)