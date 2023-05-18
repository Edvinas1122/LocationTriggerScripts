import requests
import json

def getPennyFoodOffers():
	url = "https://www.penny.de/"

	response = requests.get(url)
	html_code = response.text
	start_marker = 'window.pageData.products["'
	end_marker = '"}'

	products = []

	start_index = html_code.find(start_marker)
	while start_index != -1:
		start_index += len(start_marker)
		end_index = html_code.find(end_marker, start_index) + len(end_marker)
		json_data = html_code[start_index:end_index]
		json_data = json_data.split('"] = ')[1]

		try:
			product_data = json.loads(json_data)
			if product_data['category'] == 'food-highlights-fuer-alle':
				product_info = "Product: " + product_data['name'] + "\n" + "Discount: " + product_data['savingsPercent'] + "\n" + "Price: " + product_data['price']
				products.append(product_info)
		except json.JSONDecodeError:
			print("Failed to parse JSON data:", json_data)
		
		start_index = html_code.find(start_marker, end_index)
	
	return products
