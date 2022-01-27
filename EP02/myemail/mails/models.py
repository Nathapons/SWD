from django.db import models


class EmailModel(models.Model):
    to_mail = models.CharField(max_length=255, verbose_name='รายชื่อผู้รับ', help_text='ชนิดเมล gmail')
    topics = models.CharField(max_length=255, verbose_name='หัวเรื่องจดหมาย')
    mail_detail = models.TextField(default='', verbose_name='เนื้อความในอีเมล')

    class Meta:
        db_table = 'email'
        verbose_name = 'อีเมล'
        verbose_name_plural = verbose_name
