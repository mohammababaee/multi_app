import requests
from bs4 import BeautifulSoup


def get_news(url):
    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all elements with class="newsbox-2"
    newsbox_2_elements = soup.find_all("div", class_="newsbox-2")[:20]

    for news_box in newsbox_2_elements:
        # Extract relevant information
        news_content = news_box.find("div", class_="news-content")
        title = news_content.find("a", class_="title").find("h3").text
        news_data = news_content.find("div", class_="news-data")
        time = news_data.find("time").text.strip()
        link = news_content.find("a", class_="title")["href"]

        # Print the extracted data
        print("Time:", time)
        print("Title:", title)
        print("Link:", link)
        print("-" * 30)


# URL of the webpage
url = "https://www.varzesh3.com/news"  # It's not recommended to hardcode URLs directly into your application like this. While it's acceptable at the development stage, in production, it's better to use environment variables or configuration files to manage such URLs securely.
get_news(url)
