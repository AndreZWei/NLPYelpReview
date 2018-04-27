# NLP Yelp Review Analysis Project

# Author: Boyang Lu, Zhangyang Wei, Jie Zhou

import json

# Read in the file
f = open("dataset/small_review_sample1.json")
data = []
for line in f:
	data.append(json.loads(line))

print(data[14]["stars"])