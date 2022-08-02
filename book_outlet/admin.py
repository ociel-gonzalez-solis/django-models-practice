from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "rating")}
    list_filter = ("author", "rating")
    list_display = ("title", "author", "rating", "isBestSelling")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
