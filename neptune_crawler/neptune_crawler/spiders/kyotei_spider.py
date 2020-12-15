import scrapy

# item class included here
class RaceItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    race_title = scrapy.Field()
    race_place = scrapy.Field()
    race_name = scrapy.Field()
    first_place_name = scrapy.Field()
    first_place_age = scrapy.Field()
    first_place_lane = scrapy.Field()
    first_place_rank = scrapy.Field()
    first_place_motor = scrapy.Field()
    first_place_boat = scrapy.Field()
    first_place_weight = scrapy.Field()
    first_place_height = scrapy.Field()
    second_place_name = scrapy.Field()
    second_place_age = scrapy.Field()
    second_place_lane = scrapy.Field()
    second_place_rank = scrapy.Field()
    second_place_motor = scrapy.Field()
    second_place_boat = scrapy.Field()
    second_place_weight = scrapy.Field()
    second_place_height = scrapy.Field()
    third_place_name = scrapy.Field()
    third_place_name = scrapy.Field()
    third_place_age = scrapy.Field()
    third_place_lane = scrapy.Field()
    third_place_rank = scrapy.Field()
    third_place_motor = scrapy.Field()
    third_place_boat = scrapy.Field()
    third_place_weight = scrapy.Field()
    third_place_height = scrapy.Field()
    fourth_place_name = scrapy.Field()
    fourth_place_name = scrapy.Field()
    fourth_place_name = scrapy.Field()
    fourth_place_age = scrapy.Field()
    fourth_place_lane = scrapy.Field()
    fourth_place_rank = scrapy.Field()
    fourth_place_motor = scrapy.Field()
    fourth_place_boat = scrapy.Field()
    fourth_place_weight = scrapy.Field()
    fourth_place_height = scrapy.Field()
    fifth_place_name = scrapy.Field()
    fifth_place_name = scrapy.Field()
    fifth_place_name = scrapy.Field()
    fifth_place_age = scrapy.Field()
    fifth_place_lane = scrapy.Field()
    fifth_place_rank = scrapy.Field()
    fifth_place_motor = scrapy.Field()
    fifth_place_boat = scrapy.Field()
    fifth_place_weight = scrapy.Field()
    fifth_place_height = scrapy.Field()
    sixth_place_name = scrapy.Field()
    sixth_place_name = scrapy.Field()
    sixth_place_name = scrapy.Field()
    sixth_place_age = scrapy.Field()
    sixth_place_lane = scrapy.Field()
    sixth_place_rank = scrapy.Field()
    sixth_place_motor = scrapy.Field()
    sixth_place_boat = scrapy.Field()
    sixth_place_weight = scrapy.Field()
    sixth_place_height = scrapy.Field()


class KyoteiSpider(scrapy.Spider):
    name = "kyotei"

    def start_requests(self):

        for arena in range(1,30):
            arena = "{0:0=2d}".format(arena)
            for race_number in range(1,12):
                url = 'https://race.kyotei.club/info/info-20201212-{1}-{0}.html'.format(race_number, arena)
                yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]

        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        item = RaceItem()

        item["link"] = response.url
        item["race_title"] = response.xpath('//*[@id="mainHead"]/div[1]/div/table//tr/td[3]/text()').extract()
        item["race_place"] = response.xpath('//*[@id="infoStdm"]/option[@selected="selected"]/text()').extract()
        item["race_name"] = response.xpath('//*[@id="infoStdm"]/option[@selected="selected"]/text()').extract()

        item["first_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[1]/a/span/text()').extract()
        item["first_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[1]/span/text()').extract()
        item["first_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[2]/div/div/div/text()').extract()
        item["first_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[2]/table//tr[1]/td/div/span/text()').extract()
        item["first_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[2]/div[3]/text()').extract()
        item["first_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[2]/div[3]/text()').extract()
        item["first_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[4]/text()').extract()
        item["first_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[3]/text()').extract()

        item["second_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[1]/a/span/text()').extract()
        item["second_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[1]/span/text()').extract()
        item["second_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[3]/div/div/div/text()').extract()
        item["second_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[3]/table//tr[1]/td/div/span/text()').extract()
        item["second_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[3]/div[3]/text()').extract()
        item["second_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[3]/div[3]/text()').extract()
        item["second_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[4]/text()').extract()
        item["second_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[3]/text()').extract()

        item["third_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[1]/a/span/text()').extract()
        item["third_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[1]/span/text()').extract()
        item["third_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[4]/div/div/div/text()').extract()
        item["third_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[4]/table//tr[1]/td/div/span/text()').extract()
        item["third_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[4]/div[3]/text()').extract()
        item["third_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[4]/div[3]/text()').extract()
        item["third_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[4]/text()').extract()
        item["third_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[3]/text()').extract()

        item["fourth_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/a/span/text()').extract()
        item["fourth_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/span/text()').extract()
        item["fourth_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[5]/div/div/div/text()').extract()
        item["fourth_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[5]/table//tr[1]/td/div/span/text()').extract()
        item["fourth_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[5]/div[3]/text()').extract()
        item["fourth_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[5]/div[3]/text()').extract()
        item["fourth_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[4]/text()').extract()
        item["fourth_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[3]/text()').extract()

        item["fifth_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[1]/a/span/text()').extract()
        item["fifth_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[1]/span/text()').extract()
        item["fifth_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[6]/div/div/div/text()').extract()
        item["fifth_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[6]/table//tr[1]/td/div/span/text()').extract()
        item["fifth_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[6]/div[3]/text()').extract()
        item["fifth_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[6]/div[3]/text()').extract()
        item["fifth_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[4]/text()').extract()
        item["fifth_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[3]/text()').extract()

        item["sixth_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[1]/a/span/text()').extract()
        item["sixth_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/span/text()').extract()
        item["sixth_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[7]/div/div/div/text()').extract()
        item["sixth_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[7]/table//tr[1]/td/div/span/text()').extract()
        item["sixth_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[7]/div[3]/text()').extract()
        item["sixth_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[7]/div[3]/text()').extract()
        item["sixth_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[4]/text()').extract()
        item["sixth_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[3]/text()').extract()

        yield item
