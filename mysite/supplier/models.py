from django.db import models


class SupplierModel(models.Model):
	shipper = models.CharField(max_length=50, default=0)
	max_price = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.shipper


class Supplier(models.Model):
	product = models.CharField(max_length=100, default=0)
	shipper_name = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
	price = models.PositiveSmallIntegerField(default=0)
	


	@property
	def price_excess(self):
		max_price = self.supplier_model.max_price
		price = self.price

		if price > max_price:
			return round((((price - max_price)/max_price)* 100), 2)
		else:
			return None

	def __str__(self):
		return self.product


