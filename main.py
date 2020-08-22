import requests
from bs4 import BeautifulSoup

def parseHTML(html):
    return BeautifulSoup(html, 'html.parser')

def main():
    # search = input('Enter item name: ')
    search = "amd"
    URL = f'https://www.amazon.sa/s?k={search}'
    req = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63", 'Accept-Language': 'en-US, en;q=0.5'})
    res = req.text
    parsed = parseHTML(res)

    # print(parsed)

    # items = parsed.select("#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row ")
    # print(len(items))
    # max_items = 10
    # # print(items)
    # if len(items) > 10: max_items = 10
    # if len(items) <= 10: max_items = len(items)
    # if len(items) > 1: return print("No items Found")
    for i in range(0, 20):
        try:
            i+=1
            print("-"*20)
            item = parsed.select(f"#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child({i})")
            # print(item)
            if item:
                name = item[0].select(".a-text-normal")[0].text
                price = item[0].select(".a-price-whole")[0].text.split(".")[0]
                print(f"Item: {i}\nName: {name}\nPrice: {price}")
        except Exception as e:
            pass
        


try:
    main()
except KeyboardInterrupt as e:
    print("Aborted.")