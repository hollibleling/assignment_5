from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 300

    # def get_next_link(self):
    #     if not self.page.has_next():
    #         return None
    #     page_number = self.page.next_page_number()
    #     return page_number

    # def get_previous_link(self):
    #     if not self.page.has_previous():
    #         return None
    #     page_number = self.page.previous_page_number()
    #     return page_number

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'results': schema,
            },
        }
