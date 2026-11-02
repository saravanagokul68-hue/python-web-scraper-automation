import csv
import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch webpage")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    quote_elements = soup.find_all("div", class_="quote")

    for elem in quote_elements:
        text = elem.find("span", class_="text").get_text()
        author = elem.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in elem.find_all("a", class_="tag")]

        quotes_data.append(
            {"Quote": text, "Author": author, "Tags": ", ".join(tags)}
        )

    with open("scraped_quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Quote", "Author", "Tags"]
        )
        writer.writeheader()
        writer.writerows(quotes_data)

    print(
        f"✅ Success! Extracted {len(quotes_data)} rows and saved to 'scraped_quotes.csv'."
    )


if __name__ == "__main__":
    scrape_quotes()
