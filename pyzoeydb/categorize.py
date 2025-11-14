import json


def create_subcategory_file_list(category_file="categories.txt"):
    catFile = open(category_file).read()
    catArray = []
    catArray.extend(catFile.split('\n'))

    open(category_file, 'w').close()
    catFile = open(category_file, "a")

    for category in catArray:
        s = category
        result = ""
        x = "/"
        y = "_"
        k = " "
        j = ""

        for char in s:
            if char == k:
                result += j
            elif char == x:
                result += y
            else:
                result += char

        print result
        if result != "":
            catFile.write(result + ".txt\n")

    catFile.close()


def create_subcategory_files(category_file="categories.txt"):
    catListFile = open(category_file).read()
    catArray = []
    catArray.extend(catListFile.split('\n'))

    for category in catArray:
        if category.startswith('.txt'):
            continue
        if category == "":
            continue
        if category.startswith('_'):
            continue

        catFile = open(category, "a")
        catName = category.split('.')
        catFile.write("\"" + catName[0] + "\":{" + "\n")
        catFile.close()


def create_cat_lookup_file(product_list_file="product_list.txt",
                           category_list_file="categories.txt",
                           output_file="category_lookup.json"):
    prodCatSet = set()
    prodFile = open(product_list_file).read()
    prodArray = []
    prodArray.extend(prodFile.split('\n'))

    catListFile = open(category_list_file).read()
    catArray = []
    catArray.extend(catListFile.split('\n'))

    for product in prodArray:
        if product == '':
            continue
        productFileName = product + '.json'
        with open(productFileName) as json_data:
            try:
                d = json.load(json_data)
            except (ValueError, KeyError, TypeError):
                print "JSON format error"
                continue
            if d['category'] != '_':
                if d['category'] != ' ':
                    prodCatSet.add(d['category'])

    print len(prodCatSet)
    print len(catArray)

    catFile = open(output_file, "a")
    catFile.write("{\n")
    prodCatArray = list(prodCatSet)

    for i, item in enumerate(prodCatArray):
        if len(prodCatSet) - 1 == i:
            catFile.write("\t\"" + catArray[i] + "\":\"" + catArray[i].split('.txt')[0] + "\"\n}")
        else:
            catFile.write("\t\"" + catArray[i] + "\":\"" + catArray[i].split('.txt')[0] + "\",\n")
        print item

    catFile.close()


def append_to_category_files(product_list_file="product_list.txt",
                             lookup_file="category_lookup.json"):
    prodFile = open(product_list_file).read()
    prodArray = []
    prodArray.extend(prodFile.split('\n'))
    curCatSet = set()

    for i, item in enumerate(prodArray):
        if not item:
            continue

        productFileName = item + '.json'
        print "^^^^^^^^^  " + productFileName

        with open(productFileName) as json_data:
            catDic = json.load(json_data)
            if catDic['category'] != '_':
                if catDic['category'] != ' ':
                    json_data = open(lookup_file)
                    d = json.load(json_data)
                    for key, value in d.iteritems():
                        if catDic['category'] == value:
                            catFile = open(key, "a")
                            curCatSet.add(key)
                            productText = item + '.txt'
                            text = open(productText).read()
                            catFile.write('\t' + text + ',\n')
                            catFile.close()

    catFile = open("currentCatList.txt", "a")
    for cat in curCatSet:
        catFile.write(cat + '\n')
    catFile.close()

    for cat in curCatSet:
        temp = open(cat).read()
        temp = temp[:-2]
        temp = temp + '\n}'
        print '****************'
        print temp
        open(cat, 'w').close()
        catFile = open(cat, "a")
        catFile.write(temp)
        catFile.close()
