import string
import secrets
from datetime import date
from django.db.models import sum
from .models import Coupon, Order


def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    """
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code

def get_daily_sales_total(date: date):
    """
    calculate the total sales revenue for given date.
    :param date: A datetime.date object
    :return: Decimal total sales  for the day
    """

    orders = Order.objects.filter(created_at__date=date)

    total = orders.aggregate(total_sum=sum('total_price'))['total_sum']

    return total or 0