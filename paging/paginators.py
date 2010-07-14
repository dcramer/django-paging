from django.core.paginator import Paginator, InvalidPage, Page, PageNotAnInteger, EmptyPage

__all__ = ('BetterPaginator', 'InvalidPage', 'PageNotAnInteger', 'EmptyPage', 'EndlessPaginator')

class BetterPaginator(Paginator):
    """
    An enhanced version of the QuerySetPaginator.
    
    >>> my_objects = BetterPaginator(queryset, 25)
    >>> page = 1
    >>> context = {
    >>>     'my_objects': my_objects.get_context(page),
    >>> }
    """
    def get_context(self, page, range_gap=5):
        try:
            page = int(page)
        except (ValueError, TypeError), exc:
            raise InvalidPage, exc
        
        try:
            paginator = self.page(page)
        except EmptyPage:
            return {
                'EMPTY_PAGE': True,
            }
        
        if page > 5:
            start = page-range_gap
        else:
            start = 1

        if page < self.num_pages-range_gap:
            end = page+range_gap+1
        else:
            end = self.num_pages+1

        context = {
            'page_range': range(start, end),
            'objects': paginator.object_list,
            'num_pages': self.num_pages,
            'page': page,
            'has_pages': self.num_pages > 1,
            'has_previous': paginator.has_previous(),
            'has_next': paginator.has_next(),
            'previous_page': paginator.previous_page_number(),
            'next_page': paginator.next_page_number(),
            'is_first': page == 1,
            'is_last': page == self.num_pages,
        }
        
        return context

class EndlessPage(Page):
    def __init__(self, *args, **kwargs):
        super(EndlessPage, self).__init__(*args, **kwargs)
        self._has_next = self.paginator.per_page < len(self.object_list)
        self.object_list = self.object_list[:self.paginator.per_page]
    
    def has_next(self):
        return self._has_next
    
class EndlessPaginator(BetterPaginator):
    def page(self, number):
        "Returns a Page object for the given 1-based page number."
        try:
            number = int(number)
        except ValueError:
            raise PageNotAnInteger('That page number is not an integer')
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page + 5
        try:
            _page = EndlessPage(self.object_list[bottom:top], number, self)
        except AssertionError:
            top = top - 5
            _page = EndlessPage(self.object_list[bottom:top], number, self)

        if not _page.object_list:
            if number == 1 and self.allow_empty_first_page:
                pass
            else:
                raise EmptyPage('That page contains no results')
        return _page

    def get_context(self, page):
        try:
            paginator = self.page(page)
        except (PageNotAnInteger, EmptyPage), exc:
            return {'EMPTY_PAGE': True}

        context = {
            'objects': paginator.object_list,
            'page': page,
            'has_previous': paginator.has_previous(),
            'has_next': paginator.has_next(),
            'previous_page': paginator.previous_page_number(),
            'next_page': paginator.next_page_number(),
            'is_first': page == 1,
            'has_pages': paginator.has_next() or paginator.has_previous(),
            'is_last': not paginator.has_next(),
        }
        
        return context