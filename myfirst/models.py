from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CumpursyField(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    update_by = models.CharField(max_length=100,null=True,blank=True)
    update_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    is_void = models.BooleanField(default=False,null=True,blank=True)
    void_remarks = models.CharField(null=True, max_length=100,blank=True)

    class Meta:
        abstract=True


class resume(CumpursyField):
    name = models.CharField(max_length=100,blank=True)
    dob= models.DateField(auto_now=False,auto_now_add=False,blank=True)
    gender=models.CharField(max_length=100,blank=True)
    pin=models.PositiveIntegerField(blank=True)
    mobile=models.PositiveIntegerField(blank=True)
    email=models.EmailField(blank=True)
    job_city=models.CharField(max_length=100,blank=True)
    profile_pic= models.ImageField(upload_to='profileimg',blank=True)
    school=models.CharField(max_length=100,blank=True)
    university=models.CharField(max_length=100,blank=True)
    degree=models.CharField(max_length=100,blank=True)
    skill=models.TextField(max_length=100,blank=True)
    about_you=models.TextField(max_length=100,blank=True)
    experience=models.TextField(max_length=100,blank=True)
    hobbies=models.TextField(max_length=100,blank=True)
