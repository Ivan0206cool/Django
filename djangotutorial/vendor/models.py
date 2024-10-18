from django.db import models
from django.contrib import admin
# Create your models here.
class Vendor(models.Model):
	vendor_name = models.CharField(max_length = 20) # 攤販的名稱
	store_name = models.CharField(max_length = 10) # 攤販店家的名稱
	phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
	address = models.CharField(max_length = 100) # 攤販的地址
	def __str__(self):
		return self.vendor_name
class Food(models.Model):
	food_name = models.CharField(max_length = 30) # 食物名稱
	food_price = models.DecimalField(max_digits = 3, decimal_places=0) # 食物價錢
	food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的
	def __str__(self):
		return self.food_name


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    # 這裡我一併將 Vendor 類別 其它的欄位都加進來了
	list_display = [field.name for field in Vendor._meta.fields]
	# list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']
	

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Food._meta.fields]
	list_filter = ('food_price',)
	search_fields = ('food_name','food_price') # 搜尋欄位