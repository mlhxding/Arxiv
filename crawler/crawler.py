import requests
import re
from bs4 import BeautifulSoup
from crawler.article import Article
from arxiv_exception import SubjectNotFoundError


# computer science subjects
SUBJECT_MAP = {
    "cs.AI": "Artificial Intelligence",
    "cs.CL": "Computation and Languag",
    "cs.CC": "Computational Complexity",
    "cs.CE": "Computational Engineering, Finance, and Science",
    "cs.CG": "Computational Geometry",
    "cs.GT": "Computer Science and Game Theory",
    "cs.CV": "omputer Vision and Pattern Recognition",
    "cs.CY": "Computers and Society",
    "cs.CR": "Cryptography and Security",
    "cs.DS": "Data Structures and Algorithms",
    "cs.DB": "Databases",
    "cs.DL": "Digital Libraries",
    "cs.DM": "Discrete Mathematics",
    "cs.DC": "Distributed, Parallel, and Cluster Computing",
    "cs.ET": "Emerging Technologies",
    "cs.FL": "Formal Languages and Automata Theory",
    "cs.GL": "General Literature",
    "cs.GR": "Graphics",
    "cs.AR": "Hardware Architecture",
    "cs.HC": "Human-Computer Interaction",
    "cs.IR": "Information Retrieval",
    "cs.IT": "Information Theory",
    "cs.LO": "Logic in Computer Science",
    "cs.LG": "Machine Learning",
    "cs.MS": "Mathematical Software",
    "cs.MA": "Multiagent Systems", 
    "cs.MM": "Multimedia",
    "cs.NI": "Networking and Internet Architecture",
    "cs.NE": "Neural and Evolutionary Computing", 
    "cs.NA": "Numerical Analysis",
    "cs.OS": "Operating Systems",
    "cs.OH": "Other Computer Science",
    "cs.PF": "Performance",
    "cs.PL": "Programming Languages",
    "cs.RO": "Robotics",
    "cs.SI": "Social and Information Networks", 
    "cs.SE": "Software Engineering",
    "cs.SD": "Sound", 
    "cs.SC": "Symbolic Computation", 
    "cs.SY": "Systems and Control"
}

def get_paper_idx_list(subject):
    """extract all the paper_idx from the subject show page
    
    Args:
        subject: element of SUBJECT_MAP, only support Computer Science now

    Returns:
        List of paper_idx, for example ["2007.10534", "2007.10712", "2007.10633"]
    """

    base_url = "https://arxiv.org/list/%s/pastweek?skip=0&show=1000"

    if subject not in SUBJECT_MAP:
        raise SubjectNotFoundError()

    url = base_url % subject

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    paper_idx_list = []

    abstract_tag = soup.find_all('a', title="Abstract")

    assert abstract_tag is not None

    """
    Example of abstract_tag:
    <a href="/abs/2007.10830" title="Abstract">arXiv:2007.10830</a>
    """

    try:
        for a_tag in abstract_tag:
            paper_idx_list.append(a_tag.get_text().replace("arXiv:", ""))
    except Exception as e:
        pass

    return paper_idx_list

def get_article_info(paper_idx: str) -> Article:
    """extract article details from abstract page

    get all the article info, such as title, authors, abstract, subject,
    comments, et.al from abstract page

    Args:
        paper_idx: str. Example: 2007.10830

    Returns:
        article: instance of Article class.

    Raise:
        TypeError: param paper_idx not in the right type
    """

    # validate article idx params
    idx_pattern = r"^\d{4}\.\d{5}$"

    if not isinstance(paper_id, str) or len(paper_id) != 10 \
            or re.search(idx_pattern, self.paper_id) is None:
        raise TypeError

    abstract_url = "https://arxiv.org/abs/" + paper_idx

    