class Result_item_data:
    def __init__(self, kind, title=None, html_title=None, link=None, display_link=None, snippet=None, html_snippet=None, formatted_url=None, html_formatted_url=None, pagemap=None):
        self.kind = kind
        self.title = title
        self.html_title = html_title
        self.link = link
        self.display_link = display_link
        self.snippet = snippet
        self.html_snippet = html_snippet
        self.formatted_url = formatted_url
        self.html_formatted_url = html_formatted_url
        self.pagemap = pagemap

class Result_data:
    def __init__(self, kind, url, queries, context, search_information, items:list[Result_item_data]):
        self.kind = kind
        self.url = url
        self.queries = queries
        self.context = context
        self.search_information = search_information
        self.items = items  # List of Result_item_data