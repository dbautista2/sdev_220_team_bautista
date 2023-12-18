from decimal import Decimal
from django.db import models
from django.utils.functional import cached_property

PRICES = (
    (Decimal(0.0), "$0.00"),
    (Decimal(0.25), "$0.25"),
    (Decimal(0.5), "$0.50"),
    (Decimal(1.0), "$1.00"),
    (Decimal(1.5), "$1.50"),
    (Decimal(2.0), "$2.00"),
    (Decimal(2.5), "$2.50"),
    (Decimal(3.0), "$3.00"),
    (Decimal(3.5), "$3.50"),
    (Decimal(4.0), "$4.00"),
    (Decimal(4.5), "$4.50"),
    (Decimal(5.0), "$5.00"),
    (Decimal(5.5), "$5.50"),
    (Decimal(6.0), "$6.00"),
    (Decimal(6.5), "$6.50"),
    (Decimal(7.0), "$7.00"),
    (Decimal(7.5), "$7.50"),
    (Decimal(8.0), "$8.00"),
    (Decimal(8.5), "$8.50"),
    (Decimal(9.0), "$9.00"),
    (Decimal(9.5), "$9.50"),
    (Decimal(10.0), "$10.00"),
)


class Sauce(models.Model):
    """
    Model for Sauces
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    base_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )

    def __str__(self):
        return self.name

    @cached_property
    def price(self):
        return self.base_price + self.additional_price


class Topping(models.Model):
    """
    Model for Toppings
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    base_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )

    def __str__(self):
        return self.name

    @cached_property
    def price(self):
        return self.base_price + self.additional_price


class Cheese(models.Model):
    """
    Model for Cheeses
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    base_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )

    def __str__(self):
        return self.name

    @cached_property
    def price(self):
        return self.base_price + self.additional_price


class Bun(models.Model):
    """
    Model for Buns
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    base_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )

    def __str__(self):
        return self.name

    @cached_property
    def price(self):
        return self.base_price + self.additional_price


class Patty(models.Model):
    """
    Model for Patties
    """

    name = models.CharField(max_length=50)
    patty_count = models.IntegerField(
        choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")), default=1
    )
    description = models.CharField(max_length=200)
    base_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )

    class Meta:
        verbose_name_plural = "Patties"

    def __str__(self):
        return self.name

    @cached_property
    def price(self):
        return self.base_price + self.additional_price


class Burger(models.Model):
    """
    Model for Burgers
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )
    bun = models.ForeignKey("Bun", on_delete=models.CASCADE)
    patty = models.ForeignKey("Patty", on_delete=models.CASCADE)
    cheese = models.ForeignKey("Cheese", on_delete=models.CASCADE)
    toppings = models.ManyToManyField("Topping")
    sauces = models.ManyToManyField("Sauce")
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0.0))
    is_signature = models.BooleanField(default=False)  # New field for signature burgers

    def __str__(self):
        return self.name

    @cached_property
    def price(self):
        return (
            self.bun.price
            + self.patty.price
            + self.cheese.price
            + sum(topping.price for topping in self.toppings.all())
            + sum(sauce.price for sauce in self.sauces.all())
            - self.discount
        )


class Side(models.Model):
    """
    Model for Sides
    """

    base_price = Decimal(0.0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )

    def __str__(self):
        return self.name

    def price(self):
        return self.base_price + self.additional_price


class Drink(models.Model):
    """
    Model for Drinks
    """

    base_price = Decimal(0.0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    additional_price = models.DecimalField(
        max_digits=5, decimal_places=2, choices=PRICES, default=Decimal(0.0)
    )

    def __str__(self):
        return self.name

    def price(self):
        return self.base_price + self.additional_price


class Combo(models.Model):
    """
    Model for Combos
    Combos are defined as a Burger, Side, and Drink and a combo discount
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    burger = models.ForeignKey("Burger", on_delete=models.CASCADE)
    side = models.ForeignKey("Side", on_delete=models.CASCADE)
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0.0))

    def __str__(self):
        return self.name

    def compute_price(self):
        return (
            self.burger.compute_price()
            + self.side.compute_price()
            + self.drink.compute_price()
            - self.discount
        )


class Order(models.Model):
    """
    Model for Orders
    Orders are defined as a list of Combos, Burgers, Sides, and Drinks
    Discounts can be applied with promo codes
    """

    name = models.CharField(max_length=50)
    combos = models.ManyToManyField("Combo", related_name="orders")
    burgers = models.ManyToManyField("Burger", related_name="orders")
    sides = models.ManyToManyField("Side", related_name="orders")
    drinks = models.ManyToManyField("Drink", related_name="orders")
    sauces = models.ManyToManyField("Sauce", related_name="orders")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Order - {self.id} for {self.name}"

    def total_cost(self):
        return sum(
            (
                sum(burger.price for burger in self.burgers.all()),
                sum(side.price for side in self.sides.all()),
                sum(drink.price for drink in self.drinks.all()),
                sum(sauce.price for sauce in self.sauces.all()),
            )
        )
