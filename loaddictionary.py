import pandas as pd 

def load_dict(str):
	data = pd.read_csv('dictionary.csv')
	char_str = list(str)
	words = list(data['words'])
	ineligibleWords = [word for word in words if word[0] not in char_str]
	eligibleWords = list(set(words) - set(ineligibleWords))
	print(*eligibleWords)
	return eligibleWords; 
