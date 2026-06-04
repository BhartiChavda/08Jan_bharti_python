import requests
from django.shortcuts import render

def home(request):
    """
    View to handle the homepage where users can search for a country.
    It fetches data from the REST Countries API and passes it to the template.
    """
    context = {}
    
    if request.method == 'POST':
        country_name = request.POST.get('country')
        if country_name:
            api_url = f'https://restcountries.com/v3.1/name/{country_name}'
            try:
                # Call the REST Countries API
                response = requests.get(api_url)
                
                # Check if the API request was successful
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        # Extract the first result (most relevant country)
                        country_data = data[0]
                        
                        context['country_name'] = country_data.get('name', {}).get('common', 'N/A')
                        context['official_name'] = country_data.get('name', {}).get('official', 'N/A')
                        context['capital'] = country_data.get('capital', ['N/A'])[0]
                        context['population'] = f"{country_data.get('population', 0):,}"
                        context['region'] = country_data.get('region', 'N/A')
                        context['flag_url'] = country_data.get('flags', {}).get('png', '')
                elif response.status_code == 404:
                    context['error'] = 'Country not found. Please check the name and try again.'
                else:
                    context['error'] = 'Failed to retrieve data from the API. Please try again later.'
                    
            except requests.exceptions.RequestException as e:
                # Handle connection errors or other request exceptions
                context['error'] = 'An error occurred while connecting to the API. Please try again later.'

    return render(request, 'index.html', context)
