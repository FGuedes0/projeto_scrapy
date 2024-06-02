import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css("div.ui-search-result__content")
        

        for product in products :
           yield {
            "brand": product.css("span.ui-search-item__brand-discoverability.ui-search-item__group__element::text").get(),
            "name": product.css("h2.ui-search-item__title::text").get(),
            #"old_price": product.css("andes-money-amount.ui-search-price__partui-search-price__part--small.ui-search-price__original-value.andes-money-amount--previous.andes-money-amount--cents-superscript.andes-money-amount--compact::text").get(),
            #"new_price_": product.css("andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript::text").get(),
            "reviews_rating_number": product.css("span.ui-search-reviews__rating-number::text").get(),
            "reviews_amount": product.css("span.ui-search-reviews__amount::text").get()
           }