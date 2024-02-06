from django.db import models

# Create your models here.
class product(models.Model):
    product_icon=models.CharField(max_length=50)    
    product_title=models.CharField(max_length=50)    
    product_des=models.TextField()
    product_image=models.FileField(upload_to="products_img/", max_length=250, null=True, default=None)
    upload_product=models.FileField(upload_to="products_model/",null=False, default=None)
    product_link=models.CharField(max_length=1000, default=None)
