__all__=[
    "DepartmentDoesNotExist",
    "CreateProductFail"
]


class DepartmentDoesNotExist(Exception):
    pass


class CreateProductFail(Exception):
    pass
