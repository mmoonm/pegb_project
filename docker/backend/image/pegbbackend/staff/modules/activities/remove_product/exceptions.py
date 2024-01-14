__all__=[
    "DepartmentDoesNotExist",
    "RemoveProductFail"
]


class DepartmentDoesNotExist(Exception):
    pass


class RemoveProductFail(Exception):
    pass
