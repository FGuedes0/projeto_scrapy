import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css("div.ui-search-result__content")
        
        for product in products :
           
           prices = product.css("span.andes-money-amount__fraction::text").getall()
           
           yield {
            "brand": product.css("span.ui-search-item__brand-discoverability.ui-search-item__group__element::text").get(),
            "name": product.css("h2.ui-search-item__title::text").get(),
            "old_price": prices[0] if len(prices) > 2 else None,
            "new_price": prices[1] if len(prices) > 2 else prices[0] if len(prices) <= 2 else None,
            "reviews_rating_number": product.css("span.ui-search-reviews__rating-number::text").get(),
            "reviews_amount": product.css("span.ui-search-reviews__amount::text").get()
           }