# -*- coding: utf-8 -*-
import scrapy
import json
from contentscrape.items import ContentscrapeItem


class HotelinfoSpider(scrapy.Spider):
    name = 'hotelinfo'
    allowed_domains = ['www.kayak.co.in']
    travel_plan = 'Dubai-Hotels.6080.hotel.ksp' #'Hyderabad-Hotels.7297.hotel.ksp'
    start_urls = [f'https://www.kayak.co.in/{travel_plan}/']

    def parse(self, response):
        counter = 1

        for content in response.css('div.soom'):
            if counter < 11:
                item_title = content.xpath('div/div/div/a/span/text()').get()
                
                
                item_review = content.xpath('div/div/div/div/span/text()').get()
                item_location = content.css('span.soom-neighborhood::text').get()

                price_string = content.css('span.soom-price::text').get()
                item_price = int(price_string[2:len(price_string)-1].replace(',',''))


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