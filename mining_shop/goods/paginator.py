from django.core.paginator import Paginator
from django.db.models import QuerySet


class ProductPaginator:
    def __init__(self, object_list: QuerySet, per_page: int):
        self.product_paginator = Paginator(object_list=object_list, per_page=per_page)

    def get_paginator_page(self, page: int):
        return self.product_paginator.page(page)
