
# Scrapy Projects – SevenFifty Daily Scraper

The repo explores four different scraping strategies:

### Method 1: Local Scrapy (Static HTML)

- Scrapy spider without JavaScript support.
- Successfully extracted 177 articles during initial runs.
- Now fails to return results due to changes in site behavior or anti-bot mechanisms.

### Method 2: Selenium with Undetected ChromeDriver

- Used `undetected-chromedriver` to bypass bot detection and handle dynamic content.
- Scraped 20 articles in early runs.
- Currently fails due to detection or content changes.

### Method 3: Scrapy Cloud Deployment

- Deployed the Scrapy spider to Scrapy Cloud (Zyte).
- Failed due to Incapsula bot protection showing JS challenges instead of actual content.

### Method 4: Local Scrapy with Splash

- Introduced JavaScript rendering using Splash (via Docker).
- Faced issues like race conditions and incomplete page rendering.
- A fix using Splash Lua scripts was identified but not implemented due to complexity.

---

## 📂 Folders

- `dailysevenfifty/` – Traditional Scrapy spider (Method 1)
- `sevenfifty1/` – Selenium-based scraping (Method 2)
- `sevenfifty-scraper/` – Configured for Scrapy Cloud (Method 3, 4)

---
