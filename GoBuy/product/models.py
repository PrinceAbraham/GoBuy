from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=42)

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
         return ('product_detail', (),
              {
                 'slug': self.slug,
              })
    def save(self, *args, **kwargs):
         if not self.slug:
             self.slug = slugify(self.name)
         super(Product, self).save(*args, **kwargs)

    class Meta:
            ordering = ['created_on']
            def __unicode__(self):
                return self.name
