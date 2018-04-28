# NLP Yelp Review Analysis Project

# Author: Boyang Lu, Zhangyang Wei, Jie Zhou

import json

# Read in the file

f = open("../dataset_complete/review.json")
review_data = []
for line in f:
	review_data.append(json.loads(line))


f = open("../dataset_complete/business.json")
business_data = []
for line in f:
	business_data.append(json.loads(line))

selected_data = []
for i in range(10):
	max = 0
	print(i)
	selected = business_data[0]
	for term in business_data:
		if (term["review_count"] > max):
			max = term["review_count"]
			selected = term
	selected_data.append(selected)
	selected["review_count"] = 0

selected_review = []
for i in range(10):
	print(i)
	text = []
	for term in review_data:
		if (term["business_id"] == selected_data[i]["business_id"]):
			text.append(term["text"])
	selected_review.append((selected_data[i]["business_id"], text))

for business in selected_review:
	print(business)
	print("\n\n")