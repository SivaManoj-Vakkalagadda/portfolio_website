from django.db import models

class Profile(models.Model):
    image = models.ImageField(upload_to='profiles/')  # requires Pillow
    name = models.CharField(max_length=100)
    description = models.TextField(help_text="Short description or tagline")
    extra_info = models.TextField(blank=True, null=True, help_text="Additional paragraphs")

    def __str__(self):
        return self.name


class CodingProfile(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='coding_profiles/')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(max_length=250)
    url = models.URLField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Contact Information"