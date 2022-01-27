from django.db import models
        

class Editable(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProductsQuerySet(models.QuerySet):
    def filter_id(self, id):
        return self.filter(id=id)

    def filter_by_product_type_id(self, type_id):
        return self.filter(product_type=type_id)

    def filter_by_name(self, name):
        return self.filter(name=name)

    def filter_by_unit(self, unit):
        return self.filter(unit=unit)


class ProductsModel(Editable):
    PRODUCT_TYPE = (
        ('FOOD', 'อาหาร'),
        ('BEVERAGE', 'เครื่องดื่ม'),
        ('MEDICINE', 'ยารักษาโรค'),
        ('COMSUME', 'ของใช้'),
    )

    UNIT = (
        ('BAHT', 'บาท'),
        ('DOLLAR', 'ดอลล่า'),
        ('YEN', 'เยน'),
    )

    product_type = models.CharField(
        max_length=100, 
        choices=PRODUCT_TYPE,
        default='COMSUME',
        verbose_name='ประเภทสินค้า'
    )
    name = models.CharField(max_length=100, verbose_name='ชื่อสินค้า')
    price = models.DecimalField(max_digits=99, decimal_places=2, verbose_name='ราคาสินค้า')
    unit = models.CharField(
        max_length=100, 
        choices=UNIT,
        default='BAHT',
        verbose_name='หน่วยเงิน'
    )
    objects = ProductsQuerySet.as_manager()

    def __str__(self) -> str:
        return f'[{self.id} - {self.get_product_detail()}]'

    def get_product_detail(self):
        return f'{self.name} ราคา {self.price} {self.unit}'

    class Meta:
        db_table = 'products'
        verbose_name = 'รายการสินค้า'
        verbose_name_plural = verbose_name