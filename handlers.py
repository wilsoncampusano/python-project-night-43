from bottle import route, get, post, error, run, request
import re 

formu = '''<form action="/" method="post">
            Nombre : <input name="name" type="text" />
            Correo : <input name="email" type="text" />
            <input value="Firmar" type="submit" />
        </form> '''

@get('/')
def home():
	return formu

@post('/')
def home():
	name  = request.forms.get('name')
	email = request.forms.get('email')
	if not name or re.compile('(\w+@\w+.com)').match(email):
		return formu + '<p><strong>Revise sus datos</strong></p>'
	else:
		return name + email


@error(404)
def error404(error):
	return '404 weeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!! que intentabas'

run(host='localhost', port=8080, debug= True)
