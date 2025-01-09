from decimal import Decimal
import inspect

from example10_3 import Order
import example10_7

promos = [func for _, func in inspect.getmembers(example10_7, inspect.isfunction)]

def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)
