import scrapy

class SevenFiftyDailySpider(scrapy.Spider):
    name = "sevenfiftydaily"
    allowed_domains = ["daily.sevenfifty.com"]
    
    start_urls = [
        "https://daily.sevenfifty.com/category/business/",
        "https://daily.sevenfifty.com/category/education/",
        "https://daily.sevenfifty.com/category/tasting-notes/",
        "https://daily.sevenfifty.com/category/trends/",
        "https://daily.sevenfifty.com/category/producer-profiles/"
    ]

    def parse(self, response):
        # Extract article URLs
        for article in response.css("h2.entry-title a::attr(href)"):
            yield response.follow(article.get(), callback=self.parse_article)

        # Follow pagination links
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        title = response.css("h1.entry-title::text").get()
        author = response.css("span.author.vcard a::text").get()
        date = response.css("time.entry-date::attr(datetime)").get()
        content = " ".join(response.css("div.entry-content p::text").getall())

        if title and content:
            yield {
                "url": response.url,
                "title": title.strip(),
                "author": author.strip() if author else None,
                "date": date,
                "content": content.strip()
            }
