import stripe

from config import settings



class StripePayment:
    """Класс для удобной работы с платежами в Stripe.
В классе присутствуют методы для создания:

    1. Продукта - create_product
    2. Цены на продукты - create_price
    3. Сессии покупки - create_session
    4. Оплаты - pay
    """
    
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def create_product(self, name: str, description: str) -> str:
        """Метод для создания продукта

        Args:
            name (str): Назание продукта
            description (str): Описание продукта

        Returns:
            str: ID продукта
        """
        product = stripe.Product.create(
            name=name,
            type='service',
            description=description
        )
        print(product)
        return product["id"]
    
    def create_price(self, amount: int, product_id: str, currency="rub") -> str:
        """Создает цену для продукта, используя заданное количество, идентификатор продукта и валюту.
        
        Parameters:
            amount (int): Единичная сумма для цены.
            product_id (str): Идентификатор продукта, для которого создается цена.
            currency (str, опционально): Валюта для цены. По умолчанию "rub".
        
        Returns:
            str: Идентификатор созданной цены."""
        
        price = stripe.Price.create(
            unit_amount=amount,
            currency=currency,
            product=product_id
        )
        print(price)
        return price["id"]
    
    def create_session(self, price_id: str) -> str:
        """
        Создает сессию для совершения покупки.

        Parameters:
            price_id (str): ID цены для сессии.

        Returns:
            str: ID созданный сессии.
        """
        session = stripe.checkout.Session.create(
            line_items=[{
                'price': price_id,
                'quantity': 1
            }],
            mode='payment',
            success_url='http://localhost:8000/',
            cancel_url='http://localhost:8000/'
        )
        print(session)
        return session["url"], session["id"]
    
    def pay(self, session_id: str):
        """Метод для обработки платежа с использованием предоставленного идентификатора сессии.

        :param session_id: str - идентификатор сессии для платежа
        :return: str - статус платежа"""
        
        payment_intent = stripe.PaymentIntent.create(
            payment_method=self.create_payment_method(),
            amount=1000,
            currency='usd',
            confirm=True,
            payment_method_types=['card'],
            payment_session=session_id
        )
    
    def create_payment_method(self):
        """Метод для создания метода оплаты, болванка с картой"""
        
        return stripe.PaymentMethod.create(
            payment_method=stripe.PaymentMethod.create(
                type='card',
                card={
                    'number': '4242424242424242',
                    'exp_month': 12,
                    'exp_year': 2023,
                    'cvc': '123',
                },
            )
        )