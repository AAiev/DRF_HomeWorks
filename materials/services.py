import stripe

from config.settings import STRIPE_API_KEY


class StripeAPI:

    def __init__(self):
        self.stripe = stripe
        self.stripe.api_key = STRIPE_API_KEY

    def get_products(self):
        return self.stripe.Product.list()

    def create_product(self, name, price):
        product = self.stripe.Product.create(name=name)
        return self.stripe.Price.create(
            currency="rub",
            unit_amount=price * 100,
            product=product.id,
        )

    def create_session(self, price_id):
        return self.stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[{"price": price_id, "quantity": 1}],
            mode="payment",
        )
