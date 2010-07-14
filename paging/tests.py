import unittest

from paging.helpers import paginate
from paging.paginators import *

class PagingUnitTest(unittest.TestCase):
    def test_better_paginator(self):
        objects = range(1, 100)
        
        paginator = BetterPaginator(objects, 1)
        for num in objects:
            page = paginator.get_context(num)
            self.assertEquals(page['objects'], [num])
            self.assertEquals(page['has_next'], num < 99)
            self.assertEquals(page['has_previous'], num > 1)
            self.assertEquals(page['is_first'], num == 1)
            self.assertEquals(page['is_last'], num == 99)
            self.assertEquals(page['previous_page'], num - 1 if num else False)
            self.assertEquals(page['next_page'], num + 1)
            self.assertEquals(page['page'], num)
            self.assertEquals(page['num_pages'], 99)
            # XXX: this test could be improved
            self.assertTrue(page['page_range'])

    def test_endless_paginator(self):
        objects = range(1, 100)
        
        paginator = EndlessPaginator(objects, 1)
        for num in objects:
            page = paginator.get_context(num)
            self.assertEquals(page['objects'], [num])
            self.assertEquals(page['has_next'], num < 99)
            self.assertEquals(page['has_previous'], num > 1)
            self.assertEquals(page['is_first'], num == 1)
            self.assertEquals(page['is_last'], num == 99)
            self.assertEquals(page['previous_page'], num - 1 if num else False)
            self.assertEquals(page['next_page'], num + 1)
            self.assertEquals(page['page'], num)
