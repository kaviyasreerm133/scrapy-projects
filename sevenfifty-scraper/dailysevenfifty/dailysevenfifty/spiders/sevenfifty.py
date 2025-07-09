import scrapy
from bs4 import BeautifulSoup
from datetime import datetime
import hashlib

class SevenFiftyDailySpider(scrapy.Spider):
    name = "sevenfiftydaily"
    allowed_domains = ["daily.sevenfifty.com"]
    start_urls = ["https://daily.sevenfifty.com/"]

    def parse(self, response):
        article_links = response.css("h2 a::attr(href)").getall()
        self.logger.info(f"Found {len(article_links)} article links on {response.url}")
    
        for link in article_links:
            yield response.follow(link, callback=self.parse_article)

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            self.logger.info(f"Found next page: {next_page}")
            yield response.follow(next_page, callback=self.parse)
    
    def parse_article(self, response):
        title = response.css("h1::text").get()
        author = response.css("span.author-name::text").get(default="SevenFifty Daily Editors").strip()
        publish_date = response.css("meta[property='article:published_time']::attr(content)").get()
        tags = response.css("a[rel='category tag']::text").getall()
        content = " ".join(response.css("div.article-content-wrapper p::text").getall())

        yield {
            "url": response.url,
            "title": title,
            "author": author,
            "publish_date": publish_date,
            "tags": tags,
            "content": content,
            "scraped_at": datetime.utcnow().isoformat()
        }
