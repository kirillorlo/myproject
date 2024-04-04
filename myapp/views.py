from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Order

logger = logging.getLogger(__name__)


def home(request):
    html = """
    <h1>Добро пожаловать на сайт магазина "Рок-атрибутика"</h1>
    <p>Мы рады приветствовать вас!</p>
    <img src="https://cs10.pikabu.ru/post_img/2018/09/29/7/153821765616872994.jpg" alt="Рок-атрибутика">
    """
    logger.info('Посещение главной страницы магазина')

    return HttpResponse(html)


def about(request):
    html = """
    <h1>О нас</h1>
    <p>Магазин рок-атрибутики отличное место для всех рок-любителей, музыкантов и тех, кто любит особенный стиль. У нас вы найдете все необходимое, чтобы выразить свою страсть к рок-музыке и создать неповторимый образ. Посетите наш магазин и погрузитесь в мир рока уже сегодня!</p>
    """
    logger.info('Посещение страницы с описанием магазина')

    return HttpResponse(html)


def client_orders(request):
    # Получить текущую дату и время
    current_time = timezone.now()
    # Определение даты начала периода
    week_ago = current_time - timedelta(days=7)
    month_ago = current_time - timedelta(days=30)
    year_ago = current_time - timedelta(days=365)
    # Получение списка всех заказов клиента за разные периоды
    orders_week = Order.objects.filter(client=request.user, created_at__gte=week_ago)
    orders_month = Order.objects.filter(client=request.user, created_at__gte=month_ago)
    orders_year = Order.objects.filter(client=request.user, created_at__gte=year_ago)
    # Сортировка списка товаров
    products_week = orders_week.values_list('product', flat=True).distinct()
    products_month = orders_month.values_list('product', flat=True).distinct()
    products_year = orders_year.values_list('product', flat=True).distinct()
    # Передача данных в шаблон
    context = {
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year
    }
    return render(request, 'client_orders.html', context)
