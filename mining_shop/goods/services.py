from django.db.models import QuerySet
from django.core.paginator import Paginator

from goods.repository import ProductRepository, ProductCategoryRepository
from goods.constants import MAX_ITEM_IN_PAGE
from goods.paginator import ProductPaginator
from goods.utils import is_show_buttons


class HomePageService:
    def __init__(self, category_id: int = None, page: int = 1):
        self.category_id = category_id
        self.page = page
        self.all_products = ProductRepository.get_products(category_id=self.category_id)

    @staticmethod
    def _build_context(categories: QuerySet, show_buttons: bool, products_paginator: Paginator):
        return {
            'categories': categories,
            'products': products_paginator,
            'hav_required_item_to_show_buttons': show_buttons,
        }

    def execute(self):
        categories: QuerySet = ProductCategoryRepository.get_all_product_category()
        show_buttons: bool = is_show_buttons(
            qs=self.all_products,
            page_count=MAX_ITEM_IN_PAGE)

        products_paginator: Paginator = ProductPaginator(
            object_list=self.all_products,
            per_page=MAX_ITEM_IN_PAGE).get_paginator_page(page=self.page)

        return self._build_context(categories, show_buttons, products_paginator)
