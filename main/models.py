from django.db import models


class Conс(models.Model):
    dt = models.DateField('Дата')
    title = models.CharField('Наименование сырья', max_length=50)
    fe = models.DecimalField('Железо', max_digits=5, decimal_places=3)
    si = models.DecimalField('Кремний', max_digits=5, decimal_places=3)
    al = models.DecimalField('Алюминий', max_digits=5, decimal_places=3)
    ca = models.DecimalField('Кальций', max_digits=5, decimal_places=3)
    s = models.DecimalField('Сера', max_digits=5, decimal_places=3)

    def __str__(self):
        return self.title + ' - ' + self.dt.strftime('%Y-%m-%d')
        # + self.dt.

    class Meta:
        verbose_name = 'Концентрат'
        verbose_name_plural = 'Концентраты'
