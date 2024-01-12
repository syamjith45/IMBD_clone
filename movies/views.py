from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Movies
from . serializers import *
from django.contrib.auth.models import User
from . utils import average_rate
# Create your views here.
class IndexApiView(APIView):
    def get(self,request):
        return Response({"Status oK"},status=status.HTTP_200_OK)
    
    
class MovieApiView(APIView):
    def get(self,request):
        term = request.GET.get("term", None)
        print("Term from URL:", term)  # Add this line for debugging
        if term:
            movies = Movies.objects.filter(title__icontains=term)
        else:
            movies = Movies.objects.all()
        serializer=MovieSerializer(data=movies,many=True)
        serializer.is_valid()
        return Response({"Status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class ReviewAPIView(APIView):
    def get(self,request,id=None):
        if not id:
            return Response({"status":"failed","message":"id is not required"},status=status.HTTP_400_BAD_REQUEST)
        reviews = Review.objects.filter(movie__id=id)
        serializers=ReviewSerializer(data=reviews,many=True)
        serializers.is_valid()
        return Response({"status":"success","data":serializers.data},status=status.HTTP_200_OK)
    
    def post(self,request,id=None):
        if not id:
            return Response({"status":"failed","message":"id is required"},status=status.HTTP_400_BAD_REQUEST)
        movie = Movies.objects.filter(id=id)
        if not movie.exists():
            return Response({"status":"failed","message":"No movie found"},status=status.HTTP_400_BAD_REQUEST)
        
        movie =movie.first()
        rating =request.data.get("rating")
        review = request.data.get("review")
        user = User.objects.get(id=1)
        try:
            rating = float(rating)
        except:
            return Response({"status":"failed","message":"invalid rating"},status=status.HTTP_400_BAD_REQUEST)
        
        Review.objects.create(user=user,movie=movie,rating=rating,review=review)
        avg =average_rate(movie)
        movie.rating = avg
        movie.save()
        return Response({'status':'Success','message':'Review Added'},status=status.HTTP_201_CREATED)
    
    def delete(self,request,id):
        if not id:
            return Response({"status":"failed","message":"id is required"},status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(id=1)
        review = Review.objects.filter(user=user,id=id)
        if not review.exists():
            return Response({"status":"failed","message":"No movie found"},status=status.HTTP_400_BAD_REQUEST)
        review.delete()
        return Response({'status':'Success','message':'Review deleted'},status=status.HTTP_200_OK)
        