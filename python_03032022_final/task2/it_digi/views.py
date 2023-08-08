from logging import Logger

import day as day
from django.shortcuts import render, redirect
# from matplotlib.testing.jpl_units import day

from .models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import carinfo, stationMapping
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'show/index.html')



def loginpage(request):
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, 'successfully')
            # return render(request, 'show/login.html')
            return redirect('bookcargo')
        else:
            messages.error(request, 'check id pass')
            return redirect('loginpage')
    return render(request, 'show/login.html')


def register(request):
    if request.method == "POST":
        # name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        # contact = request.POST['contact']
        password = request.POST['password']
        # print(name, username, email, password)
        if User.objects.filter(username=username).exists():
            print("Username is already taken")
            messages.error(request, 'This username is already taken')
            return redirect('registrationpage', )
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken")
            return redirect('registrationpage')
        else:
            students = User.objects.create_user(username=username, email=email, password=password)
            students.save()
            messages.success(request, "Registered successfully")
            return redirect('/lg')

    return render(request, 'show/registration.html')


# def login(request):
#     if request.method == "POST":
#         print(request.POST)
#         username = request.POST['loginusername']
#         password = request.POST['loginpassword']
#         print(password,username)
#         User = authenticate(request, username=username, password=password)
#         print(User)
#         if User is None:
#             messages.error(request, 'not successfully')
#             return render(request, 'show/login.html')
#         else:
#             messages.error(request, 'Login successfully')
#             return redirect('/')
#     return render(request, 'show/login.html')
#
# def register(request):
#
#     if request.method == "POST":
#         #name = request.POST['name']
#         username = request.POST['username']
#         email = request.POST['email']
#         #contact = request.POST['contact']
#         password = request.POST['password']
#         # print(name, username, email, password)
#         if User.objects.filter(username=username).exists():
#             print("Username is already taken")
#             messages.error(request, 'This username is already taken')
#             return redirect('registrationpage', )
#         elif User.objects.filter(email=email).exists():
#             messages.error(request, "Email is already taken")
#             return redirect('registrationpage')
#         else:
#             students = User( username=username,email=email,password=password,)
#             students.save()
#             messages.success(request, "Registered successfully")
#             return redirect('/lg')
#
#     return render(request, 'show/registration.html')

def python(request):
    return render(request, 'show/python.html')


def java(request):
    return render(request, 'show/java.html')


def c(request):
    return render(request, 'show/c++.html')


def ac(request):
    return render(request, 'show/addcar.html')
#
#
# def book(request):
#     return render(request, 'show/booknow.html')


def end(request):
    return render(request, 'show/engpage.html')


def pdf(request):
    return render(request, 'show/pdf1.html')


def car(request):
    if request.method == "POST":
        carnumber = request.POST['carnumber']
        carstartlocation = request.POST['carstartlocation']
        # carsecondlocation= request.POST['carsecondlocation']
        carthridlocation = request.POST['carthridlocation']
        carfourthlocation = request.POST['carfourthlocation']
        carendlocation = request.POST['carendlocation']
        carstatus = request.POST['carstatus']
        # book = request.POST['Book Now']
        runningdays = request.POST['runningdays']
        # availableSeatsStop1 = request.POST['availableSeatsStop1']
        # availableSeatsStop2 = request.POST['availableSeatsStop2']
        # availableSeatsStop3 = request.POST['availableSeatsStop3']
        # availableSeatsStop4 = request.POST['availableSeatsStop4']
        CarD = carinfo(carnumber=carnumber,
                       carstartlocation=carstartlocation,
                       # availableSeatsStop1=availableSeatsStop1,
                       # availableSeatsStop2=availableSeatsStop2,
                       # availableSeatsStop3=availableSeatsStop3,
                       # availableSeatsStop4=availableSeatsStop4,
                       # carsecondlocation=carsecondlocation,
                       carthridlocation=carthridlocation,
                       carfourthlocation=carfourthlocation,
                       carendlocation=carendlocation, carstatus=carstatus, runningdays=runningdays,
                       )
        CarD.save()
        # from django.http import HttpResponse
        # from django.template.loader import get_template
        # from xhtml2pdf import pisa
        # template_path = 'pdf1.html'
        # # Create a Django response object, and specify content_type as pdf
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # # find the template and render it.
        # template = get_template(template_path)
        # html = template.render(context)

        # create a pdf
        # pisa_status = pisa.CreatePDF(
        #     html, dest=response)
        # # if error then show some funy view
        # if pisa_status.err:
        #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
        # return response
        # messages.success(request, "Successfully Uploded")
        # return redirect('car')
    return render(request, 'show/car.html')


