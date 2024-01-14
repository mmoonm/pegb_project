__all__ = [
    "ProductDoesNotExist",
    "RemoveFromCartFail"
]


class ProductDoesNotExist(Exception):
    pass


class RemoveFromCartFail(Exception):
    pass
