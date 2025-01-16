from django.db import models


class AuthorsModel(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    pseudo_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField()
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
