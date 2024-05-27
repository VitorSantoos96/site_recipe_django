from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], paginaiton)
        
        
    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        # Current page = 1 qty pages = 2 - middles pages = 2
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], paginaiton)
        
        # Current page = 2 qty pages = 2 - middles pages = 2
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], paginaiton)
        
        # Current page = 3 qty pages = 2 - middles pages = 2
        # HERE RANGE SHOULD CHANGE  
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], paginaiton)
        

    def test_make_sure_middle_ranges_are_correct(self):
        # Current page = 10 qty pages = 2 - middles pages = 2
        # HERE RANGE SHOULD CHANGE  
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], paginaiton)

        # Current page = 14 qty pages = 2 - middles pages = 2
        # HERE RANGE SHOULD CHANGE  
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], paginaiton)
        
    
    def test_make_pagination_range_is_static_when_lass_page_is_next(self):
        # Current page = 19 qty pages = 2 - middles pages = 2
        # HERE RANGE SHOULD CHANGE  
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], paginaiton)
        
        # Current page = 19 qty pages = 2 - middles pages = 2
        # HERE RANGE SHOULD CHANGE  
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], paginaiton)
        
        # Current page = 20 qty pages = 2 - middles pages = 2
        # HERE RANGE SHOULD CHANGE  
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], paginaiton)
        
        # Current page = 21 qty pages = 2 - middles pages = 2
        # HERE RANGE SHOULD CHANGE  
        paginaiton = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], paginaiton)