from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_discription = models.CharField(max_length=800)
    pos_tdate = models.DateTimeField(auto_now_add=True, blank=True)
    job_status =models.BooleanField(default=True)
    
    def __str__(self):
        return "%s %s" % (self.job_title, self.user)


class QuestionBank(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=800)
    #time = models.TimeField((""), auto_now=False, auto_now_add=False)
    time = models.IntegerField()
    #time = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    pos_tdate = models.DateTimeField(auto_now_add=True, blank=True)
    question_status =models.BooleanField(default=True)
    
    def __str__(self):
        return "%s %s %s" % (self.user,"_"+self.job.job_title,  "_"+self.question)


class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    company_user_id = models.IntegerField()
    applidejob_id = models.IntegerField()
    schduele_time = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    apply_date = models.DateTimeField(auto_now_add=True, blank=True)
    interview_status =models.BooleanField(default=False)
    confirm_status =models.BooleanField(default=False)
    video_link = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    
    def __str__(self):
        return "%s %s %s %s" % (self.user,"_"+self.job.job_title,"_",self.job.user )