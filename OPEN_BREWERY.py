import requests

class OpenBrewery:
    def __init__(self):
        pass

#Using methods of requests to fetch required data from URL
    def fetch_brewery_NY(self, ny_url):
        response = requests.get(ny_url)
        if response.status_code == 200:
            brewery_data = response.json()
            return brewery_data
        else:
            print("Error")
            return None

#Using methods of requests to fetch required data from URL
    def fetch_brewery_Alaska(self, alaska_url):
        response = requests.get(alaska_url)
        if response.status_code == 200:
            brewery_data = response.json()
            return brewery_data
        else:
            print("Error")
            return None

#Using methods of requests to fetch required data from URL
    def fetch_brewery_Maine(self, maine_url):
        response = requests.get(maine_url)
        if response.status_code == 200:
            brewery_data = response.json()
            return brewery_data
        else:
            print("Error")
            return None
#Using state value as filter to get total count
    def breweries_in_NY(self, brewery_data):
        newyork_breweries_count = 0
        for brewery in brewery_data:
            if 'New York' in brewery.get('state_province', []) :
                newyork_breweries_count = newyork_breweries_count + 1

        return newyork_breweries_count

# Using state value as filter to get total count
    def breweries_in_Alaska(self, brewery_data):
        alaska_breweries_count = 0
        for brewery in brewery_data:
            if 'Alaska' in brewery.get('state_province', []):
                alaska_breweries_count = alaska_breweries_count + 1
        return alaska_breweries_count

#Using state value as filter to get total count
    def breweries_in_Maine(self, brewery_data):
        maine_breweries_count = 0
        for brewery in brewery_data:
            if 'Maine' in brewery.get('state_province', []):
                maine_breweries_count = maine_breweries_count + 1
        return maine_breweries_count
#Instance Creation - To Access Methods for OpenBrewery Class
open_brewery = OpenBrewery()
ny_url = "https://api.openbrewerydb.org/v1/breweries?by_state=new_york"
ny_data = open_brewery.fetch_brewery_NY(ny_url)
print("Breweries in NewYork:")
print(ny_data)
ny_count = open_brewery.breweries_in_NY(ny_data)
print("Total Count of Breweries in New York:")
print(ny_count)
alaska_url = "https://api.openbrewerydb.org/v1/breweries?by_state=alaska"
alaska_data = open_brewery.fetch_brewery_Alaska(alaska_url)
print("Breweries in Alaska:")
print(alaska_data)
alaska_count = open_brewery.breweries_in_Alaska(alaska_data)
print("Total Count of Breweries in Alaska:")
print(alaska_count)
maine_url = "https://api.openbrewerydb.org/v1/breweries?by_state=maine"
maine_data = open_brewery.fetch_brewery_Maine(maine_url)
print("Breweries in Maine:")
print(maine_data)
maine_count = open_brewery.breweries_in_Maine(maine_data)
print("Total Count of Breweries in Maine:")
print(maine_count)