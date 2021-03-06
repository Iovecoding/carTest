# Generated by Django 2.2 on 2021-02-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='装备名称')),
                ('country', models.CharField(max_length=20, verbose_name='研制国家')),
                ('start', models.IntegerField(verbose_name='起始制造年份')),
                ('end', models.IntegerField(verbose_name='终止制造年份')),
                ('costume', models.CharField(max_length=100, verbose_name='主要用户')),
                ('image', models.ImageField(upload_to='images/%Y%m%d')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='全长/m')),
                ('width', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='全宽/m')),
                ('height', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='全高/m')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='重量/吨')),
                ('max_speed', models.IntegerField(verbose_name='最大速度/(km/h)')),
                ('max_stroke', models.IntegerField(verbose_name='最大行程/km')),
            ],
        ),
    ]
