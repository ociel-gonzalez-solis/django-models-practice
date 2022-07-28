from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "rating")}
    list_filter = ("author", "rating")
    list_display = ("title", "author", "rating", "isBestSelling")


admin.site.register(Book, BookAdmin)
