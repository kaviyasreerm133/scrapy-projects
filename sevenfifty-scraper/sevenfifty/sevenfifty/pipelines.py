import hashlib
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class DuplicatesPipeline:
    def __init__(self):
        self.seen_urls = set()
        self.seen_hashes = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('url') in self.seen_urls:
            raise DropItem(f"Duplicate URL: {adapter['url']}")

        content_hash = adapter.get('content_hash')
        if content_hash in self.seen_hashes:
            raise DropItem(f"Duplicate content: {adapter['url']}")

        self.seen_urls.add(adapter['url'])
        self.seen_hashes.add(content_hash)
        return item

class ValidationPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if not adapter.get('title'):
            raise DropItem(f"Missing title: {adapter['url']}")
        if not adapter.get('content') or len(adapter.get('content')) < 100:
            raise DropItem(f"Insufficient content: {adapter['url']}")
        return item
