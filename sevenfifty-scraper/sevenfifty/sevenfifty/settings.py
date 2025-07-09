BOT_NAME = 'sevenfifty'

SPIDER_MODULES = ['sevenfifty.spiders']
NEWSPIDER_MODULE = 'sevenfifty.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Polite crawling settings
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = 0.5

CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1

USER_AGENT = 'dailysevenfifty (+http://www.yourdomain.com)'

# (Optional) Disable Telnet console
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

# Logging level
LOG_LEVEL = 'INFO'

# Pipelines (you’ll create these in Step 5)
ITEM_PIPELINES = {
    'sevenfifty.pipelines.DuplicatesPipeline': 300,
    'sevenfifty.pipelines.ValidationPipeline': 400,
}


# # Scrapy settings for sevenfifty project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     https://docs.scrapy.org/en/latest/topics/settings.html
# #     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# #     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# BOT_NAME = "sevenfifty"

# SPIDER_MODULES = ["sevenfifty.spiders"]
# NEWSPIDER_MODULE = "sevenfifty.spiders"

# ADDONS = {}


# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = "sevenfifty (+http://www.yourdomain.com)"

# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# # Concurrency and throttling settings
# #CONCURRENT_REQUESTS = 16
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# DOWNLOAD_DELAY = 1

# # Disable cookies (enabled by default)
# #COOKIES_ENABLED = False

# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False

# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# #    "Accept-Language": "en",
# #}

# # Enable or disable spider middlewares
# # See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    "sevenfifty.middlewares.SevenfiftySpiderMiddleware": 543,
# #}

# # Enable or disable downloader middlewares
# # See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# #DOWNLOADER_MIDDLEWARES = {
# #    "sevenfifty.middlewares.SevenfiftyDownloaderMiddleware": 543,
# #}

# # Enable or disable extensions
# # See https://docs.scrapy.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    "scrapy.extensions.telnet.TelnetConsole": None,
# #}

# # Configure item pipelines
# # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# #ITEM_PIPELINES = {
# #    "sevenfifty.pipelines.SevenfiftyPipeline": 300,
# #}

# # Enable and configure the AutoThrottle extension (disabled by default)
# # See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# #AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# #AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# #AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# #AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False

# # Enable and configure HTTP caching (disabled by default)
# # See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = "httpcache"
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
