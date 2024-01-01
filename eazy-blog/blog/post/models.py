from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User 

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length = 255 )
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('post_detail',  args=[str(self.category.slug), str(self.slug)])
    

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name    
    
    
    






