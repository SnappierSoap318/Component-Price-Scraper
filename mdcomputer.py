from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
def mdComputers(component):
    searchUrl = 'https://mdcomputers.in/index.php?category_id=0&search='
    final_list = {}
    for i in range(len(component)):
        if component[i] == ' ':
            searchUrl += '+'
        else:
            searchUrl += component[i]
    searchUrl += '&submit_search=&route=product%2Fsearch'
    try:
        request = Request(searchUrl, headers={'User-Agent': 'Mozilla/5.0'})
        searchResult = urlopen(request).read()
    except:
        print('Site unreachable')   
    soup = BeautifulSoup(searchResult, 'html.parser')
    product_list = soup.findAll('div', class_ = 'product-layout')
    for product in product_list:
        if(product.find('span', class_ = "price-normal")):
            Product_price = product.find('span', class_ = "price-normal")
        else:
            Product_price = product.find('span', class_ = "price-new")
        Product_name = product.find('a')['title']
        if component in Product_name:
            final_list[Product_name] = Product_price.text
    with open('price_list.txt', 'a',encoding= 'utf-8') as file:
        for key,value in final_list.items():
            file.write(key + ': ' + value + '\n')
    file.close()