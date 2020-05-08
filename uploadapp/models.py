from django.db import models

# database and save the image
class Uploadfile(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name