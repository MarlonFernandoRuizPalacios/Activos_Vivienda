from django.contrib import admin
from .models import inventtario, Category, Author, Book, Customer, Order, OrderDetail, Activo

class InventtarioAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ActivoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'publication_date')
    search_fields = ('title', 'authors__first_name', 'authors__last_name')
    list_filter = ('categories', 'authors')
    filter_horizontal = ('categories', 'authors')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number')
    search_fields = ('user__username', 'address', 'phone_number')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'shipped_date', 'is_shipped')
    search_fields = ('customer__user__username',)
    list_filter = ('is_shipped', 'order_date', 'shipped_date')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'price')
    search_fields = ('order__customer__user__username', 'book__title')
    list_filter = ('order__order_date',)

admin.site.register(inventtario, InventtarioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Activo, ActivoAdmin)
