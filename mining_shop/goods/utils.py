from django.db.models import QuerySet


def is_show_buttons(qs: QuerySet, page_count: int) -> bool:
    """Нужно ли показывать кнопки назад/вперёд в пагинации,
    если кол-во элементов больше/или меньше вместимости на странице"""
    return len(qs) > page_count
