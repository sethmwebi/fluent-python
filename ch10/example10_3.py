from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Callable, NamedTuple, Optional


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self):
        return self.price * self.quantity


@dataclass(frozen=True)
class Order:  # the context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[["Order"], Decimal]] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f"<Order total: {self.total():.2f} due: {self.due():.2f}>"


def fidelity_promo(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal("0.05")
    return Decimal(0)


def bulk_item_promo(order: Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal("0.1")
    return discount


def large_order_promo(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal("0.07")
    return Decimal(0)

promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')), LineItem('watermelon', 5, Decimal(5))]
# print(Order(joe, cart, fidelity_promo))
# print(Order(ann, cart, fidelity_promo))
banana_cart = [LineItem('banana', 30, Decimal('.5')), LineItem('apple', 10, Decimal('1.5'))]
# print(Order(joe, banana_cart, bulk_item_promo))
long_cart = [LineItem(str(item_code), 1, Decimal(1)) for item_code in range(10)]
# print(Order(joe, long_cart, large_order_promo))
# print(Order(joe, cart, large_order_promo))
# print(Order(joe, long_cart, best_promo))
# print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))
