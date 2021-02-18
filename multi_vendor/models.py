from django.db import models

# Create your models here.






# 1st Products , Orders , Reviews , Comments , users ,Save , Add to cart



# - vendors
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