def fetch(request):
    global prev_sta_data
    print(request.POST, "-------")
    fetch_data = {}
    carstartlocation = request.POST['start location']
    carendlocation = request.POST['end location']
    # bookingDate = request.POST['Booking Date']
    # Booking_Seat = request.POST['Booking Seat']c
    # carthirdlocation = request.POST['Third location']

    # def bn(request):
    #         print(request.POST, "-------")
    #         booknow_data = {}
    #         carstartlocation = request.POST['start location']
    #         carendlocation = request.POST['end location']
    # #

    import datetime

    ## mm/dd/yyyy to date object
    # dateStr = bookingDate
    # dateObj = datetime.datetime.strptime(dateStr, "%Y-%m-%d").date()
    # day = ""
    # print(dateObj.weekday())
    # if dateObj.weekday() == 6: day = "SUN,WEEKLY"
    # elif dateObj.weekday() == 0 : day = "MON,WEEKLY"
    # elif dateObj.weekday() == 1:  day = "TUE,WEEKLY"
    # elif dateObj.weekday() == 2:  day = "WED,WEEKLY"
    # elif dateObj.weekday() == 3: day = "THU,WEEKLY"
    # elif dateObj.weekday() == 4: day = "FRI,WEEKLY"
    # elif dateObj.weekday() == 5: day = "SAT,WEEKLY"
    # else: day = "WEEKLY"

    status = "Active"
    from django.db.models import Q

    if carinfo.objects.filter(carstartlocation=carstartlocation, carstatus=status).exists():

        seatCheck = stationMapping.objects.filter(startLocation=carstartlocation, nextLocation=carendlocation,
                                                  availSeat__gt=0)
        # print("1st condition", seatCheck)

        prev_sta_data = []
        fetch_data_new = []
        if not seatCheck:
            fetch_data = carinfo.objects.filter(Q(carstartlocation=carstartlocation, carsecondlocation=carendlocation,
                                                  carstatus=status) | Q(carstartlocation=carstartlocation,
                                                                        carthridlocation=carendlocation,
                                                                        carstatus=status) | Q(
                carstartlocation=carstartlocation, carfourthlocation=carendlocation,
                carstatus=status) | Q(carstartlocation=carstartlocation, carendlocation=carendlocation,
                                      carstatus=status))
            prev_sta_data = fetch_data

        else:
            for k in seatCheck:
                fetch_data = carinfo.objects.filter(carnumber=k.carnumber)
                for l in fetch_data:
                    l.availableSeatsStop4 = k.availSeat  # change field
                    l.save()
                    weeklyDays = str(k.runningdays).split(",")
                    for j in weeklyDays:
                        if j in day:
                            fetch_data_new.append(l)

    elif carinfo.objects.filter(carsecondlocation=carstartlocation, carstatus=status).exists():
        print("2 nd condition")

        seatCheck = stationMapping.objects.filter(startLocation=carstartlocation, nextLocation=carendlocation,
                                                  availSeat__gt=0)
        prev_sta_data = []
        fetch_data_new = []
        if not seatCheck:
            fetch_data = carinfo.objects.filter(Q(carsecondlocation=carstartlocation, carthridlocation=carendlocation,
                                                  carstatus=status)
                                                | Q(carsecondlocation=carstartlocation,
                                                    carfourthlocation=carendlocation, carstatus=status)
                                                | Q(carsecondlocation=carstartlocation, carendlocation=carendlocation,
                                                    carstatus=status))
            prev_sta_data = fetch_data

        else:
            for k in seatCheck:
                list_data = carinfo.objects.filter(carnumber=k.carnumber)
                fetch_data = list_data
                for l in fetch_data:
                    l.availableSeatsStop4 = k.availSeat  # change field
                    l.save()
                    weeklyDays = str(k.runningdays).split(",")
                    for j in weeklyDays:
                        if j in day:
                            fetch_data_new.append(l)


    elif carinfo.objects.filter(carthridlocation=carstartlocation, carstatus=status).exists():

        seatCheck = stationMapping.objects.filter(startLocation=carstartlocation, nextLocation=carendlocation,
                                                  availSeat__gt=0)
        print("3rd condition", seatCheck)
        fetch_data_new = []
        prev_sta_data = []
        if not seatCheck:
            fetch_data = carinfo.objects.filter(Q(carthridlocation=carstartlocation, carfourthlocation=carendlocation,
                                                  carstatus=status)
                                                | Q(carthridlocation=carstartlocation, carendlocation=carendlocation,
                                                    carstatus=status))

            prev_sta_data = fetch_data

        else:
            for k in seatCheck:
                fetch_data = carinfo.objects.filter(carnumber=k.carnumber)
                for l in fetch_data:
                    l.availableSeatsStop4 = k.availSeat  # change field
                    l.save()
                    weeklyDays = str(k.runningdays).split(",")
                    for j in weeklyDays:
                        if j in day:
                            fetch_data_new.append(l)



    elif carinfo.objects.filter(carfourthlocation=carstartlocation, carstatus=status).exists():

        seatCheck = stationMapping.objects.filter(startLocation=carstartlocation, nextLocation=carendlocation,
                                                  availSeat__gt=0)

        print("4 th condition", seatCheck)
        fetch_data_new = []
        prev_sta_data = []
        if not seatCheck:
            fetch_data = carinfo.objects.filter(Q(carthridlocation=carstartlocation, carfourthlocation=carendlocation,
                                                  carstatus=status)
                                                | Q(carthridlocation=carstartlocation, carendlocation=carendlocation,
                                                    carstatus=status))
            prev_sta_data = fetch_data

        else:
            for k in seatCheck:
                fetch_data = carinfo.objects.filter(carnumber=k.carnumber)
                for l in fetch_data:
                    l.availableSeatsStop4 = k.availSeat  # change field
                    l.save()
                    weeklyDays = str(k.runningdays).split(",")
                    for j in weeklyDays:
                        if j in day:
                            fetch_data_new.append(l)


    else:
        print("all condition checking")
        fetch_data = carinfo.objects.filter()
        fetch_data_new = fetch_data

        print(type(fetch_data_new))

    if fetch_data_new:
        context = {
            'content': {
                'data': fetch_data_new,
                'p1': carstartlocation,
                'p2': carendlocation
            }
        }
        print(context)

        return render(request, 'show/fetchNew.html', context)
    else:
        context = {
            'content': {
                'data': prev_sta_data,
                'p1': carstartlocation,
                'p2': carendlocation
            }
        }

        return render(request, 'show/prevStation.html', context)


