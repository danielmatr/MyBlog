from django.db import models

from account.models import MyUser


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True) #pk=true - budet sozdavat otdelnoe pole id i sdekaet pervichnym klychom
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts') #cascade esli avtor udalen to vse ego posty udalyasta
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts') #cherez kategoriyu mojno vytawit vse posty
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

