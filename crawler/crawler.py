import requests
from bs4 import BeautifulSoup
from arxiv_exception import SubjectNotFoundError


base_url = "https://arxiv.org/list/%s/pastweek?skip=0&show=1000"

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

    if subject not in SUBJECT_MAP:
        raise SubjectNotFoundError()

    url = base_url % subject

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    paper_idx_list = []

    for a_tag in soup.find_all('a', title="Abstract"):
        paper_idx_list.append(a_tag.get_text().replace("arXiv:", ""))

