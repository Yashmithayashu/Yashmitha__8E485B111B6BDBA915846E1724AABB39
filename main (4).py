def LinearSearchProduct(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Mango", "Apple"]
target = "Apple"
result = LinearSearchProduct(products, target)
print(result)  