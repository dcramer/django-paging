from paging.paginators import *

def paginate(request, queryset_or_list, per_page=25, endless=True):
    if endless:
        paginator_class = EndlessPaginator
    else:
        paginator_class = BetterPaginator
    
    paginator = paginator_class(queryset_or_list, per_page)
    
    query_dict = request.GET.copy()
    if 'p' in query_dict:
        del query_dict['p']

    try:
        page = int(request.GET.get('p', 1))
    except (ValueError, TypeError):
        page = 1
    if page < 1:
        page = 1

    context = {
        'query_string': query_dict.urlencode(),
        'paginator': paginator.get_context(page),
    }
    return context