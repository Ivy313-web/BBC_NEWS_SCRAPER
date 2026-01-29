# https://www.bbc.co.uk/search?q=f&d=NEWS_PS&page=29
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from BBC_saving_method import excel_method, csv_method

data = {}
while True:
    keyword = input('Please enter the keyword:').replace(' ', '+').replace(',', '%2C').replace('/', '%2F')
    driver = webdriver.Chrome()
    driver.get(f'https://www.bbc.co.uk/search?q={keyword}&d=NEWS_PS')
    try:
        test = driver.find_element(By.CSS_SELECTOR, 'div.ssrcss-ymtzkm-Stack.e1y4nx260')
        print('No information found, please enter the correct word')
        driver.quit()
        continue
    except:
        mn = driver.find_elements(By.CSS_SELECTOR,'li.ssrcss-hp3otd-StyledListItem-PageButtonListItem.e1ksme8n1 div.ssrcss-3vkeha-StyledButtonContent.e1kcrsdk1')
        max_num = mn[-1].text
        print(f'Total page:{max_num} pages')
        driver.quit()
        while True:
            page_num = input('Please enter the page number:')
            if page_num.isdigit() and int(page_num) <= int(max_num):
                driver = webdriver.Chrome()
                for page in range(1, int(page_num) + 1):
                    driver.get(f'https://www.bbc.co.uk/search?q={keyword}&d=NEWS_PS&page={page}')
                    time.sleep(2)
                    details = driver.find_elements(By.CSS_SELECTOR, 'div.ssrcss-k49uhy-PromoContent.exn3ah912')
                    list = []
                    for detail in details:
                        try:
                            titles = detail.find_elements(By.CSS_SELECTOR,
                                                          'p.ssrcss-1b1mki6-PromoHeadline.exn3ah99>span')
                            if len(titles) > 1 and 'watch now' in titles[0].text:
                                title = 'Video content--' + titles[1].text
                            elif len(titles) > 1 and 'listen now' in titles[0].text:
                                title = 'Voice content--' + titles[1].text
                            else:
                                title = titles[0].text
                            link = detail.find_element(By.TAG_NAME, 'a').get_attribute('href')
                            list.append({
                                'title': title,
                                'link': link
                            })
                        except Exception as e:
                            title = 'no title information'
                            link = 'no link information'
                        print(title, link)
                    data[page] = list
                    print(f'{page} page is done')
                break
            else:
                print('Please enter a valid page number.')
        save = input('Do you want to save these data? Y/N: ')
        if save.lower() == 'y':
            save_method = input('Please select your saving method(csv/excel): ')
            while True:
                if save_method.lower() == 'csv':
                    csv_method(keyword, data)
                    break
                elif save_method.lower() == 'excel':
                    excel_method(keyword, data)
                    break
                else:
                    print('Please select a valid saving method.')
            break
        else:
            print('Thank you for your using!')
            break