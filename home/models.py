from django.db import models
from django.core.validators import validate_image_file_extension

class Contact(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.time.year} - {self.time.month} - {self.time.day}"

    class Meta:
        ordering = ['-time']

services = {
    ("Graphic Des","Graphic Designing"),
    ("Web development","Web development"),
    ("Marketing","Marketing"),
    ("SEO","SEO"),
    ("Tech solutions","Tech solutions"),
    ("Data Analysis","Data Analysis")

}

class Portfolio(models.Model):
    service_type = models.CharField(choices=services,max_length=100)
    project_name = models.CharField(max_length=50)
    project_image = models.ImageField(validators=[validate_image_file_extension])
    project_desc = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} - {self.project_name}"

    class Meta:
        ordering = ['-time']