from django.db import models


class MenuCategory(models.Model):
    menu_category = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_category


class MenuEntry(models.Model):
    swedish_title = models.CharField(max_length=200, blank=True)
    swedish_description = models.CharField(max_length=200, blank=True)
    hungarian_title = models.CharField(max_length=200, blank=True)
    hungarian_description = models.CharField(max_length=200, blank=True)
    english_title = models.CharField(max_length=200, blank=True)
    english_description = models.CharField(max_length=200, blank=True)

    price = models.IntegerField(default=0)

    menu_category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.swedish_title}, {self.price} :-'


class Review(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()

    review_text = models.CharField(max_length=800)

    def __str__(self):
        return f'Review by: {self.name} at {self.date_time}'