def show(request):
    return render(request, 'show/show.html')


def books(request):
    print(request.POST, "-------")

    cargo = carinfo.objects.all()
    #     print("-------------")
    #     print(cargo)
    return render(request, 'show/booknow.html', {'shri': cargo})




def show(request):
    return render(request, 'show/show.html')


#
# def show(request):
#     return render(request, 'show/booknow.html')


# # pdf form data
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import *



def book(request):

    if request.method == "POST":
        # carnumber = request.POST['carnumber'],
        # carstartlocation = request.POST['carstartlocation'],
        # carthridlocation = request.POST['carthridlocation'],
        # carfourthlocation = request.POST['carfourthlocation'],
        # carendlocation = request.POST['carendlocation'],
        # carstatus = request.POST['carstatus'],
        # runningdays = request.POST['runningdays']
        context = {
            "carnumber": request.POST['carnumber'],
            "carstartlocation": request.POST['carstartlocation'],
            "carthridlocation": request.POST['carthridlocation'],
            "carfourthlocation": request.POST['carfourthlocation'],
            "carendlocation": request.POST['carendlocation'],
            "carstatus": request.POST['carstatus'],
            "runningdays": request.POST['runningdays']
        }
        # students = User(carnumber=carnumber, )
        # students.save()
        template_path = 'show/pdf1.html'
        # Create a Django responfse object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf1')
        response['Content-Disposition'] = 'attachment; filename="bookresipt.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        # print("DSamper "+context)
        # Logger.info("xcsds");
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    return render(request, 'show/booknow.html')

# pdf to data
