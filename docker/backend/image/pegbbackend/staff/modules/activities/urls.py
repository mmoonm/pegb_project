from django.urls import path, include

from staff.modules.activities.add_category_discount.view import AddCategoryDiscount
from staff.modules.activities.add_customer_discount.view import AddCustomerDiscount
from staff.modules.activities.add_product.view import AddProduct
from staff.modules.activities.get_list_category.view import GetListCategory
from staff.modules.activities.get_list_product.view import GetListProduct
from staff.modules.activities.remove_product.view import RemoveProduct
from staff.modules.activities.update_product.view import UpdateProduct

urlpatterns = [
    path('add-product/', AddProduct.as_view()),
    path('update-product/', UpdateProduct.as_view()),
    path('remove-product/', RemoveProduct.as_view()),
    path('add-category-discount/', AddCategoryDiscount.as_view()),
    path('add-customer-discount/', AddCustomerDiscount.as_view()),
    path('get-list-category/', GetListCategory.as_view()),
    path('get-list-product/', GetListProduct.as_view()),
]
