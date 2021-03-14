from bs4 import BeautifulSoup
import requests
import csv


csv_file = open("csv_blog_file.csv", "w")
csv_writter = csv.writer(csv_file)
csv_writter.writerow(["title", "tag", "image", "created_date", "content"])


url = requests.get("https://teonite.com/blog/")

soup = BeautifulSoup(url.text, "lxml")


tag_list = []
for blog_article in soup.find_all("div", class_="post-container"):
    article_title = blog_article.a.text
    print(article_title)

    for article_tag_list in blog_article.find_all("li", class_="post-tag"):
        art_tag_list = article_tag_list.a.text
        tag_list.append(art_tag_list)
        print(art_tag_list)

    # for article_tag_list in soup.find_all("ul", class_="tags-list"):
    #     article_tag_list_item = article_tag_list.find("li", class_="post-tag").a.text
    #     print(article_tag_list_item)

    article_img = blog_article.find("img", class_="blog-image")["src"]
    print(article_img)

    article_date = blog_article.find("div", class_="post-info").span.text
    print(article_date)

    article_content = blog_article.find("div", class_="post-content").p.text
    print(article_content)

    print("-------------------------------------------------------------------------")

    # tag_list = ",".join(tag_list)
    rows = [article_title, tag_list, article_img, article_date, article_content]

    csv_writter.writerow(rows)


csv_file.close()