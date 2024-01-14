__all__=[
    "DepartmentDoesNotExist",
    "UpdateProductFail",
    "ProductDoesNotExist"
]


class DepartmentDoesNotExist(Exception):
    pass


class UpdateProductFail(Exception):
    pass


class ProductDoesNotExist(Exception):
    pass
