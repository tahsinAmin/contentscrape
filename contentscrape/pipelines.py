# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import psycopg2


class ContentscrapePipeline(object):
    #update username and password here
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres' 
        password = 'password'
        database = 'test'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
        self.cur.execute("DROP TABLE IF EXISTS hotels_content")
        self.cur.execute("CREATE TABLE IF NOT EXISTS hotels_content (id SERIAL PRIMARY KEY,title VARCHAR NOT NULL,price int NOT NULL,review VARCHAR NOT NULL,location VARCHAR,amenities VARCHAR NOT NULL,image_link VARCHAR NOT NULL)")

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into hotels_content(title,price,review,location, amenities,image_link) values(%s,%s,%s,%s,%s,%s)",(item['title'],item['price'],item['review'],item['location'],item['amenities'],item['image_link']))
        self.connection.commit()
        return item



# select * from hotels_content;
# insert into hotels_content(title,price,review,location, amenities,image_link) values('Tahsin Villa',12000,'6.0 Good','Mirpur DOHS','reading books, play basketball, hard working','https://avatars.githubusercontent.com/u/29802879?s=400&u=e54e15a6d5fcb8056caf052cad4c4275d8eec863&v=4');

