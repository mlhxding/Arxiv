from typing import List
import re
from exception.exception import ArticleFormatException


class Article(object):
    def __init__(self,
                 paper_id: str,  # arXiv identifier, such as 2007.10866
                 title: str,  # article title, string type
                 authors: List[str],  # article authors, a list of authors
                 submitDate: str,  # such as "21 Jul 2020"
                 comments: str = None,  # Comments
                 subjects: str = None,  # Subject, such as Computation and Language (cs.CL)
                 journal_ref: str = None,  # Journal reference
                 ):

        self.paper_id = paper_id
        self.title = title
        self.authors = authors
        self.submitDate = submitDate
        self.comments = comments
        self.subjects = subjects
        self.journal_ref = journal_ref

        self.__validateParams__()

    def __validateParams__(self):

        # validate article idx params
        idx_pattern = r"^\d{4}\.\d{5}$"

        if not isinstance(self.paper_id, str) or len(self.paper_id) != 10 \
                or re.search(idx_pattern, self.paper_id) is None:
            raise ArticleFormatException("idx")
