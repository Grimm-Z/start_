from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    film_name = models.CharField(max_length=25)
    description = models.TextField()
    date_and_time = models.DateTimeField()
    already_ordered = models.BooleanField(False)
    row = models.IntegerField()
    place = models.IntegerField()

    
class Additional(models.Model):
    class Size(models.TextChoices):
        Small = 'S', 'Small'
        Medium = 'M', 'Medium'
        Large = 'L', 'Large'
        XLarge = 'XL', 'Extra large'
    name = models.CharField(max_length=25)
    size_of_portion = models.CharField(max_length = 10, choices = Size.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["price"]

class Ticket_buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    additional_things = models.ForeignKey(Additional, on_delete=models.CASCADE)

    def __str__(self):
        return self.user, self.ticket, self.start_date, self.end_date, self.status, self.additional_things