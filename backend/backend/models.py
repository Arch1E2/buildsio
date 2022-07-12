from django.db import models

class Valute(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Rate(models.Model):
    valute = models.ForeignKey(Valute, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()
    nominal = models.PositiveIntegerField()

    def __str__(self):
        return self.valute.name + ' ' + str(self.date)

    class Meta:
        ordering = ['-date']