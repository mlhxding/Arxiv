from crawler.crawler import get_article_info, get_paper_idx_list


if __name__ == "__main__":
    subject = "cs.CL"
    papar_list_idx = get_paper_idx_list(subject)
    for paper_idx in papar_list_idx:
        article = get_article_info(paper_idx)
        print(article.to_json())
