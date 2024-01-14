__all__ = [
    "ProductDoesNotExist",
    "AddToCartFail"
]


class ProductDoesNotExist(Exception):
    pass


class AddToCartFail(Exception):
    pass
