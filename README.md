Note : this project is scraping a specific website's page content.

# Setup

Reconfigure the postgres connection of this project with your given postgres username and password in contentscrape.pipeline.py file and write the following code in the terminal

```
scrapy crawl hotelinfo
```

<!-- sudo -i -u postgres -->
<!-- psql -->

# Tasks

- [x] Finish creating a class naminmg, hotels_content in test database
- [x] Able to store direct from code to postgres
- [x] Drops table if exist, Create table if it doesn't exist then insert.
- [x] Update Readme file for setting it up.
- [x] Able to store price value as integer by handling (',','$', '+')
- [ ] Adding requirements.txt
- [ ] Which all can be fetched
- [ ] add images as evidence

# Problems and solution

- [x] (how to connect python scrapyt with postgres)[https://medium.com/codelog/store-scrapy-crawled-data-in-postgressql-2da9e62ae272]
- [x] postgres error. Possiblity of varibales assigned before or having a null value but table created as no null for that value
