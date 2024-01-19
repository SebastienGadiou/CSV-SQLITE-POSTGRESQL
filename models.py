from django.db import models


class transfer(models.Model):

    Year = models.CharField(("Year"),max_length=200)
    Australia =models.FloatField(("Australia"))
    Canada = models.FloatField(("Canada"),max_length=255)
    France =models.FloatField(("France"),max_length=255)
    Germany =models.FloatField(("Germany"),max_length=255)
    Italy = models.FloatField(("Italy"), max_length=255)
    Japan = models.FloatField(("Japan"), max_length=255)
    Mexico = models.FloatField(("Mexico"), max_length=255)
    Korea = models.FloatField(("South_Korea"), max_length=255)
    UK = models.FloatField(("UK"), max_length=255)
    USA = models.FloatField(("USA"), max_length=255)

