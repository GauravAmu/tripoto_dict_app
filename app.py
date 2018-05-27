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

	for word in response:
		if typeofComparison == 'eq':
			if(len(word)==int(lengthThreshold)) :
				toShow.append(word)
			else:
				return 'no result found'
		elif typeofComparison == 'lt':
			if(len(word)<int(lengthThreshold)) :
				toShow.append(word)
			else:
				print('no result found')
		elif typeofComparison == 'lte':
			if(len(word)<=int(lengthThreshold)) :
				toShow.append(word)
			else:
				print('no result found')
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