from ast import BinOp
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save
# Create your models here.

VERIFICATION_OPTIONS =(
    ('unverified', 'unverified'),
    ('verified', 'verified'),
)

TYPE_OPTIONS =(
    ('Client', 'Client'),
    ('Restaurant', 'Restaurant'),
)


def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name

def user_directory_path_banner(instance, filename):
    profile_picture_name = 'users/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name





class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50)
    
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default = 'users/default_user.jpg', upload_to=user_directory_path_profile)
    banner = models.ImageField(default = 'users/default_background.jpg', upload_to=user_directory_path_banner)
    veirifed = models.CharField(max_length=10, choices = VERIFICATION_OPTIONS, default ='unverified')
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    Bio = models.TextField(max_length=300, null=True, blank=True)
    Birthday =models.DateField(null=True, blank=True)
    Usertype = models.CharField(max_length=10, choices = TYPE_OPTIONS, default ='Client')
    
    def __str__(self):
        return self.user.username
    
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()
            
    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)