from flask import Flask, render_template
from flask import request
from flask import Response
from seggregator import constructableWords
app = Flask(__name__)

@app.route("/tripoto", methods=['POST'])
def getDicwords():
	inputString = request.form.get('inputString')
	lengthThreshold = request.form.get('threshold')
	typeofComparison = request.form.get('comparison')
	response = constructableWords(inputString)
	toShow = []
	if lengthThreshold == '':
		for word in response:
			toShow.append(word)
		toShow.sort()
		return Response(",".join(toShow))

	if lengthThreshold != '':
		for word in response:
			if typeofComparison == 'eq':
				if(len(word)==int(lengthThreshold)) :
					toShow.append(word)
			elif typeofComparison == 'lt':
				if(len(word)< int(lengthThreshold)) :
					toShow.append(word)
			elif typeofComparison == 'lte':
				if(len(word)<=int(lengthThreshold)) :
					toShow.append(word)
			else:
				print('no valid words in dictionary')

		if not toShow:
			return 'no valid words in dictionary'
		
		toShow.sort()
		
		return Response(",".join(toShow))
	

@app.route("/")
def renderHomePage():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=False)