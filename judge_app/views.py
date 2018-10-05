from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer

@api_view(['POST'])
def newuser(request):
	username = request.data['name']
	# check if username has been used
	if not User.objects.filter(username=username).exists():
		# if username has not been used then create a new user
		user = User.objects.create(username=username)
		userSerializer = UserSerializer(user, many=False)
		return Response({"vaild": "true"})
	else:
		# username has been used
		return Response({"vaild": "false"})
		
@api_view(['GET'])
def username(request, userID):
	# check if userID exists
	if User.objects.filter(pk=userID).exists():
		# if userID exists then print data of the user object
		user = User.objects.get(pk=userID)
		userSerializer = UserSerializer(user, many=False)
		return Response(userSerializer.data) 
	else:
		# if userID not exists then return false
		return Response({"vaild": "false"})

@api_view(['DELETE'])
def user(request, userID):
	# check if userID exists
	if User.objects.filter(pk=userID).exists():
		# if userID exists then delete this user
		User.objects.get(pk=userID).delete()
		return Response({"vaild": "true"})
	else:
		# if userID not exists then return false
		return Response({"vaild": "false"})
