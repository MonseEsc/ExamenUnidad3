from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
	contenido = """

	<html>
	<head>
		<style>
			body{
			margin: 9em;
			text-align: center;
			color: purple;
			background-color: rgb(231,152,231);
			}
		</style>
	</head>
	<body>
		<h1> ITI8MB</h1>
		<h1>MONSERRAT ESCOBAR MARTINEZ</h1>
		<h1>1318283177</h1>
	</body>
	</html>
	"""
	return HttpResponse(contenido)
