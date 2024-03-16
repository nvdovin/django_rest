"""В этом файле я подключаюсь к страйпу, чтобы подключить к моему проекту платежную систему"""

from datetime import datetime
import stripe


class StripePayment:
    """Класс для работы со страйпом"""

    def __init__(self) -> None:
        stripe.api_key = "sk_test_51OusigBmOnO8BJxu9KNMQzQucCkWv9lPTdsSIDSMymavPsfTkZP61hLWJ1ziTN8Jj4gyahB5R6X4iVFE4yJAmbTF00145tGscq"

    def create_payment(self, title: str, valute="rub", value=1000):
        """Метод создания оплаты для продукции"""
        stripe.Price.create(
            currency=valute,
            unit_amount=value,
            product_data={"name": title},
        )

    def pay(self, current_user, payment_value=1000):
        """Метод для непосредственной оплаты готовой продукции"""
        # price_1Ov3R4BmOnO8BJxuZIuZl20i -- ID готовой продукции, которую будем оплачивать

        stripe.checkout.Session.create(
            success_url="http://localhost:8000/view_lessons/",
            line_items=[{"price": "price_1Ov3R4BmOnO8BJxuZIuZl20i", "quantity": 2}],
            mode="payment",
            payment_method_types=["card"],  # Добавляем разрешенные типы платежных методов
            
            # попытка катомизировать это дело и передавать прямо сюда данные из запроса
            user=current_user,
            payment_date=datetime.now(),
            payment_sum=payment_value

        )
