from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity


class Order(NamedTuple):  # the context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional["Promotion"] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f"<Order total: {self.total():.2f} due: {self.due():.2f}>"


class Promotion(ABC):  # the Strategy: an abstract base class
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order: Order) -> Decimal:
        rate = Decimal("0.05")
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)


class BulkItemPromo(Promotion):  # second Concrete strategy
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal("0.1")
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal("0.7")
        return Decimal(0)


joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)
cart = [
    LineItem("banana", 4, Decimal(".5")),
    LineItem("apple", 10, Decimal("1.5")),
    LineItem("watermelon", 5, Decimal(5)),
]
# print(Order(joe, cart, FidelityPromo()))
# print(Order(ann, cart, FidelityPromo()))
banana_cart = (
    LineItem("banana", 30, Decimal(".5")),
    LineItem("apple", 10, Decimal("1.5")),
)
# print(Order(joe, banana_cart, BulkItemPromo()))
long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))
print(Order(joe, long_cart, LargeOrderPromo()))
