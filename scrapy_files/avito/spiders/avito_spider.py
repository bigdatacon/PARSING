# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from avito.items import AvitoItem
from scrapy.loader import ItemLoader

class AvitoSpiderSpider(scrapy.Spider):
    name = 'avito_spider'
    allowed_domains = ['avito.ru']
    # start_urls = ['https://www.avito.ru/rossiya/kvartiry']
    start_urls = ['https://www.avito.ru/moskva/transport']

    def parse(self, response: HtmlResponse):
        ads_links = response.xpath('//a[@class="styles-link-36uWZ"]/@href').extract()
        for link in ads_links:
            yield response.follow(link, self.parse_ads)

    def parse_ads(self, response:HtmlResponse):
        # photos = response.xpath('//div[contains(@class, "gallery-img-wrapper")]//div[contains(@class, "gallery-img-frame")]/@data-url').extract()
        # temp = AvitoItem(photos=photos)
        # yield temp
        loader = ItemLoader(item=AvitoItem(), response=response)
        loader.add_xpath('photos',
                         '//div[contains(@class, "gallery-img-wrapper")]//div[contains(@class, "gallery-img-frame")]/@data-url')

        loader.add_css('title', 'h1.title-info-title span.title-info-title-text::text')
        ### ДОБАВЛЯЕМ ОПИСАНИЕ ПАРАМЕТРОВ
        loader.add_css('description', 'div.item-params ul.item-params-list li.item-params-list-item::text span::text')
        # loader.add_xpath('description', 'div.[contains(@class, "item-params")]//ul[contains(@class, "item-params-list")]//li[contains(@class, "item-params-list-item")]/text()')


        yield loader.load_item()

# <div class="styles-root-2nfT7" xpath="1">
# <a data-marker="title" class="styles-link-2BT6y" itemprop="url"
# href="/moskva/avtomobili/bmw_4_seriya_gran_coupe_2018_1501302914"
#
# //div[contains(@class, "styles-root-2nfT7")]//a[contains(@class, "styles-link-2BT6y")]/@href
###ВОТ ссылка для входа через фото
# <a class="styles-link-36uWZ" itemprop="url" href="/moskva/avtomobili/jaguar_xjr_2000_1084670591" target="_self" title="Объявление «Jaguar XJR, 2000»" rel="noopener" xpath="1"><div class="styles-root-1oL-O"><img class="styles-img-1Oovb" itemprop="image" src="//34.img.avito.st/208x156/4961989234.jpg" alt="Jaguar XJR, 2000"></div><div class="styles-root-2fkaY"><i class="styles-icon-1lpY0 styles-images-G07uI">18</i></div></a>
### ССЫЛКИ НА КАРТИНКи

# <div class="gallery-img-frame js-gallery-img-frame" data-url="//34.img.avito.st/640x480/4961989234.jpg" data-title="Jaguar XJR, 2000— фотография №1" xpath="1">
#   <span class="gallery-img-cover" style="background-image: url('//34.img.avito.st/640x480/4961989234.jpg')"></span> <img src="//34.img.avito.st/640x480/4961989234.jpg" alt="Jaguar XJR, 2000— фотография №1">
#   </div>

#### Cсылки на элементы и описание:
# <ul class="item-params-list" xpath="1">
# <ul class="item-params-list" xpath="1">
# <li class="item-params-list-item" xpath="1"> <span class="item-params-label">Модификация: </span>4.0 AT (363 л.с.) </li>
