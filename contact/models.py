from django.db import models



STATUS = (
    (0,"Új"),
    (1,"Folyamatban"),
    (2,"Lezárva"),
)

class Contact(models.Model):
    contact_name = models.CharField(max_length=200, unique=True)
    contact_email = models.CharField(max_length=254)
    contact_message = models.TextField()

    contact_status = models.IntegerField(choices=STATUS, default=0)

    contact_updated_at = models.DateTimeField(auto_now= True)
    contact_created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-contact_created_at']

    def __str__(self):
        return self.contact_name