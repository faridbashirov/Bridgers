from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Services(AbstractBaseModel):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='services')
    small_description = models.TextField(null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

    
class Contact(AbstractBaseModel):

    LOCATION_CHOICES = (
        ('USA', 'USA'),
        ('CANADA', 'CANADA'),
        ('OTHER', 'OTHER'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='USA')
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class Blog(AbstractBaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    small_description = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextUploadingField()
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)

    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Career(AbstractBaseModel):
    resume = models.FileField(upload_to='resume', blank=True, null=True)

    class Meta:
        verbose_name = 'Career'
        verbose_name_plural = 'Careers'

    def __str__(self):
        return "%s"%self.resume


class RequestQuote(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    services = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Request Quote'
        verbose_name_plural = 'Request Quotes'

    def __str__(self):
        return self.name
    
class Subscriber(AbstractBaseModel):
    email=models.EmailField(max_length=55 ,unique=True)
    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
    def __str__(self):
        return self.email