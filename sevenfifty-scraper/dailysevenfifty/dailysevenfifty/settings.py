BOT_NAME = "dailysevenfifty"

SPIDER_MODULES = ["dailysevenfifty.spiders"]
NEWSPIDER_MODULE = "dailysevenfifty.spiders"

USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS_PER_DOMAIN = 1

EXTENSIONS = {
    "scrapy.extensions.telnet.TelnetConsole": None,
}

ITEM_PIPELINES = {
    "dailysevenfifty.pipelines.DuplicatesPipeline": 300,
    "dailysevenfifty.pipelines.ValidationPipeline": 400,
}

FEEDS = {
    "articles.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "fields": ["url", "title", "content", "author", "publish_date", "tags", "scraped_at"]
    },
    "articles.csv": {
        "format": "csv",
        "encoding": "utf8",
        "store_empty": False,
        "fields": ["url", "title", "content", "author", "publish_date", "tags", "scraped_at"]
    }
}

FEED_EXPORT_ENCODING = "utf-8"
LOG_LEVEL = "INFO"