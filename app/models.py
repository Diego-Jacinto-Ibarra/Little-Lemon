from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')
    
    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            return sum(rating.rating for rating in ratings) / ratings.count()
        return 0
    
    def rating_count(self):
        return self.rating_set.count()

    def __str__(self):
        return self.name

class Rating(models.Model):
    rating = models.SmallIntegerField(default=1)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating
