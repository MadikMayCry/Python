import pyowm

owm = pyowm.OWM('c5a0ecd4fe79afb4753f4132fdb2a2cb')  # You MUST provide a valid API key

observation = owm.weather_at_place('Москва')
w = observation.get_weather()
print(w)
