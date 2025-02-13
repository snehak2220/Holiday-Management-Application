from datetime import datetime

from django.conf import settings
from django.contrib.sites import requests
from django.core.paginator import Paginator
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import HolidaySerializer


# Create your views here.

def index(request):
    # Get Query Parameters
    country = request.GET.get('country')
    year = request.GET.get('year')
    month = request.GET.get('month')
    name = request.GET.get('name', '').strip().lower()
    type = request.GET.get('type', '').strip().lower()
    date = request.GET.get('date')
    page_number = request.GET.get('page', 1)

    holidays = []

    # Check Required Parameters
    if country and year:
        api_key = settings.CALENDARIFIC_API_KEY
        api_url = f'https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country}&year={year}'

        if month:
            api_url += f"&month={month}"
        if date:
            api_url += f"&date={date}"

        print("API URL:", api_url)

        # Call API
        response = requests.get(api_url)
        if response.status_code == 200:
            holidays = response.json().get('response', {}).get('holidays', [])
            print("Holidays from API:", holidays)
        else:
            return render(request, 'index.html', {"messages": "Failed to fetch holidays from Calendarific API."})

        # Filter by Name (Case Insensitive)
        if name:
            holidays = [holiday for holiday in holidays if name in holiday['name'].lower()]

        # Filter by Type (Case Insensitive, handling list of types)
        if type:
            holidays = [holiday for holiday in holidays if type.lower() in [t.lower() for t in holiday['type']]]

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            holidays = [holiday for holiday in holidays if holiday['date']['iso'] == date]

    # Paginate the Results
    paginator = Paginator(holidays, 10)
    page_obj = paginator.get_page(page_number)
    unique_types = set()
    print("Date Filter:", date)
    for holiday in holidays:
        for t in holiday['type']:
            unique_types.add(t)
    # Context for Template
    context = {
        'holidays': page_obj,
        'country': country,
        'year': year,
        'month': month,
        'type': type,
        'name': name,
    }

    return render(request, 'index.html', context)


class HolidayListView(APIView):
    def get(self, request):
        country = request.GET.get('country')
        year = request.GET.get('year')
        month = request.GET.get('month')
        holiday_type = request.GET.get('type')

        if not country or not year:
            return Response({"error": "Country and year are required."}, status=status.HTTP_400_BAD_REQUEST)

        api_url = "https://calendarific.com/api/v2/holidays"
        params = {
            'api_key': settings.CALENDARIFIC_API_KEY,
            'country': country,
            'year': year,
        }

        if month:
            params['month'] = month

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Check for HTTP request errors
            data = response.json()
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)

        holidays = []
        if response.status_code == 200 and 'response' in data:
            for holiday in data['response']['holidays']:
                if holiday_type:
                    if holiday_type.lower() in [t.lower() for t in holiday['type']]:
                        holidays.append({
                            'name': holiday['name'],
                            'date': holiday['date']['iso'],
                            'description': holiday.get('description', 'No description available.')
                        })
                else:
                    holidays.append({
                        'name': holiday['name'],
                        'date': holiday['date']['iso'],
                        'description': holiday.get('description', 'No description available.')
                    })

        serializer = HolidaySerializer(holidays, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
