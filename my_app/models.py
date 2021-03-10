from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique='category')
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='projects/%Y/%m/%d', blank=True)
    url = models.URLField(blank=True)
    start_date = models.DateField(default=timezone.now)
    finish_date = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('orbicx:project_detail', args=[self.category.slug, self.slug])


class Image(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='staff/%Y/%m/%d', blank=True)
    role = models.CharField(max_length=100, db_index=True)
    introduction = models.TextField(blank=True)

    def __str__(self):
        return self.name
