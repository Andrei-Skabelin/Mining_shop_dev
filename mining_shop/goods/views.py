from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.services import HomePageService
from repository import ProductRepository, ProductCategoryRepository
from constants import MAX_ITEM_IN_PAGE


# Первый вариант: устаревший
def products(request, category_id=None, page=1):
    """Выводим список товаров с категориями"""

    products = ProductRepository.get_products(category_id=category_id)
    categories = ProductCategoryRepository.get_all_product_category()

    paginator = Paginator(object_list=products, per_page=MAX_ITEM_IN_PAGE)
    products_paginator = paginator.page(page)

    # Показывать кнопки назад/вперёд, если элементов больше MAX_ITEM_IN_PAGE
    is_show_buttons = len(products) > MAX_ITEM_IN_PAGE

    context = {
        'title': 'TEST',
        'categories': categories,
        'products': products_paginator,
        'hav_required_item_to_show_buttons': is_show_buttons,
    }
    return render(request, 'products/products.html', context=context)


# второй вариант: улучшенная версия
class HomePage(TemplateView):
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        home_page_context = HomePageService(**kwargs).execute()
        ctx.update(home_page_context)
        return ctx