# -*- coding: utf-8 -*-
import scrapy
import json
from contentscrape.items import ContentscrapeItem


class HotelinfoSpider(scrapy.Spider):
    name = 'hotelinfo'
    allowed_domains = ['www.kayak.co.in']
    start_urls = ['https://www.kayak.co.in/Hyderabad-Hotels.7297.hotel.ksp/']

    def parse(self, response):
        counter = 1
        # for content in response.css('div.soom'):
        #     print("Inside div")
        #     if counter < 11:
        #         title = content.xpath('div/div/div/a/span/text()').get()
        #         list1 = content.css('span.yRv1-text::text').extract()
        #         list_to_string = ",".join(list1)
        #         image_link = content.xpath('a/img/@src').get()

        #         if image_link is None:
        #             try1 = response.xpath(f"(//script[contains(text(),'{title}')])/text()").getall()
        #             data = json.loads(try1[0])
        #             image_link = data.get('image')

        #             if image_link:
        #                 yield {
        #                     'title': title,
        #                     'image_link': image_link,
        #                     'price': content.css('span.soom-price::text').get(),
        #                     'review': content.xpath('div/div/div/div/span/text()').get(),
        #                     'amenities': list_to_string,
        #                     'location': content.css('span.soom-neighborhood::text').get(),
        #                 }
        #                 counter += 1
        #             else:
        #                 print("Skipped an element")
        #     else:
        #         break


        for content in response.css('div.soom'):
            if counter < 11:
                item_title = content.xpath('div/div/div/a/span/text()').get()
                
                
                item_review = content.xpath('div/div/div/div/span/text()').get()
                item_location = content.css('span.soom-neighborhood::text').get()

                manipulate_price_string = content.css('span.soom-price::text').get()
                item_price = int(manipulate_price_string.split()[1].split('+')[0])
                
                list1 = content.css('span.yRv1-text::text').extract()
                item_amenities = ",".join(list1)

                item_image_link = content.xpath('a/img/@src').get()
                
                if item_image_link is None:
                    try1 = response.xpath(f"(//script[contains(text(),'{item_title}')])/text()").getall()
                    data = json.loads(try1[0])
                    item_image_link = data.get('image')

                if item_image_link:
                    hotelItem = ContentscrapeItem(title= item_title, price=item_price, review=item_review, location=item_location, amenities=item_amenities, image_link=item_image_link)
                    yield hotelItem                       
                    counter += 1
                else:
                    print("Skipped an element")
            else:
                break