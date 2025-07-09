import time
import json
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def scrape_articles():
    # Setup Chrome in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    base_url = "https://daily.sevenfifty.com/"
    driver.get(base_url)
    time.sleep(5)

    # Scroll to load more articles
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_pause_time = 2
    max_scrolls = 5

    for _ in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get article URLs
    article_links = []
    article_elements = driver.find_elements(By.CSS_SELECTOR, "h2 a")

    for elem in article_elements:
        link = elem.get_attribute("href")
        if link and link.startswith("https://daily.sevenfifty.com"):
            article_links.append(link)

    print(f"Found {len(article_links)} articles.")

    articles = []
    for url in article_links:
        try:
            driver.get(url)
            time.sleep(2)

            title = driver.find_element(By.TAG_NAME, "h1").text.strip()
            try:
                author = driver.find_element(By.CSS_SELECTOR, "span.author-name").text.strip()
            except:
                author = "SevenFifty Daily Editors"

            try:
                publish_date = driver.find_element(By.CSS_SELECTOR, "meta[property='article:published_time']").get_attribute("content")
            except:
                publish_date = ""

            try:
                tags = [tag.text.strip() for tag in driver.find_elements(By.CSS_SELECTOR, ".post-tags a")]
            except:
                tags = []

            paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.post-content > p")
            content = "\n".join([p.text for p in paragraphs if p.text.strip()])

            article = {
                "url": url,
                "title": title,
                "author": author,
                "publish_date": publish_date,
                "tags": tags,
                "content": content,
                "scraped_at": datetime.utcnow().isoformat()
            }
            articles.append(article)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    # Save to JSON
    with open("articles.json", "w", encoding="utf-8") as jf:
        json.dump(articles, jf, indent=4, ensure_ascii=False)

    # Save to CSV
    with open("articles.csv", "w", encoding="utf-8", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=["url", "title", "author", "publish_date", "tags", "content", "scraped_at"])
        writer.writeheader()
        for article in articles:
            writer.writerow(article)

    print(f"Saved {len(articles)} articles to JSON and CSV.")
    driver.quit()


if __name__ == "__main__":
    scrape_articles()
