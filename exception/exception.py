
class ArticleFormatException(Exception):
    def __init__(self, locate:str):
        super().__init__(self)
        self.locate = locate
        self.msg = "Article %s Format Error!" % self.locate

    def __str__(self):
        return self.msg
