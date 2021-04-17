from django.db import models
from django.contrib.auth.models import User
from memberships.models import Plan


class PostCategory(models.Model):
    post_category_name = models.CharField(max_length=200, db_index=True)
    post_category_image = models.ImageField(upload_to='posts/category', default='posts/category/default.jpg')

    def __str__(self):
        return self.post_category_name

class PostOwner(models.Model):
    post_owner_name = models.CharField(max_length=200, db_index=True)
    post_owner_meta = models.CharField(max_length=254)
    post_owner_image = models.ImageField(upload_to='posts/owner', default='posts/owner/default.jpg')

    def __str__(self):
        return self.post_owner_name


STATUS = (
    (0,"Vázlat"),
    (1,"Publikálva")
)

class Post(models.Model):
    post_title = models.CharField(max_length=200, unique=True)

    post_description = models.TextField()
    post_description_1 = models.TextField()
    post_description_2 = models.TextField()
    post_description_3 = models.TextField()

    post_unique_slug = models.CharField(max_length=200, null=True, blank=True)

    post_text_1 = models.CharField(max_length=200, null=True, blank=True)
    post_text_2 = models.CharField(max_length=200, null=True, blank=True)
    post_text_3 = models.CharField(max_length=200, null=True, blank=True)
    post_video = models.CharField(max_length=200, null=True, blank=True)
    post_image = models.ImageField(upload_to='posts', default='posts/default.jpg')

    post_featured = models.BooleanField(default=True)
    post_status = models.IntegerField(choices=STATUS, default=0)

    post_category = models.ForeignKey(PostCategory, on_delete= models.SET_NULL,related_name='categories_posts', null=True, blank=True)
    post_owner = models.ForeignKey(PostOwner, on_delete=models.SET_NULL,related_name='owners_posts', null=True, blank=True)

    post_is_paid = models.BooleanField(default=False) #fizetős igen/nem

    post_plan = models.ManyToManyField(Plan, related_name='plans')

    post_updated_at = models.DateTimeField(auto_now= True)
    post_created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-post_created_at']

    def __str__(self):
        return self.post_title