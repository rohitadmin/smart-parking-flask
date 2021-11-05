import googlemaps
import json
import pprint
import time
#from GoogleMapsAPIKey import get_my_key

# Define the API Key.
API_KEY = 'AIzaSyAbToi8TEMeo8rxSZPuhxPGNRPzymnJH_0'

# Define the Client
gmaps = googlemaps.Client(key = API_KEY)

# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters
places_result  = gmaps.places_nearby(location='-33.8670522,151.1957362', radius = 40000, open_now =False , type = 'parking')

time.sleep(3)

place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])

stored_results = []

# loop through each of the places in the results, and get the place details.      
for place in places_result['results']:

    # define the place id, needed to get place details. Formatted as a string.
    my_place_id = place['place_id']

    # define the fields you would liked return. Formatted as a list.
    my_fields = ['name','formatted_phone_number','website']

    # make a request for the details.
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

    # print the results of the details, returned as a dictionary.
    pprint.pprint(places_details['result'])

    # store the results in a list object.
    stored_results.append(places_details['result'])
