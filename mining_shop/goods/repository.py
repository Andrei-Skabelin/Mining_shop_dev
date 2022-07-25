from goods.models import Product, ProductCategory
from django.db.models import QuerySet


class ProductRepository:
    @staticmethod
    def get_all_products() -> Product:
        return Product.objects.all()

    @classmethod
    def get_products_by_category(cls, category_id: int) -> Product:
        return cls.get_all_products().filter(category_id=category_id)

    @classmethod
    def get_products(cls, category_id: int = None) -> Product:
        if category_id is not None:
            return cls.get_products_by_category(category_id=category_id)
        return cls.get_all_products()

    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return Product.objects.get(id=product_id)


class ProductCategoryRepository:
    @staticmethod
    def get_all_product_category() -> QuerySet:
        return ProductCategory.objects.all()
