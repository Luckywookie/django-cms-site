from django.db import models
from django.utils import timezone
from cms.models import CMSPlugin


class OfficeItem(CMSPlugin):
    # Create OfficeItem
    number = models.CharField(verbose_name='Номер офиса', max_length=36)
    floor = models.PositiveIntegerField(verbose_name='Этаж', default=0)
    metres = models.PositiveIntegerField(verbose_name='Количество метров', default=0)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    desc = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='offices', blank=True)
    is_free = models.BooleanField(verbose_name='Свободен', default=False)
    published = models.BooleanField(verbose_name='Публикация', default=False)

    def __str__(self):
        return self.number

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['-number', 'floor']


class OfficeLink(CMSPlugin):
    news = models.ForeignKey(OfficeItem, verbose_name="Office")

 #   def copy_relations(self, oldinstance):
 #       self.news = oldinstance.news.all()


class OfficeFloorLink(CMSPlugin):
    office = models.ForeignKey(OfficeItem, verbose_name="Office")