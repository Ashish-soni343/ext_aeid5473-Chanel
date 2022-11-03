import json
import scrapy
from ..items import ChanelItem
from datetime import datetime

custom_settings = {
    'LOG_LEVEL': 'INFO',
    'RETRY_ENABLED': 'False',
    'DOWNLOAD_TIMEOUT': '99999999',
    'REDIRECT_ENABLED': 'False',
    'DNS_RESOLVER': 'scrapy.resolver.CachingThreadedResolver',
    'DUPEFILTER_CLASS': "scrapy.dupefilters.BaseDupeFilter",
    'AUTOTHROTTLE_ENABLED': 'False'
}


class ChanelUaeSpider(scrapy.Spider):       # Starting our spider with a class which contains url to initiate crawling
    name = 'chanel_uae'
    site = 'https://www.chanel.com'

    start_urls = ['https://www.chanel.com/ae/']
    frag_url = 'https://www.chanel.com/ae/fragrance/women/c/7x1x1/page-'
    frag_m_url = 'https://www.chanel.com/ae/fragrance/men/c/7x1x2/page-'
    eyegls_url = 'https://www.chanel.com/ae/eyewear/eyeglasses/c/2x1x2/page-'
    sungls_url = 'https://www.chanel.com/ae/eyewear/sunglasses/c/2x1x1/page-'
    watch_url = 'https://www.chanel.com/ae/watches/collection/c/4x2/page-'
    fine_jewellery = 'https://www.chanel.com/ae/fine-jewelry/collection/c/3x2/page-'
    face_url = 'https://www.chanel.com/ae/makeup/complexion/c/5x1x6/page-'
    eye_url = 'https://www.chanel.com/ae/makeup/eyes/c/5x1x4/page-'
    lips_url = 'https://www.chanel.com/ae/makeup/lips/c/5x1x1/page-'
    nails_url = 'https://www.chanel.com/ae/makeup/nails/c/5x1x7/page-'
    brushes_url = 'https://www.chanel.com/ae/makeup/brushes-and-accessories/c/5x1x3/page-'
    skin_care = 'https://www.chanel.com/ae/skincare/category/c/6x1/page-'
    skin_line_url = 'https://www.chanel.com/ae/skincare/collection/c/6x2/page-'
    frag_bb_url = 'https://www.chanel.com/ae/fragrance/bath-and-body/c/7x1x7/page-'

    nxp = []
    feed_code = 'aeid5473'
    record_create_by = 'aeid5473_chanel'
    record_create_date = datetime.now()
    source_country = 'UAE'
    for i in range(15):
        nxp.append(1)

    def parse(self, response):  # Getting the links from selector and filtering the required urls
        for link in response.css('ul.header__category__links a::attr(href)'):
            a = link.get()
            if a == '/ae/eyewear/sunglasses/c/2x1x1/':
                page = self.site + '/ae/eyewear/sunglasses/c/2x1x1/'
                next_page = response.follow(url=page, callback=self.sunglass)
                yield next_page

            elif a == '/ae/eyewear/eyeglasses/c/2x1x2/':
                page1 = self.site + '/ae/eyewear/eyeglasses/c/2x1x2/'
                next_page1 = response.follow(url=page1, callback=self.eyeglass)
                yield next_page1

            elif a == '/ae/fragrance/women/c/7x1x1/':
                page2 = self.site + '/ae/fragrance/women/c/7x1x1/'
                yield response.follow(url=page2, callback=self.fragrance)

            elif a == '/ae/watches/collection/c/4x2/':
                page3 = self.site + '/ae/watches/collection/c/4x2/'
                yield response.follow(url=page3, callback=self.watches)

            elif a == '/ae/fine-jewelry/collection/c/3x2/':
                page4 = self.site + '/ae/fine-jewelry/collection/c/3x2/'
                yield response.follow(url=page4, callback=self.fine_jwlry)

            elif a == '/ae/makeup/complexion/c/5x1x6/':
                page5 = self.site + '/ae/makeup/complexion/c/5x1x6/'
                yield response.follow(url=page5, callback=self.mkp_face)

            elif a == '/ae/makeup/eyes/c/5x1x4/':
                page6 = self.site + '/ae/makeup/eyes/c/5x1x4/'
                yield response.follow(url=page6, callback=self.mkp_eye)

            elif a == '/ae/makeup/lips/c/5x1x1/':
                page7 = self.site + '/ae/makeup/lips/c/5x1x1/'
                yield response.follow(url=page7, callback=self.mkp_lips)

            elif a == '/ae/makeup/nails/c/5x1x7/':
                page8 = self.site + '/ae/makeup/nails/c/5x1x7/'
                yield response.follow(url=page8, callback=self.mkp_nails)

            elif a == '/ae/makeup/brushes-and-accessories/c/5x1x3/':
                page9 = self.site + '/ae/makeup/brushes-and-accessories/c/5x1x3/'
                yield response.follow(url=page9, callback=self.mkp_brushes)

            elif a == '/ae/fashion/ready-to-wear/':
                page10 = self.site + '/ae/fashion/ready-to-wear/'
                yield response.follow(page10, callback=self.parse_page)

            elif a == '/ae/skincare/category/c/6x1/':
                page11 = self.site + '/ae/skincare/category/c/6x1/'
                yield response.follow(page11, callback=self.skin)

            elif a == '/ae/skincare/collection/c/6x2/':
                page12 = self.site + '/ae/skincare/collection/c/6x2/'
                yield response.follow(page12, callback=self.skin_line)

            elif a == '/ae/fragrance/men/c/7x1x2/':
                page13 = self.site + '/ae/fragrance/men/c/7x1x2/'
                yield response.follow(url=page13, callback=self.frag_m)

            elif a == '/ae/fragrance/bath-and-body/c/7x1x7/':
                page14 = self.site + '/ae/fragrance/bath-and-body/c/7x1x7/'
                yield response.follow(url=page14, callback=self.frag_bb)
            else:
                pass

    def sunglass(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.sungls_url + str(self.nxp[0] + 1) + '/')
        self.nxp[0] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE sunglass")
            yield response.follow(url=next_page, callback=self.sunglass)

    def eyeglass(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.eyegls_url + str(self.nxp[1] + 1) + '/')
        self.nxp[1] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE eyeglass")
            yield response.follow(url=next_page, callback=self.eyeglass)

    def fragrance(self, response):  # Crawling products category individually
        if response.status == 301:
            self.ur.append(response)
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.frag_url + str(self.nxp[2] + 1) + '/')
        self.nxp[2] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE fragrance")
            yield response.follow(url=next_page, callback=self.fragrance)

    def watches(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.watch_url + str(self.nxp[3] + 1) + '/')
        self.nxp[3] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE watches")
            yield response.follow(url=next_page, callback=self.watches)

    def fine_jwlry(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.fine_jewellery + str(self.nxp[4] + 1) + '/')
        self.nxp[4] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE fine_jwlry")
            yield response.follow(url=next_page, callback=self.fine_jwlry)

    def mkp_face(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.face_url + str(self.nxp[5] + 1) + '/')
        self.nxp[5] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE mkp_face")
            yield response.follow(url=next_page, callback=self.mkp_face)

    def mkp_eye(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.eye_url + str(self.nxp[6] + 1) + '/')
        self.nxp[6] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE mkp_eye")
            yield response.follow(url=next_page, callback=self.mkp_eye)

    def mkp_lips(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.lips_url + str(self.nxp[7] + 1) + '/')
        self.nxp[7] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE mkp_lips")
            yield response.follow(url=next_page, callback=self.mkp_lips)

    def mkp_nails(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.nails_url + str(self.nxp[8] + 1) + '/')
        self.nxp[8] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE mkp_nails")
            yield response.follow(url=next_page, callback=self.mkp_nails)

    def mkp_brushes(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.nails_url + str(self.nxp[9] + 1) + '/')
        self.nxp[9] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE mkp_brushes")
            yield response.follow(url=next_page, callback=self.mkp_brushes)

    def skin(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.skin_care + str(self.nxp[10] + 1) + '/')
        self.nxp[10] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE skin")
            yield response.follow(url=next_page, callback=self.skin)

    def skin_line(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.skin_line_url + str(self.nxp[11] + 1) + '/')
        self.nxp[11] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE skin_line")
            yield response.follow(url=next_page, callback=self.skin_line)

    def frag_m(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.frag_m_url + str(self.nxp[12] + 1) + '/')
        self.nxp[12] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE frag_m")
            yield response.follow(url=next_page, callback=self.frag_m)

    def frag_bb(self, response):  # Crawling products category individually
        links = response.css('.txt-product a::attr(href)')
        for link in links:
            full_link = self.site + link.get()
            yield response.follow(url=full_link, callback=self.scrape)

        next_page = (self.frag_bb_url + str(self.nxp[13] + 1) + '/')
        self.nxp[13] += 1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE frag_bb")
            yield response.follow(url=next_page, callback=self.frag_bb)

    def parse_page(self, response):  # For fashion category using multiple function to access more than one pages
        if response.css('p.fs-quick-catalog-access__simple-entry-wrapper a::attr(href)'):
            a = response.css('p.fs-quick-catalog-access__simple-entry-wrapper a::attr(href)').get()
            b = self.site + a
            yield response.follow(b, callback=self.parse_products)
        else:
            pass

    def parse_products(self, response):  # Accessing the page to find products
        if response.css('ol.look-grid a::attr(href)'):
            for links in response.css('ol.look-grid a::attr(href)'):
                full_link = self.site + links.get()
                yield response.follow(full_link, callback=self.parse_categories)
        else:
            pass

    def parse_categories(self, response):  # Getting url to finally crawl products
        if response.css('a.fs-lookdetails__products-block__link::attr(href)'):
            for link_a in response.css('a.fs-lookdetails__products-block__link::attr(href)'):
                full_link = self.site + link_a.get()
                yield response.follow(full_link, callback=self.scrape)
        else:
            pass

    def scrape(self, response):  # Crawling products
        items = ChanelItem()
        if response.css('ul.form-buttons'):
            items['Availability'] = 'InStock'
        else:
            items['Availability'] = 'OutofStock'

        items['Site'] = self.site
        items['Execution_Id'] = ''
        items['Feed_Code'] = self.feed_code
        items['Record_Create_By'] = self.record_create_by
        items['Record_Create_Date'] = self.record_create_date
        items['Source_Country'] = self.source_country

        items['Source'] = response.url
        data = response.xpath('//script[@type="application/ld+json"]/text()').getall()
        data0 = data[0]
        if 'sku' in data0:
            data0 = data0.replace('\n', '')
            data0 = json.loads(data0)
            try:
                items['name'] = data0['name']
            except:
                items['name'] = ''
            try:
                items['color'] = data0['color']
            except:
                items['color'] = ''
            try:
                items['material'] = data0['material']
            except:
                items['material'] = ''
            try:
                items['description'] = data0['description']
            except:
                items['description'] = ''
            try:
                items['product_id'] = data0['sku']
            except:
                items['product_id'] = ''
            data1 = data[1]
            data1 = json.loads(data1)
            try:
                items['Context_Identifier'] = data1['itemListElement'][2]['item']['@id']
            except:
                items['Context_Identifier'] = ''
            if response.css('.js-dimension::text').get():
                items['size'] = response.css('.js-dimension::text').get()
            else:
                try:
                    response.css('span.dropdown_size_text::text')
                    lst = []
                    str1 = ','
                    for sizes in response.css('span.dropdown_size_text::text').getall():
                        lst.append(sizes)
                    str_1 = str1.join(lst)
                    items['size'] = str_1

                except:
                    items['size'] = ''
            if response.css('.product-details__price::text'):
                items['price'] = response.css('.product-details__price::text').get().strip()
            else:
                items['price'] = ""
            yield items

        else:
            data_1 = data[0]
            data_1 = json.loads(data_1)
            try:
                items['Context_Identifier'] = data_1['itemListElement'][2]['item']['@id']
            except:
                items['Context_Identifier'] = ''
            if response.css('.product-details__title::text').get():
                items['name'] = response.css('.product-details__title::text').get().strip()
            else:
                items['name'] = ''

            if response.css('.product-details__reference::text'):

                items['product_id'] = response.css('.product-details__reference::text').get().strip().replace('Ref.',
                                                                                                              "")
            else:
                items['product_id'] = ""

            if response.css('.product-details__description::text'):

                items['description'] = response.css('.product-details__description::text').get().strip()
            else:
                items['description'] = ""

            if response.css('.product-details__color::text'):

                items['color'] = response.css('.product-details__color::text').get().strip()
            else:
                items['color'] = ""
            if response.css('.product-details__price::text'):

                items['price'] = response.css('.product-details__price::text').get().strip()
            else:
                items['price'] = ""

            if response.css('.product-details__heel span::text'):
                items['size'] = response.css('.product-details__heel span::text').get().strip()

            elif response.css('.product-details__option p::text'):
                items['size'] = response.css('.product-details__option p::text').get().strip()
            elif response.css('span.dropdown_size_text::text'):
                lst = []
                str1 = ','
                for sizes in response.css('span.dropdown_size_text::text').getall():
                    lst.append(sizes)
                str_1 = str1.join(lst)
                items['size'] = str_1
            else:
                items['size'] = ""
            if response.css('#characteristic-watches li:nth-child(1) p::text'):
                list1 = []
                strng = ','
                for material in response.css('#characteristic-watches li:nth-child(1) p::text').getall():
                    list1.append(material)
                str_lst = strng.join(list1)
                items['material'] = str_lst
            else:
                items['material'] = ''

            yield items
