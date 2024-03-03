from django.db import models

class ConvertedFile(models.Model):
    image = models.ImageField(upload_to='uploaded_imgs/')
    pdf = models.FileField(upload_to='converted_pdfs/', null=True, blank=True)
