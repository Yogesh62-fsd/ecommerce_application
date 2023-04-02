from django.db import models


# Banner
class Banner(models.Model):
    img=models.CharField(max_length=100)
    alt_text=models.CharField(max_length=300)

#Category 
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='cat_imgs/')

    def __str__(self):
        return self.title    
    
#Brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='brand_imgs/')

    def __str__(self):
        return self.title 
# Color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    def __str__(self):
        return self.title 
# Size
class Size(models.Model):
    title=models.CharField(max_length=100)
    

    def __str__(self):
        return self.title
    
# Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='products_imgs/')
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    price=models.PositiveIntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title



# ProductAttribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    # image=models.ImageField(upload_to="product_imgs/",null=True)

    # class Meta:
    #     verbose_name_plural='7. ProductAttributes'

    def __str__(self):
        return self.product.title

    # def image_tag(self):
    #     return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

# class CartOrder(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     total_amt=models.FloatField()
#     paid_status=models.BooleanField(default=False)
#     order_dt=models.DateTimeField(auto_now_add=True)
#     order_status=models.CharField(choices=status_choice,default='process',max_length=150)