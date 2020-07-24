from typing import List
import re
import json
from datetime import datetime
from arxiv_exception import ArticleFormatException


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
    """Class for Article

    Attributes:
        paper_id: str, arXiv identifier, for example: 2007.10866
        title: str, article title, string type
        authors: list of string, article authors, list of authors
        abstract: str, abstract
        submitDate: str, for example: "21 Jul 2020"
        subjects: list of str, Subject, for example: Computation and Language (cs.CL)
        comments: str, default None,  Comments
        journal_ref: str, default None,  Journal reference
    """
    def __init__(self,
                 paper_id: str,  # arXiv identifier, such as 2007.10866
                 title: str,  # article title, string type
                 authors: List[str],  # article authors, a list of authors
                 abstract: str, # abstract
                 submitDate: str,  # such as "21 Jul 2020"
                 subjects: List[str],  # Subject, such as Computation and Language (cs.CL)
                 comments: str = None,  # Comments
                 journal_ref: str = None,  # Journal reference
                 ):

        self.paper_id = paper_id
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.submitDate = formatSubmitDate(submitDate)
        self.comments = comments
        self.subjects = subjects
        self.journal_ref = journal_ref

        self.validateParams()

    def validateParams(self):
        """
        validate correctness for input params
        """

        # validate article idx params
        idx_pattern = r"^\d{4}\.\d{5}$"

        if not isinstance(self.paper_id, str) or len(self.paper_id) != 10 \
                or re.search(idx_pattern, self.paper_id) is None:
            raise ArticleFormatException("idx")

        # validate abstract params
        if self.abstract is None:
            raise ArticleFormatException("Abstract")

        # validate subjects params
        if len(self.subjects) <= 1:
            raise ArticleFormatException("Subjects")

        # validate article id match submit date
        idx_year = int(self.paper_id[:4])
        idx_month = int(self.paper_id[-5:])

        if idx_month != self.submitDate.month or idx_year != self.submitDate.year:
            raise ArticleFormatException("SubmitDate")

    @staticmethod
    def formatSubmitDate(submitdate):
        """
        transform submitDate from string type to datetime
        Example：
        transform “21 Jul 2020” to datetime(year=2020, month=7, day=21)
        """

        assert isinstance(submitdate, str)

        if len(submitdate.split()) == 3:
            [day_str, month_str, year_str] = submitdate.split()
            return datetime(year=int(year_str), month=MONTH_MAP[month_str], day=int(day_str))
        else:
            return None

    def to_json(self):
        """convert Article class to Json object

        Returns:
            article_json: json object of article
        """
        return json.dumps({
                "paper_idx": self.paper_id,
                "title": self.title,
                "author": self.authors,
                "abstract": self.abstract,
                "submitDate": self.submitDate,
                "subjects": self.subjects,
                "comments": self.comments,
                "journal_ref": self.journal_ref}, indent=4
        )