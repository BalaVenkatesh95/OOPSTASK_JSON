import requests

class RestCountries:
    def __init__(self):
        pass

#METHOD TO FETCH JSON / DATA FROM PROVIDED URL(USED REQUESTS)
    def fetch_json_data(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("error")
            return None

    def get_country_details(self, url):
        json_data = self.fetch_json_data(url)
#Filtering out Name, currency name and Symbols from List and creating separate List
        if json_data:
            country_details = []
            for country_data in json_data:
                country_name = country_data.get('name', {}).get('common', '')
                currencies = country_data.get('currencies', {})
                currency_names = []
                currency_symbols = []
                for currency_code, currency_info in currencies.items():
                    currency_names.append(currency_info.get('name', ''))
                    currency_symbols.append(currency_info.get('symbol', ''))
                country_details.append({'name': country_name,'currency':currency_names, 'symbol': currency_symbols})
            return country_details
        else:
            return None

#Filtering out country with € as currency
    def countries_with_euro(self, country_details):
        euro_countries = []
        for country in country_details:
            if '€' in country.get('symbol', []):
                euro_countries.append(country)
        return euro_countries

    # Filtering out country with $ as currency
    def countries_with_dollar(self, country_details):
        dollar_countries = []
        for country in country_details:
            if '$' in country.get('symbol', []):
                dollar_countries.append(country)
        return dollar_countries


#Instance Creation - To Access Methods for RestCountries Class
rest_countries = RestCountries()


url = "https://restcountries.com/v3.1/all"

json_data = rest_countries.fetch_json_data(url)
country_details = rest_countries.get_country_details(url)
print("FETCHED DETAILS:")
print(country_details)
countries_with_euro = rest_countries.countries_with_euro(country_details)
print("COUNTRIES WITH EURO AS CURRENCY:")
print(countries_with_euro)
countries_with_dollar = rest_countries.countries_with_dollar(country_details)
print("COUNTRIES WITH DOLLAR AS CURRENCY:")
print(countries_with_dollar)







