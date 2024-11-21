import requests
import pathlib
import json
from bs4 import BeautifulSoup

pages = []

base_url = "https://brobizz.com"
urls = ["https://brobizz.com/kundeservice/"]

visited_urls = []

# Until all pages have been visited
while len(urls) > 0:
    # Get the current URL to visit
    current_url = urls.pop()

    # Crawling logic
    response = requests.get(current_url)
    soup = BeautifulSoup(response.text, "html.parser")

    visited_urls.append(current_url)
    pages.append({"url": current_url, "content": soup.get_text()})

    link_elements = soup.select("a[href]")

    for link_element in link_elements:
        url = link_element["href"]
        url.replace(base_url, "")
        url = base_url + url
        if "https://brobizz.com/kundeservice/" in url:
            if url not in visited_urls and url not in urls:
                urls.append(url)

# Save data to file in data folder
this_file_path = pathlib.Path(__file__).parent.absolute()
output_path = this_file_path.parent.parent.parent / "data" / "pages.json"
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w+") as file:
    json.dump(pages, file)
