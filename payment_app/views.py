from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from materials_app.models import Course
from payment_app.services_payment import StripePayment
from .models import Payments

# Create your views here.

class PaymentAPIView(APIView):
    """Класс что была возможность совершать платежи"""
    
    def post(self, *args, **kwargs):
        course_id = self.request.data["course"]
        course_item = get_object_or_404(Course, pk=course_id)
        if course_item:
            payment_class = StripePayment()
            
            product_id = payment_class.create_product(name="Оплата курса", description="Оплата курса")
            price_id = payment_class.create_price(amount=10000, product_id=product_id, currency="rub")
            payment_url = payment_class.create_session(price_id=price_id)
            
            new_payment = Payments.objects.create(user=self.request.user, payment_url=payment_url)
            new_payment.save()
            return Response({"message": "Ссылка для оплаты", "url": payment_url})
        else:
            print("Такого курса нет")
            return Response({"message": "Нет такого курса"})