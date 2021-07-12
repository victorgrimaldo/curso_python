import requests
url = "https://api.tomorrow.io/v4/timelines"

querystring = {
"location":"25.772032369661, -100.24108910193371",
"fields":["temperature", "cloudCover"],
"units":"imperial",
"timesteps":"1d",
"apikey":"vovTsS0NlUl7LVRUB5jrcnS1Fyr3XK4C"}

response = requests.request("GET", url, params=querystring)
print(response.text)