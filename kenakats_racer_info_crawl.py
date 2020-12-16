from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome()
browser.set_page_load_timeout(60)

listfin = []
url_number = list(range(2014,5175,1))

for num in url_number:
    url = "https://www.boatrace.jp/owpc/pc/data/racersearch/season?toban={0}".format(num)
    browser.get(url)

    try:
        name = browser.find_element_by_class_name('racer1_bodyName')
        name_t = name.text
        name_t2 = name_t.replace('\u3000\u3000',' ')
        id = browser.find_element_by_tag_name('dd')
        racer_info=[]
        elems_racer_info = browser.find_elements_by_tag_name('dd')
        for a in elems_racer_info:
            t = a.text
            racer_info.append(t)
        racer_info_detail =[]
        elems_racer_info_d = browser.find_element_by_class_name('table1').find_elements_by_tag_name('td')
        for a in elems_racer_info_d:
            t = a.text
            racer_info_detail.append(t)
        racer_info_list = racer_info + racer_info_detail
        racer_info_list.append(name_t2)
        listfin.append(racer_info_list)
    except NoSuchElementException:
        pass
browser.close()
df = pd.DataFrame(listfin)
df.to_csv('racer_info.csv', encoding = 'utf_8_sig')
