# sevenfifty_spider.py - FINAL WORKING LOCAL VERSION WITH SPLASH

import scrapy
from scrapy_splash import SplashRequest
from datetime import datetime
import hashlib

class SevenfiftySpider(scrapy.Spider):
    name = 'sevenfifty'
    
    def start_requests(self):
        # This first request is fine.
        yield SplashRequest(
            url='https://daily.sevenfifty.com/',
            callback=self.parse,
            args={'wait': 3}
        )

    # ======================================================================
    # THIS METHOD IS NOW FIXED
    # ======================================================================
    def parse(self, response):
        article_links = response.css('a.post-card__link::attr(href)').getall()
        for link in article_links:
            if link:
                # We now create a new, clean request, explicitly passing
                # the 'splash' meta dictionary to avoid the LookupError.
                yield SplashRequest(
                    url=response.urljoin(link),
                    callback=self.parse_article,
                    meta={
                        'splash': {
                            'args': {'wait': 2},
                            'endpoint': 'render.html',
                        }
                    }
                )

        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            # We do the same fix for the pagination link.
            yield SplashRequest(
                url=response.urljoin(next_page),
                callback=self.parse,
                meta={
                    'splash': {
                        'args': {'wait': 3},
                        'endpoint': 'render.html',
                    }
                }
            )

    # This part of the code was already correct.
    def parse_article(self, response):
        title = response.css('h1.entry-title::text').get()
        if not title:
            title = response.css('h1::text').get()

        content_paragraphs = response.css('.entry-content p::text').getall()
        content = ' '.join(content_paragraphs).strip()

        author = response.css('.author-name::text').get()
        if not author:
            author = response.css('.byline a::text').get()

        publish_date = self.extract_date(response)
        tags = response.css('.tags a::text').getall()

        if title and content:
            yield {
                'url': response.url,
                'title': title.strip(),
                'content': content,
                'author': author.strip() if author else None,
                'publish_date': publish_date,
                'tags': tags,
                'content_hash': hashlib.md5(content.encode()).hexdigest(),
                'scraped_at': datetime.now().isoformat(),
            }

    def extract_date(self, response):
        date_selectors = [
            'time::attr(datetime)',
            '.entry-date::text',
            '.published::text',
            '.date::text'
        ]
        for selector in date_selectors:
            date_text = response.css(selector).get()
            if date_text:
                return date_text.strip()
        return None