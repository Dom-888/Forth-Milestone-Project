from django.db import models


class Category(models.Model):

    class Meta:
	    verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.display_name
    

# Products sold on the site
class Game(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# Items included in the game's box, such cards and dice
class Included(models.Model):

    class Meta:
	    verbose_name_plural = 'Included'

    game = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE)
    item = models.CharField(max_length=254)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item


# Rating assigned by registered users to products. It is commented out as the user model does not yet exist
'''
class Rating(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE) 
    grade = models.tinyint() # the grade expressed with a number from 1 to 5

    def __str__(self):
        return self.grade # Probably this is not going to work as grade is not a string
'''