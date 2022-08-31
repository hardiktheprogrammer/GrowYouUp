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
    ("Graphic Designing","Graphic Designing"),
    ("Web development","Web development"),
    ("Marketing","Marketing"),
    ("SEO","SEO"),
    ("Tech solutions","Tech solutions"),
    ("Data Analysis","Data Analysis")

}

class Portfolio(models.Model):
    service_type = models.CharField(choices=services,max_length=100)
    project_name = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='Porfolio-Images',validators=[validate_image_file_extension])
    project_link = models.URLField(blank=True,null=True)
    project_desc = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} - {self.project_name}"

    class Meta:
        ordering = ['-time']

class Testimonial(models.Model):
    client_name  = models.CharField(max_length=50)
    client_message = models.TextField()
    testimonial_image = models.ImageField(upload_to='Testimonial-Images',validators=[validate_image_file_extension])
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

    class Meta:
        ordering = ['-published_at']



class Team(models.Model):
    photo=models.ImageField(upload_to='Team-Images',validators=[validate_image_file_extension])
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=150)
    joined_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name