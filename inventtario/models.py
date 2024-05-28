from django.db import models
from django.contrib.auth.models import User

class inventtario(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Activo(models.Model):
    CATEGORY_CHOICES = [
        ('APARTMENT', 'Apartment'),
        ('HOUSE', 'House'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='activos/')

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    cover_image = models.ImageField(upload_to='book_covers/')
    publication_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    shipped_date = models.DateTimeField(null=True, blank=True)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.book.title}"
