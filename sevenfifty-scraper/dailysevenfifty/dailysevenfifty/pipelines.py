# dailysevenfifty/pipelines.py

from scrapy.exceptions import DropItem
import logging

class DuplicatesPipeline:
    def __init__(self):
        self.seen_hashes = set()

    def process_item(self, item, spider):
        content_hash = item.get("content_hash")
        if content_hash in self.seen_hashes:
            spider.logger.warning(f"Duplicate article dropped: {item.get('url')}")
            raise DropItem(f"Duplicate article found: {item.get('url')}")
        self.seen_hashes.add(content_hash)
        return item


class ValidationPipeline:
    def process_item(self, item, spider):
        missing = []
        for field in ["title", "content", "url"]:
            if not item.get(field):
                missing.append(field)

        if missing:
            spider.logger.warning(f"Dropping item missing fields: {missing} — URL: {item.get('url')}")
            raise DropItem(f"Missing fields {missing} in {item.get('url')}")
        
        return item
