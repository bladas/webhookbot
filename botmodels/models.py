from django.db import models


class Customer(models.Model):
    customer_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    check = models.BooleanField(null=True,blank=True)

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return f'{self.customer_id} {self.name}'


class Message(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )
    json = models.TextField(null=True)
    customer = models.ForeignKey(to='botmodels.Customer',
                                 on_delete=models.CASCADE,
                                 verbose_name='Користувач'
                                 )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'

    def __str__(self):
        return f'{self.customer} {self.created_at}'
