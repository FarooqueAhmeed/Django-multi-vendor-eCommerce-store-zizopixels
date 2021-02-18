from django.db import models

# Create your models here.






# 1st Products , Orders , Reviews , Comments , users ,Save , Add to cart



class Products(models.Model):
    category = (
        ('Sports', 'Sports'),
        ('Business', 'Business'),
        ('Computer', 'Computer'),
        ('Entertainment', 'Entertainment'),
        ('Games', 'Games'),
        ('Family', 'Family'),
        ('Travel', 'Travel'),
        ('Fashion', 'Fashion'),
        ('Politics', 'Politics'),
        ('Pets', 'Pets'),
    )
    category = models.CharField(max_length=13, blank=True,null=True, choices= category)
    title = models.CharField(max_length=100, null=True,blank=True)
    content = models.CharField(max_length=1000, null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog_image")
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.user,'-blog_title-',self.title, '-image-', self.image)


class Favorite(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.user,'-fav-', self.blog)


class Comments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=250, null=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment





# - Seller
   # - Name
   # - City
   # - Mob
   # - Address
   # - Gmail
   # - BIO
   # - Image
   # - DOB
   # - Male/Female

     # - Shop
        # - Name
        # - Logo
        # - date of creation
        # - BIO
        # - venders(R)
        # -




     # - Products
         # - Category
         # - Name
         # - Color
         # - Size
         # - Quantity
         # - Description
         # - Image
         # - Prize
         # - Date of added on shop
         # - Shop(R)
         # - Reviews(R)
         # - Comments (R)
         # - User (R)


     # - Orders
        # - Shop
        # - Name (Products r)
        # - User (R)
        # - Quantity
        # - color
        # - size
        # - Date


     # = Reviews
        # - User(R)
        # - Product (R)
        # - Shop(R)
        # - Stars
        # - Thoughts



     # - Comments
       # - Product(R)
       # - User (R)
       # - Comment

    #  - Social media links
       # - URLs




# - users
    # - username
    # - mail

     # - Details
         # - Name
         # - Phone
         # - Address
         # - city
         # - State
         # - Country
         # - Street
         # - PostalCode
         # - Room no
         # - Building

    # - Save
       # - Product (R)
    # - Add to cart
       # - Product (R)