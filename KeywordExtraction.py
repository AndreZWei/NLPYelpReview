# Keyword Extraction

# Author: Boyang Lu, Zhangyang Wei, Jie Zhou

import pickle

# dictionary of (business id, list of review ids)
with open('business_review.data', 'rb') as input:
	business_review = pickle.load(input)

# dictionary of (review id, review contents)
with open('id_content.data', 'rb') as input:
	id_content = pickle.load(input)