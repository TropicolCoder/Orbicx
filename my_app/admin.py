from django.contrib import admin
from .models import Category, Project, Image, Member


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'created', 'updated']
    list_filter = ['category', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'project', 'created']
    list_filter = ['project', 'created']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'image']
    list_filter = ['role']

