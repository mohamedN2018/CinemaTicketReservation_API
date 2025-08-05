from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservation
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, ReservationSerializer, MovieSerlializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets

# Create your views here.


#1 without REST and no model query FBV
def on_rest_no_model(request):
    guests = [
        {
            'id': 1,
            "Name": "Mohamed",
            "mobile": "01000000000",
        },
        {
            'id': 2,
            'name': "Ahmed",
            'mobile': "01000000001",
        }
    ]
    return JsonResponse(guests, safe=False)

#2 model data default django without rest
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name', 'mobile')),
    }
    return JsonResponse(response)



#3 Function based view
# 3.1 GET POST    
@api_view(['GET' , 'POST'])
def FBV_List(request):   
    # GET 
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#3.2 GET POST PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pK(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND)
        # GET 
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    if request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# CBV Class Based Views
# 4.1 List and Create == GET and POST
class CBV_List(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 4.2 GET PUT Delete cloass based views -- pk
class CBV_pK(APIView):
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#5 Mixins 
# 5.1 mixins list
class mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# 5.2 mixins get retrieve update delete
class mixins_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#6 Generics
# 6.1 get and post
class Generic_List(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'mobile']
# 6.2 get put and delete
class Generic_pK(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer



#7 ViewSets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerlializer
    filter_backend = [filters.SearchFilter]
    search_fields = ['movie', 'hall', 'date']


class viewsets_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


#8 find movie 

#9 create new reservation