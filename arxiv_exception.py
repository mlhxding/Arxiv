
class ArticleFormatException(Exception):
    def __init__(self, locate:str):
        super().__init__(self)
        self.locate = locate
        self.msg = "Article %s Format Error!" % self.locate

    def __str__(self):
        return self.msg


class SubjectNotFoundError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return "Subject Not Found Error! See https://arxiv.org/ for more information"


class IllegalHTMLPageError(Exception):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "Illegal HTML Page Error, page may not in the expect format!"