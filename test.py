# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import random

def getHTMLText(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'   #模拟浏览器登陆
        headers = {
                   'Accept':'*/*',
                   'Accept-Encoding':'gzip, deflate, br',
                   'Accept-Language':'zh-CN,zh;q=0.8',
                   'Connection':'keep-alive',
                   'User-Agent': user_agent,

                   'Host':'www.evervc.com',
                   'X-Requested-With':'XMLHttpRequest'
                    #Referer:https://www.tianyancha.com/company/32106442

                   }

        #xproxy = Best_Proxys.proxys_get() #从代理池中获取可用的IP

        #proxy=urllib.request.ProxyHandler(xproxy)
        #opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        #urllib.request.install_opener(opener)
        
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)r
        return r.text
    except:
        print('无法正确链接！')

if __name__ == '__main__':
    html = getHTMLText('http://www.evervc.com/startups/85653')
    soup = BeautifulSoup(html,'lxml')
    with open('web.txt','wb') as f:
        f.write(soup.prettify().encode('utf-8'))
    # uu = soup.find_all("a", class_="label label-default")
    # item['name'] = response.xpath('//*[@class="portfolio-user-info"]/h1/text()').extract_first(default='NULL') 

    name = soup.select('div[class="portfolio-user-info"] h1')[0].get_text()
    short_info = soup.select('span[class="text"]')[0].get_text()
    current_status = soup.select('div[class="portfolio-user-tag"]')[0].get_text() 

    tags = soup.select('a[class="label label-default"]')
    tag = []
    for info in tags:
        tag.append(info.get_text())
    
    
    if soup.select('div[class="portfolio-text"]'):
        project_info = soup.select('div[class="portfolio-text"]')[0].get_text().strip()
    else:
        project_info = 'null'

    
    if soup.select('div[class="portfolio-light"]'):
        highlight = soup.select('div[class="portfolio-light"]')[0].get_text().strip()
    else:
        highlight = 'null'

    
    if soup.select('div[class="portfolio-corp"] p'):
        company_info = soup.select('div[class="portfolio-corp"] p')[0].get_text()
    else:
        company_info = 'null'

    invest_num = soup.select('div[class="row text-center amount"] h2')[0].get_text().replace('￥','').replace(',','')

    # similars = soup.select('div[class="media"] a div[class="media-body"] h5')
    index = soup.select('div[class="panel-body portfolio"]')
    similar = []
    for info in similars:
        similar.append(info.get_text())
    
    if soup.select('dl[class="user-contact"] dd span a'):
        website = soup.select('dl[class="user-contact"] dd span a')[0].get_text()
    else:
        website = 'null'

    if soup.select('span[class="user-wx"] dd span'):
        wechat = soup.select('span[class="user-wx"] dd span')[0].get_text()
    else:
        wechat = 'null'

    if soup.select('dl[class="user-contact"] dd span em'):
        detail_location = soup.select('dl[class="user-contact"] dd span em')[0].get_text()
    else:
        detail_location = 'null'
    
    print("name: " + name)
    print("short_info: " + short_info)
    print("tag:")
    print(tag)
    print("project_info: " + project_info)
    print("highlight: " + highlight)
    print("company_info: " + company_info)
    print("invest_num: " + invest_num)
    print("similar:")
    print(similar)
    print("website: " + website)
    print("wechat: " + wechat)
    print("detail_location: " + detail_location)
    
    

        