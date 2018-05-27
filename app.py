from flask import Flask, render_template
from flask import request
from flask import Response
from seggregator import constructableWords
app = Flask(__name__)

@app.route("/tripoto", methods=['POST'])
def getDicwords():
	inputString = request.form.get('inputString')
	print(inputString)
	lengthThreshold = request.form.get('threshold')
	typeofComparison = request.form.get('comparison')
	print(typeofComparison)
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
				else:
					return 'no valid words found in dictionary'
			elif typeofComparison == 'lt':
				if(len(word)<int(lengthThreshold)) :
					toShow.append(word)
				else:
					return 'no valid words found in dictionary'
			elif typeofComparison == 'lte':
				if(len(word)<=int(lengthThreshold)) :
					toShow.append(word)
				else:
					return 'no valid words found in dictionary'
			else:
				print('no result found')
		toShow.sort()
		print(*toShow)
		return Response(",".join(toShow))

@app.route("/")
def renderHomePage():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=False)