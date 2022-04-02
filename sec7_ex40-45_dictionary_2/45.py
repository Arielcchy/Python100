# Convert Dictionary into a List of Lists

product_info = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

output = []

for k, v in product_info.items():
    output.append([k,v])

print(output)
