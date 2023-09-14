#from django.shortcuts import render
#from .models import Train

#def display_stations(request):
 #   if request.method == 'POST':
  #      train_id = request.POST.get('train_id')  
   #     train = Train.objects.filter(train_id=train_id).first()
    #    if train:
     #       stations = [getattr(train, f'station{i}') for i in range(1, 11) if getattr(train, f'station{i}')]
      #      if stations:
       #         return render(request, 'stations.html', {"stations": stations, "train_id": train_id})
        #    else:
         #    message = "No stations found for the given train ID."
          #   return render(request, 'index.html', {"message": message})
    #return render(request, 'index.html')
from django.shortcuts import render
from .models import Train, Station, Seat


def display_stations(request):
    if request.method == 'POST':
        train_id = request.POST.get('train_id')
        train = Train.objects.filter(train_id=train_id).first()

        if train:
            stations = [getattr(train, f'station{i}') for i in range(1, 11) if getattr(train, f'station{i}')]
            
            if stations:
                return render(request, 'stations.html', {"stations": stations, "train_id": train_id})
            else:
                message = "No stations found for the given train ID."
                return render(request, 'index.html', {"message": message})
        message="Train ID is invalid" 
        return render(request, 'index.html', {"message": message})
    return render(request, 'index.html')

#def display_trains(request):
#    if request.method == 'POST':
 #       station_name = request.POST.get('station_name')
  #      station = Station.objects.filter(station_name=station_name).first()

   #     if station:
    #        trains = Train.objects.filter(station_name=station_name) 

     #       if trains:
      #          return render(request, 'trains.html', {"trains": trains, "station_name": station_name})
       #     else:
        #        message = "No trains found for the given station."
         #       return render(request, 'index.html', {"message": message})

    #return render(request, 'index.html')
def display_trains(request):
    if request.method == 'POST':
        station_name = request.POST.get('station_name')
        station = Station.objects.filter(station_name=station_name).first()

        if station:
            trains = [getattr(station, f'train{i}') for i in range(1, 6) if getattr(station, f'train{i}')]
            
            if trains:
                return render(request, 'trains.html', {"trains": trains, "station_name": station_name})
            else:
                message = "No trains found for the given station."
                return render(request, 'index.html', {"message": message})
    message = "No trains found for the given station."
    return render(request, 'index.html', {"message":message})

def display_seat(request):
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = Seat.objects.filter(seat_id=seat_id).first()

        if seat:
            return render(request, 'seat.html', {"seat": seat})
        else:
            message = "No seat found for the given seat ID."
            return render(request, 'index.html', {"message": message})

    return render(request, 'index.html')