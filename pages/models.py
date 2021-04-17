from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Vázlat"),
    (1,"Publikálva")
)

SLUG = (
    ("home_1","Kezdőlap #1"),
    ("home_2","Kezdőlap #2"),
    ("home_3","Kezdőlap #3"),
    ("home_4","Kezdőlap #4"),
    ("home_5","Kezdőlap #5"),
    ("about","Rólam"),
    ("gdpr","Adatkezelési nyilatkozat"),
    ("aszf","Általános szerődési feltételek"),

)

class Page(models.Model):
    page_title = models.CharField(max_length=200, unique=True)
    paget_description = models.TextField()
    page_image = models.ImageField(upload_to='pages', default='pages/default.jpg')
    page_unique_field = models.CharField(max_length=200, blank=True, null=True)
    page_status = models.IntegerField(choices=STATUS, default=0)
    page_slug = models.CharField(choices=SLUG, max_length=254, unique=True) #ide olyan egyedi azonosítok jönnek, hogy pl about, privacy, stb
    page_updated_at = models.DateTimeField(auto_now= True)
    page_created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-page_created_at']

    def __str__(self):
        return self.page_title