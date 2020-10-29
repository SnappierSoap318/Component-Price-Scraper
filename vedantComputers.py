from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def vedantComputers(component):
    searchUrl = 'https://www.vedantcomputers.com/index.php?route=product/search&search='
    final_list = {}
    for i in range(len(component)):
        if component[i] == ' ':
            searchUrl += '%20'
        else:
            searchUrl += component[i]
    searchUrl += '&description=true&fq=1'

    # Try to connect to the server, 
    try:
        request = Request(searchUrl, headers={'User-Agent': 'Mozilla/5.0'})
        searchResult = urlopen(request).read()
    except:
        print('Site unreachable')   
    soup = BeautifulSoup(searchResult, 'html.parser')

    # check the availablility of product
    check_avail = soup.find("div", class_ = 'main-products-wrapper')
    if  check_avail.text == 'There is no product that matches the search criteria.':
        with open('price_list.txt', 'a') as file:
            file.write('This product does isnt available at Vedant Computers')
    else:
        product_list = soup.findAll("div", class_ = "product-layout")
        for product in product_list:
            if(product.find('span', class_ = "price-normal")):
                Product_price = product.find('span', class_ = "price-normal")
            else:
                Product_price = product.find('span', class_ = "price-new")
            Product_name = product.find('div', class_ = "name")
            if component in Product_name.text:
                final_list[Product_name.text] = Product_price.text
    with open('price_list.txt', 'a',encoding= 'utf-8') as file:
        for key, value in final_list.items():
            file.write(key + ': ' + value + '\n')


