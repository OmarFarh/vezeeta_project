from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.


class Profile(models.Model):

    Gender = [
        ('M','Male'),
        ('F','Female'),
    ]

    D_in = [
        ('مخ و اعصاب' , 'مخ و اعصاب'),
        ('نساء وتوليد' , 'نسا وتوليد'),
        ('أسنان' , 'أسنان'),
        ( 'اطفال' , 'اطفال'),
    ]

    user = models.OneToOneField(User , on_delete = models.CASCADE)
    name = models.CharField(max_length = 50 , null=True , blank= True , default='NA')
    subtitle = models.CharField(max_length = 50 , null=True , blank= True)
    Specialist_doctor = models.CharField(max_length = 50 , null=True , blank= True)
    address = models.CharField(max_length = 100 , null=True , blank= True)
    who_i = models.TextField(null=True , blank= True)
    price = models.IntegerField(null=True , blank= True)
    Waiting_time = models.IntegerField(null=True , blank= True)
    working_hours  = models.IntegerField(null=True , blank= True)
    number_phone = models.CharField(max_length = 100 , null=True , blank= True)
    image = models.ImageField(upload_to= 'profile/%y/%m/%d' , null=True , blank= True)
    join = models.DateTimeField(auto_now_add = True , null = True , blank = True)
    gender = models.CharField(max_length = 50 , choices = Gender , null = True , blank = True)
    doctor_in = models.CharField(max_length = 50 , null = True , blank = True , choices= D_in)
    slug = models.SlugField(null = True , blank = True)

    def __str__(self) -> str:
        return self.name
    
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile , self).save(*args , **kwargs)

def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile , sender= User)


class patient(models.Model):

    doctor = models.ForeignKey( User , on_delete= models.CASCADE)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    phone1 = models.CharField(max_length = 11)
    phone2 = models.CharField(max_length = 11 , null = True , blank = True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    

class Create_Post(models.Model):

    user = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length = 100 , verbose_name = 'العنوان')
    Introduction = models.TextField(verbose_name = 'المقدمة')
    subject = models.TextField(verbose_name = 'الموضوع')
    time = models.DateTimeField(auto_now = True , null = True , blank = True)
    image = models.ImageField(upload_to='Post/%y/%m/%d' , verbose_name = 'الصورة')

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(Create_Post , on_delete = models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    time = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name


class Favorite(models.Model):

    Post = models.ForeignKey(Create_Post , on_delete = models.CASCADE)
    user = models.ForeignKey(User , on_delete = models.CASCADE)

    # def __str__(self) -> str:
    #     return self.user