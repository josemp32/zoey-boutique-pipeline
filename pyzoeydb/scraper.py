import os
import json
import time
import datetime

import requests
import BeautifulSoup

from models import create_item

inventoryProductURLArray = []
inventoryProductList = []
catset = set()


def save_inventory_urls_to_file(the_list, output_file="inventoryURLs.txt"):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print st

    url_list = []

    for key, value in the_list.items():
        subcategory = key
        print "======\n\n" + key + "\n\n======"
        page = requests.get(value)
        soup = BeautifulSoup.BeautifulSOAP(page.content)
        data = soup.findAll('div', attrs={"class": "v-product"})

        for div in data:
            links = div.findAll('a')
            for a in links:
                trimmed = subcategory + "#" + a['href']
                trimmed = trimmed.strip() + "\n"
                url_list.append(trimmed)

    urlset = set(url_list)

    f = open(output_file, "a")
    for item in urlset:
        f.write(item)
    f.close()


def initialize_url_data_source(url_file="inventoryURLs.txt"):
    f = open(url_file).read()
    inventoryProductURLArray.extend(f.split('\n'))


def build_product_json_for_firebase(url_file="inventoryURLs.txt"):
    f = open(url_file).read()
    inventoryProductURLArray.extend(f.split('\n'))

    counter = 0

    for url in inventoryProductURLArray:
        if url == '':
            continue

        print url
        time.sleep(0.59)

        final = url.split('#')
        item = create_item()

        page = requests.get(final[1])
        ts = time.time()
        finalCat = final[0].split('-')
        item.category = finalCat[0]

        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        item.date_added = st
        item.path = url

        soup = BeautifulSoup.BeautifulSOAP(page.content)

        baseURL = "https://www.wholesalefashionsquare.com"

        image_tag = soup.find('img', attrs={"itemprop": "image"})
        item.image_url = baseURL + image_tag['src']

        temp = set()
        spans = soup.findAll('a', attrs={"rel": "shadowbox[ProductImages]"})
        for picture in spans:
            print baseURL + picture['href']
            temp.add(baseURL + picture['href'])
        item.alt_images = list(temp)

        name = soup.find('span', attrs={"itemprop": "name"})
        item.full_name = name.text
        item.name = name.text

        price_span = soup.find('span', attrs={"itemprop": "price"})
        item.price = price_span.text

        list_price = soup.find('div', attrs={"class": "product_listprice"})
        item.unit_price = list_price.text

        data = soup.findAll('font', attrs={"class": "text colors_text"})
        package = data[len(data) - 1]
        item.package = package.text

        meta = soup.find('span', attrs={"class": "product_code"})
        item.product_code = meta.text

        description = soup.findAll('br')
        for x in description:
            if x.text != "":
                if x.text.startswith("Related Products"):
                    break
                if x.text.startswith("Product Code"):
                    continue
                if x.text.startswith("Fabric Content:"):
                    item.fabric_content = x.text
                if x.text.startswith("Size Scale:"):
                    item.size_scale = x.text
                if x.text.startswith("Size Ratio:"):
                    item.size_ratio = x.text
                if x.text.startswith("Description:"):
                    item.description = x.text
                if x.text.startswith("Quantity in Stock:"):
                    item.quantity_in_stock = x.text
                if x.text.startswith("Description&nbsp"):
                    item.description_info = x.text

        catset.add(item.category)
        counter += 1
        print counter, '  #################################################'

        incompletJson = item.product_code + '.txt'
        if not os.path.isfile(incompletJson):
            inventoryProductList.append(item.product_code)
            print incompletJson
            f = open(incompletJson, "a")
            f.write("\"" + item.product_code + "\":" + json.dumps(vars(item), sort_keys=True, indent=4))
            f.close()

        completeJson = item.product_code + '.json'
        if not os.path.isfile(completeJson):
            f = open(completeJson, "a")
            f.write(json.dumps(vars(item), sort_keys=True, indent=4))
            f.close()

    catFile = open("categories.txt", "a")
    for x in catset:
        catFile.write(x + "\n")
        print x
    catFile.close()

    productList = open("product_list.txt", "a")
    for x in inventoryProductList:
        if x != "__":
            productList.write(x + "\n")
        print x
    productList.close()
