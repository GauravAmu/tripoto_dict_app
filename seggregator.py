from loaddictionary import load_dict

def constructableWords(inputString) :
	response = []
	eligibleWords = load_dict(inputString)
	for word in eligibleWords :
		if len(list(set(list(word))-set(list(inputString))))==0:
			response.append(word)

	return response