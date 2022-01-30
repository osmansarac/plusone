import json

# Parsing Json File
f = open('data.json')
data = json.load(f)
# Product List
productList = []

if __name__ == '__main__':
    # Checking toppings and adding product name to product list if it includes 'Maple'
    for i in data:
        for j in i['topping']:
            if j['type'] == 'Maple':
                productList.append(i['name'])
    # Sorting product list
    productList.sort()
    # Printing products
    for i in productList:
        print(i)

    f.close()
