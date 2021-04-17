from django.db import models
from django.contrib.auth.models import User



class BlogCategory(models.Model):
    blog_category_name = models.CharField(max_length=200, db_index=True)
    blog_category_image = models.ImageField(upload_to='blog/category', default='blog/category/default.jpg')

    def __str__(self):
        return self.blog_category_name

class BlogOwner(models.Model):
    blog_owner_name = models.CharField(max_length=200, db_index=True)
    blog_owner_meta = models.CharField(max_length=254)
    blog_owner_image = models.ImageField(upload_to='blog/owner', default='blog/owner/default.jpg')

    def __str__(self):
        return self.blog_owner_name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    blog_title = models.CharField(max_length=200, unique=True)

    blog_description = models.TextField()

    blog_image = models.ImageField(upload_to='blog', default='blog/default.jpg')

    blog_featured = models.BooleanField(default=True)
    blog_status = models.IntegerField(choices=STATUS, default=0)

    blog_owner = models.ForeignKey(BlogOwner, on_delete=models.SET_NULL,related_name='owners_blogs', null=True, blank=True)

    blog_category = models.ForeignKey(BlogCategory, on_delete= models.SET_NULL,related_name='categories_blogs', null=True, blank=True)

    blog_updated_at = models.DateTimeField(auto_now= True)
    blog_created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-blog_created_at']

    def __str__(self):
        return self.blog_title