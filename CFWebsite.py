from flask import Flask
from flask import Flask, render_template
from flask import request
import requests

key = 'key-7f6f27f594aa7790f2c8219457aab707'
sandbox = 'sandboxa27646c310604c5da3abf84ceb3d80df.mailgun.org'

app = Flask(__name__)

@app.route('/')
def website():
	return render_template('CFWebsite.html')


@app.route('/404')
def error_404():
    return "You should not be here"


@app.route('/<name>')
def name(name):
	h = "hello" + name.title()

#@app.route('/page 2')
#def page2():
 #   return "this is page 2"

#@app.route('/204')
#def page204():
 #   return "this is page 204"

#@app.route('/aboutme1')
#def aboutme():
#return render_template('aboutme1.html')


@app.route("/contact", methods=['POST'])
def contact():
	form_data= request.form

	#Get form data
	name = form_data['name']
	message = form_data['message']
	email = form_data['Email']

	print(name, message, email)

	#email message
	subject = "Hello from Anna and Caitlin"
	body = "You've successfully typed in your details and affirming the success of our website"

	sender = 'Ip3g14@soton.ac.uk'

	#Sending message 
	request_url = 'https://api.mailgun.net/vs/{0}/messages'.format(sandbox)

	email_request = requests.post(request_url, auth=('api', key), data={
	'from': sender,
	'to': email,
	'subject': subject,
	'text': body
	})

	with open("Data/contact.txt",'w') as f1:
		f1.write(name + "\t" + message + "\t" + email)
		print('Written in file')
			
	# checking email status
	print('Status:{0}'.format(email_request.status_code))
	print('Body: {0}'.format(email_request.text))

	return("Thank you for using our website!")

if __name__ == "__main__":
     app.run()

# def hello_world():
#        author = "Devasena"
#        name = "Robot"
#        return render_template('index.html', author=author)