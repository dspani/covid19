import cgi

form = cgi.FieldStorage()
print(form.getvalue('name'))
print(form.getvalue('email'))
print(form.getvalue('phone'))
