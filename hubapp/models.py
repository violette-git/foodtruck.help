from django.db import models
from user_app.models import User


                                    #Category
# ---------------------------------------------------------------------------------

CATEGORIES = {
    ('burgers','Burgers'),
    ('sides','Sides'),
    ('appetizers','Appetizers'),
    ('breakfast','Breakfast'),
    ('lunch','Lunch'),
    ('dinner','Dinner'),
    ('snacks','Snacks'),
    ('drinks','Drinks'),
    ('alcoholic','Alcoholic'),
    ('beverages','Beverages'),
    ('desserts','Desserts'),
    ('sandwiches','Sandwiches'),
    ('soups','Soups'),
    ('stews','Stews'),
    ('salads','Salads'),
    ('pastas','Pastas'),
    ('rice','Rice'),
    ('chicken','Chicken'),
    ('beef','Beef'),
    ('pork','Pork'),
    ('lamb','Lamb'),
    ('fish','Fish'),
    ('seafood','Seafood'),
    ('vegetarian','Vegetarian'),
    ('vegan','Vegan'),
    ('gluten-free','Gluten-free'),
    ('low-carb','Low-Carb'),
    ('keto-friendly','Keto-Friendly'),
    ('paleo','Paleo'),
    ('mediterranean','Mediterranean'),
    ('indian','Indian'),
    ('chinese','Chinese'),
    ('japanese','Japanese'),
    ('thai','Thai'),
    ('vietnamese','Vietnamese'),
    ('korean','Korean'),
    ('mexican','Mexican'),
    ('american','American'),
    ('hawaiian','Hawaiian'),
    ('sandwiches','Sandwiches'),
    ('soup','Soup'),
    ('salad','Salad'),
    ('chicken','Chicken'),
    ('steak','Steak'),
    ('seafood','Seafood'),
    ('pasta','Pasta'),
    ('rice','Rice'),
    ('beans','Beans'),
    ('vegetables','Vegetables'),
    ('fruit','Fruit'),
    ('juices','Juices'),
    ('smoothies','Smoothies'),
    ('coffee','Coffee'),
    ('tea','Tea'),
    ('soda','Soda'),
    ('beer','Beer'),
    ('wine','Wine'),
    ('liquor','Liquor'),
    ('fast food','Fast Food'),
    ('casual dining','Casual Dining'),
    ('fine dining','Fine Dining'),
    ('ethnic','Ethnic'),
    ('comfort','Comfort'),
    ('barbecue','Barbecue'),
    ('junk food','Junk Food'),
    ('healthy food','Healthy Food'),
    ('vegan','Vegan'),
    ('vegetarian','Vegetarian'),
    ('gluten-free','Gluten-Free'),
    ('diabetic-friendly','Diabetic-Friendly'),
    ('keto-friendly','Keto-Friendly'),
    ('low-fat','Low-Fat'),
    ('low-carb','Low-Carb'),
    ('paleo-friendly','Paleo-Friendly'),
    ('dairy-free','Dairy-Free'),
}

class Category(models.Model):

    name = models.CharField(max_length=50, choices=CATEGORIES, default='')

    def __str__(self):
        return self.name


                                    # MenuItem
# ---------------------------------------------------------------------------------

class MenuItem(models.Model):

    # menu = models.ManyToManyField('Menu', related_name='item' )

    name = models.CharField(max_length=65, null=False)

    price = models.FloatField(default=0.00, null=False)

    description = models.CharField(max_length=350, null=False)

    image = models.ImageField(null=True)
    
    quantity_left = models.IntegerField(default=0, null=True)

    allergy_info = models.CharField(max_length=350, null=True)
    
    def __str__(self):

        return f'{self.name.capitalize()}'

    def __self__(self):

        return f'{self.name.capitalize()}'

# ---------------------------------------------------------------------------------

class Menu(models.Model):

    name = models.CharField(max_length=65, null=False)

    items = models.ManyToManyField(MenuItem, related_name="item")


    def __str__(self):

        return f'{self.name}'

    def __self__(self):

        return f'{self.name}'


# ---------------------------------------------------------------------------------


                                    # FoodTruck
# ---------------------------------------------------------------------------------
class FoodTruck(models.Model):

    name = models.CharField(max_length=65)    

    number = models.IntegerField()

    website = models.URLField()

    logo = models.ImageField()

    categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="category", null=False)

    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, related_name="category", null=False)

    def __str__(self):

        return f'{self.name.capitalize()}'

    def __self__(self):

        return f'{self.name.capitalize()}'