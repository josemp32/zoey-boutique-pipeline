def create_master_json_file(current_cat_list="currentCatList.txt",
                            output_file="zoey_boutique.json"):
    currCatFile = open(current_cat_list).read()
    currCatArray = []
    currCatArray.extend(currCatFile.split('\n'))
    temp = ''

    for i, item in enumerate(currCatArray):
        if item == '':
            continue

        currCatFileContent = open(item).read()

        if i == 0:
            temp = '{\n'

        temp += currCatFileContent + ',\n'

        if i == len(currCatArray) - 1:
            temp += '}'

    temp = temp[:-2]
    temp = temp + '\n}'

    catFile = open(output_file, "a")
    catFile.write(temp)
    catFile.close()


if __name__ == "__main__":
    create_master_json_file()
