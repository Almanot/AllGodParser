class response_data:
    def __init__(self, kind, title, html_title, link, display_link, snippet, html_snippet, formatted_url, html_formatted_url, pagemap=None):
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