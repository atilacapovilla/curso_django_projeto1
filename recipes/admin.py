from django.contrib import admin
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_published', 'category')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)

