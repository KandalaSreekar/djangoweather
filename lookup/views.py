from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['Zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=5&API_KEY=C0869F65-D5AB-4B98-B5AA-793E832A30E3")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error.."
		Category_description = None
		Category_color = None
		if api[0]['Category']['Name'] == 'Good':
			Category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk. "
			Category_color = "good"
		elif api[0]['Category']['Name'] == 'Moderate':
			Category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			Category_color = "moderate"
		elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
			Category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
			Category_color = "Unhealthyforsensitivegroups"
		elif api[0]['Category']['Name'] == 'Unhealthy':
			Category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			Category_color = "unhealthy"
		elif api[0]['Category']['Name'] == 'Very Unhealthy':
			Category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			Category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == 'Hazardous':
			Category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			Category_color = "hazardous"


		return render(request, 'home.html', {
			'api':api,
			'Category_description':Category_description,
			'Category_color':Category_color,
			})
	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C0869F65-D5AB-4B98-B5AA-793E832A30E3")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error.."
		Category_description = None
		Category_color = None
		if api[0]['Category']['Name'] == 'Good':
			Category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk. "
			Category_color = "good"
		elif api[0]['Category']['Name'] == 'Moderate':
			Category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			Category_color = "moderate"
		elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
			Category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
			Category_color = "Unhealthyforsensitivegroups"
		elif api[0]['Category']['Name'] == 'Unhealthy':
			Category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			Category_color = "unhealthy"
		elif api[0]['Category']['Name'] == 'Very Unhealthy':
			Category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			Category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == 'Hazardous':
			Category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			Category_color = "hazardous"


		return render(request, 'home.html', {
			'api':api,
			'Category_description':Category_description,
			'Category_color':Category_color,
			})

def about(request):
    return render(request, 'about.html', {})

def third(request):
	return render(request, 'third.html', {})