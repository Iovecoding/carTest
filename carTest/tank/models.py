from django.db import models

# Create your models here.
class Tank(models.Model):
    name = models.CharField(verbose_name=u'装备名称',max_length = 100)
    country = models.CharField(verbose_name =u'研制国家',max_length = 20)
    start = models.IntegerField(verbose_name =u'起始制造年份')
    end = models.IntegerField(verbose_name =u'终止制造年份')
    costume = models.CharField(verbose_name=u'主要用户',max_length = 100)
    image = models.ImageField(upload_to='images/%Y%m%d')

    #基本参数
    length = models.DecimalField(verbose_name= u'全长/m',max_digits = 10, decimal_places=2)
    width = models.DecimalField(verbose_name=u'全宽/m', max_digits=10, decimal_places=2)
    height = models.DecimalField(verbose_name= u'全高/m',max_digits = 10, decimal_places=2)
    weight = models.DecimalField(verbose_name= u'重量/吨',max_digits = 10, decimal_places=2)
    max_speed = models.IntegerField(verbose_name=u'最大速度/(km/h)')
    max_stroke = models.IntegerField(verbose_name=u'最大行程/km')

    def __str__(self):
        return self.name

    class meta:
        db_table = 'Tanks'  # 表名称

        verbose_name = '坦克'  # 表备注

        # 表名复数形式，如果不设置末尾会多一个s
        verbose_name_plural = verbose_name

        ordering = ['id']

