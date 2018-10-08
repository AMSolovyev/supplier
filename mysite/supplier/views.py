from django.shortcuts import render
from .models import SupplierModel, Supplier


def suppliers_table(request):
	supplier_select = request.POST.get('supplier_select')
	supplier_models = SupplierModel.objects.all()

	if (supplier_select is None or supplier_select=='all'):
		suppliers = Supplier.objects.all().order_by('product')
	else:
		suppliers = Supplier.objects.filter(shipper_name=supplier_select).all()

	return render(request, 'supplier/suppliers_table.html', {'suppliers': suppliers,
		                                                    'supplier_models': supplier_models
		                                                     })