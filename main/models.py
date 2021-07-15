from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=100)
    cat_pic=models.ImageField(upload_to='category')
    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    subcat_name=models.CharField(max_length=100)
    subcat_pic=models.ImageField(upload_to='sub_category')
    def __str__(self):
        return self.subcat_name



class Product1(models.Model):
    name = models.CharField(max_length=200)
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_id=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products')
    price = models.IntegerField()
    
    def __str__(self):
        return self.name


    def get_products_by_subcategory(subcat_id):
        if subcat_id:
            return Product1.objects.filter(subcategory=subcat_id)
        else:
            return Product1.objects.all()

class Cart(models.Model):
    cus_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product1, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.cus_id.first_name

    @property
    def get_total_cart(self):
        return self.quantity * self.product_id.price

STATE_CHOICES= (
    ('Andhra Pradesh','Andhra Pradesh'), 
    ('Arunachal Pradesh','Arunachal Pradesh'),   
    ('Assam','Assam'), 
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa') ,
    ( 'Gujarat','Gujarat'),
    ('Haryana','Haryana'), 
    ('Himachal Pradesh','Himachal Pradesh') ,
    ('Jharkhand','Jharkhand') ,
    ('Karnataka','Karnataka') ,
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'), 
    ('Maharashtra','Maharashtra') ,
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'), 
    ('Sikkim','Sikkim'),
    ('Telangana','Telangana'),
    ('Telangana','Telangana'),
    ('Uttar Pradesh' ,'Uttar Pradesh '),
    ('Uttarakhand ','Uttarakhand '),
    ('West Bengal','West Bengal')
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)+self.address


STATUS_CHOICES=(
   ('Accepted','Accepted'),
   ('Packed','Packed'),
   ('On The Way','On The Way'),
   ('Delivered','Delivered'),
   ('cancel','cancel'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    customer=models.ForeignKey(Customer,on_delete=CASCADE)
    product=models.ForeignKey(Product1,on_delete=CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    date_ordered=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,
    choices=STATUS_CHOICES,default='Pending')


    def __str__(self):
        return str(self.user)
    
    @staticmethod
    def get_order_by_customer(customer_id):
        return OrderPlaced.objects.filter(user=customer_id)
