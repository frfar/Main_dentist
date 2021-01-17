from django.db import models
from django.utils.html import format_html
from account.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# My Manager.
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', default = None, null= True, blank=True, on_delete=models.SET_NULL, related_name = 'children')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100 , unique=True)
    status = models.BooleanField(default= True, verbose_name="Do you want this item be visable?")
    position = models.IntegerField()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name="articles")
    description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    objects = ArticleManager()

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = 'image'




