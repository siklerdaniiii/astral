from django.db import models
from django.contrib.auth.models import User



class PlaceCategory(models.Model):
    place_category_name = models.CharField(max_length=200, db_index=True)
    lace_category_image = models.ImageField(upload_to='places/category', default='places/category/default.jpg')

    def __str__(self):
        return self.place_category_name




class PlaceType(models.Model):
    place_type_name = models.CharField(max_length=200, db_index=True)
    place_type_image = models.ImageField(upload_to='places/type', default='places/type/default.jpg')

    def __str__(self):
        return self.place_type_name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Place(models.Model):
    place_title = models.CharField(max_length=200, unique=True)

    place_description = models.TextField()

    place_audience = models.CharField(max_length=200, null=True, blank=True)
    place_address = models.CharField(max_length=200, null=True, blank=True)
    place_schedule = models.CharField(max_length=200, null=True, blank=True)
    place_phone  = models.CharField(max_length=200, null=True, blank=True)
    place_website = models.CharField(max_length=200, null=True, blank=True)

    place_text_1 = models.CharField(max_length=200, null=True, blank=True)
    place_text_2 = models.CharField(max_length=200, null=True, blank=True)
    place_text_3 = models.CharField(max_length=200, null=True, blank=True)

    place_video = models.CharField(max_length=200, null=True, blank=True)
    place_image = models.ImageField(upload_to='places', default='places/default.jpg')

    place_featured = models.BooleanField(default=True)
    place_status = models.IntegerField(choices=STATUS, default=0)

    place_author = models.ForeignKey(User, on_delete= models.SET_NULL,related_name='authors_places', null=True, blank=True)
    place_category = models.ForeignKey(PlaceCategory, on_delete= models.SET_NULL,related_name='categories_places', null=True, blank=True)
    place_type = models.ForeignKey(PlaceType, on_delete=models.SET_NULL,related_name='types_places', null=True, blank=True)

    place_updated_at = models.DateTimeField(auto_now= True)
    place_created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-place_created_at']

    def __str__(self):
        return self.place_title