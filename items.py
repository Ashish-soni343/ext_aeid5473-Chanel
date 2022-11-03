# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from unicodedata import name
import scrapy


class ChanelItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    color = scrapy.Field()
    material = scrapy.Field()
    description = scrapy.Field()
    product_id = scrapy.Field()
    Context_Identifier = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()
    Source = scrapy.Field()
    Execution_Id = scrapy.Field()
    Source_Country = scrapy.Field()
    Record_Create_Date = scrapy.Field()
    Site = scrapy.Field()
    Availability = scrapy.Field()
    Feed_Code = scrapy.Field()
    Record_Create_By = scrapy.Field()
    pass
