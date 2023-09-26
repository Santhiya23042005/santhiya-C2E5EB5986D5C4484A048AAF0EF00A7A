def linear_search_product(product_list, target_product):
    indices = []

    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)

    return indices

# Example list of products
products = ["apple", "banana", "orange", "apple", "grape"]

# Target product to search for
target = "apple"

# Call the function to find the indices of "apple" in the list
result = linear_search_product(products, target)

# Print the result
if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")






