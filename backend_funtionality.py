
# ====================================================== IMPORTING RANDOM =======================================================#
import random


# ====================================================== CREATING UID =======================================================#

def UID_maker(name,latitude,longitude):
    uid=['H','O','S','-']
    uid.append(name[0])
    for i in range(1,len(name)):
        if(name[i]==' '):
            uid.append(name[i+1].upper())
    uid.append('@')
    uid.append(str(round(latitude,3)))
    uid.append('.')
    uid.append(str(round(longitude,3)))
    uidf=''
    uidf=uidf.join(uid)
    return uidf


# ====================================================== FINDING HOSPITAL NEAR ME =======================================================#

def hosfinder():

    # ====================================================== IMPORTING LIBRARIES =======================================================#

    from googleplaces import GooglePlaces, types, lang
    import requests
    import json
    import geocoder
    import database_funtionality
    g = geocoder.ip('me')

    name_list=[]
    uid_list=[]

    lat = g.latlng[0]
    print(lat)
    lon = g.latlng[1]
    print(lon)

    # Use  API key for making api request calls
    API_KEY = 'AIzaSyCd5aslzA_Doi2ank8_zVkk9_euqSfoCwo'

    # Initialising the GooglePlaces constructor
    google_places = GooglePlaces(API_KEY)

    # call the function nearby search with
    # the parameters as longitude, latitude,
    # radius and type of place which needs to be searched of
    # type can be HOSPITAL, CAFE, BAR, CASINO, etc
    query_result = google_places.nearby_search(
        lat_lng={'lat': lat, 'lng': lon},
        radius=1000,
        # types =[types.TYPE_HOSPITAL] or
        # [types.TYPE_CAFE] or [type.TYPE_BAR]
        # or [type.TYPE_CASINO])

        types=[types.TYPE_HOSPITAL])

    # If any attributions related
    # with search results print them

    if query_result.has_attributions:
        print(query_result.html_attributions)

    # Iterate over the search results
    for place in query_result.places:

        # ====================================================== GENERATING FAKE DATA =======================================================#

        UID = UID_maker(place.name, place.geo_location['lat'], place.geo_location['lng'])
        password = "PASS-" + UID
        licence = "LIC-" + UID
        a = random.choice(['9:00-11:00','10:00-12:00','11:00-1:00','12:00 - 2:00'])
        gopd = a
        pn = random.randint(7000000000,9999999999)
        icu = random.randint(2,10)
        a_icu = random.randint(0, icu)
        rateing  = round(random.uniform(2.0,5.0),1)
        ambulance = random.randint(0, 10)
        totalbed = random.randint(100,500)
        a_totalbed = random.randint(100, totalbed)
        pharm = random.choice([0,1])
        A_N_UNIT = random.randint(0,100)
        A_P_UNIT = random.randint(0, 100)
        B_N_UNIT = random.randint(0, 100)
        B_P_UNIT = random.randint(0, 150)
        AB_N_UNIT = random.randint(0, 50)
        AB_P_UNIT = random.randint(0, 50)
        O_N_UNIT = random.randint(0, 50)
        O_P_UNIT = random.randint(0, 100)
        uid_list.append(UID)
        name_list.append(place.name)

        # ====================================================== ADDING DATA TO DATABASE =======================================================#

        database_funtionality.hospital_data_entry(place.name,UID,password,place.geo_location['lat'],place.geo_location['lng'],
                                                  gopd,pn,icu,a_icu,rateing,ambulance,totalbed,a_totalbed,pharm
                                                  ,A_N_UNIT,A_P_UNIT,B_N_UNIT,B_P_UNIT,AB_N_UNIT,AB_P_UNIT,O_N_UNIT,O_P_UNIT)


        #print("Name : ", place.name)
        #print("Latitude : ", place.geo_location['lat'])
        #print("Longitude : ", place.geo_location['lng'])
        #print("phone no.",pn)
        #print("genral OPD timing :",gopd)
        #print("Unique ID : ", UID)
        #print("Password : ", password)
        #print("licence : ", licence)
        #print('icu :', icu)
        #print('avilable icu :', a_icu)
        #print('rating :', rateing)
        #print('ambulance :', ambulance)
        #print('beds :', totalbed)
        #print('avilable :', a_totalbed)
        #print('pharmacy :',pharm)
        #print("A- :",A_N_UNIT)
        #print("A+ :", A_P_UNIT)
        #print("B- :", B_N_UNIT)
        #print("B+ :", B_P_UNIT)
        #print("AB- :", AB_N_UNIT)
        #print("AB+ :", AB_P_UNIT)
        #print("O- :", O_N_UNIT)
        #print("O+ :", O_P_UNIT)
        #print()

    return name_list,uid_list


# ====================================================== CREATING USERNAME FOR USER =======================================================#

def creating_user_username(email='INVALID EMAIL'):
    username = ['C','L','I','-']
    for i in email:
        if(i!='@'):
            username.append(i)
        else:
            break

    username=''.join(username)
    return username


# ====================================================== CHEACKING DATA AT TIME OF SIGNUP =======================================================#
def cheacking_data(name,email,mobile,password):
    if(name==''):
        return 'e1'
    elif(email.find('@')==-1):
        return 'e2'
    elif(len(mobile)<10):
        return 'e3'
    else:
        return 'p'

