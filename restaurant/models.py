from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    parent_category = models.ForeignKey(
        'self', null=True, blank=True, related_name='sub_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuEntry(models.Model):
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, blank=True)

    swedish_title = models.CharField(max_length=200, blank=True)
    swedish_description = models.CharField(max_length=200, blank=True)
    hungarian_title = models.CharField(max_length=200, blank=True)
    hungarian_description = models.CharField(max_length=200, blank=True)
    english_title = models.CharField(max_length=200, blank=True)
    english_description = models.CharField(max_length=200, blank=True)

    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.swedish_title}, {self.price}:-'


class Review(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()

    review_text = models.CharField(max_length=800)

    def __str__(self):
        return f'Review by: {self.name} at {self.date_time}'
#<div><img src="{% static "images/bg-parl.png"%}" class="z-[-10] object-cover"></div>
