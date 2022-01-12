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
- [x] Works for other hotel travel plans with url, ".ksp"
- [x] Able to store price value as integer by handling (',','$', '+')
- [x] Use othger python-db projects's readme here
- [x] Adding requirements.txt
- [ ] add images as evidence

# What I Learned

- [x] About "with" clause. 1. A "with" clause will take care of closing the cursor for you. 2. We don't need to mention about connection.commit after our sql manipulation, wit clause will take of it as soon as our with clause of database connection is over, it'll comit the transaction automatic. Once we're done, It closes the cursor as well however, it doesn't close the connection of our database. so, tha needs to be done manually.

# Problems and solution

- [x] (how to connect python scrapyt with postgres)[https://medium.com/codelog/store-scrapy-crawled-data-in-postgressql-2da9e62ae272]
- [x] postgres error. Possiblity of varibales assigned before or having a null value but table created as no null for that value
- [ ] Ho to print in tabular format. Solution maybe = > https://www.delftstack.com/howto/python/data-in-table-format-python/
