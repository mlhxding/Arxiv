from typing import List
import re
from datetime import datetime
from exception.exception import ArticleFormatException

MONTH_MAP = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sept": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

class Article(object):
    """
    Class for Article
    """
    def __init__(self,
                 paper_id: str,  # arXiv identifier, such as 2007.10866
                 title: str,  # article title, string type
                 authors: List[str],  # article authors, a list of authors
                 submitDate: str,  # such as "21 Jul 2020"
                 subjects: List[str],  # Subject, such as Computation and Language (cs.CL)
                 comments: str = None,  # Comments
                 journal_ref: str = None,  # Journal reference
                 ):

        self.paper_id = paper_id
        self.title = title
        self.authors = authors
        self.submitDate = formatSubmitDate(submitDate)
        self.comments = comments
        self.subjects = subjects
        self.journal_ref = journal_ref

        self.validateParams()

    def validateParams(self):

        # validate article idx params
        idx_pattern = r"^\d{4}\.\d{5}$"

        if not isinstance(self.paper_id, str) or len(self.paper_id) != 10 \
                or re.search(idx_pattern, self.paper_id) is None:
            raise ArticleFormatException("idx")

        if len(self.subjects) <= 1:
            raise ArticleFormatException("Subjects")

    @staticmethod
    def formatSubmitDate(submitdate):
        """
        transform submitDate from string type to datetime
        Example：
        transform “21 Jul 2020” to datetime(year=2020, month=7, day=21)
        """

        assert isinstance(submitdate, str)

        [day_str, month_str, year_str] = submitdate.split()

        