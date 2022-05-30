# from django.contrib.auth.models import User
# from django.db import models
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio = models.TextField()
#     avatar = models.ImageField(null=True, blank=True, upload_to='profile_images')
#
#     def __str__(self):
#         return self.user.username
