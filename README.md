# Report
1. Completed the python program to convert Arabic Numerals to Roman Numerals and created a test python file.
2. Used `flake8` linter to check the coding style by GithubAction.
3. Used `pytest` to run the test python file by GithubAction.

## Committed Files
- `weather.py`
	1. This is the main program of `AirportWeather` API.
	The file can run with its own main function, which takes user inputs including the target airport `iata code` and the expected past `time period`. The result can be see in samples section.
	2. After being imported, user can instantiated the AirportWeather class to make an object, and by giving the input  `iata` and `duration`, the api will automatically searching for the weather condition about the target airport in the specific time period.
- `test_weather.py`
	This is the test file of `weather.py`. It aims to test the stability of AirportWeather API. Such as typos, Internet connection and nonexistent airports.
	It also tests the normal cases.
- `data.csv`
	This is the source file of all the airports in the world. You can check the name, iata code, coordinates and city.
## User Story
- "As a user, I would like to get weather informations form my interested airports."
- "As a user, I would like to get weather informations in a specific period."
## AirportWeatherAPI
### Imported Files
- requests
- datetime
- pandas
### Class AirportWeather()
- This is the only class in the file, can be instantiated.
- It takes the iput as `iata` and `duration`
### __init__(self, iata, duration)
- This is the constructor
### _lookup_airport(self)
- This reads the `data.csv` file. Matches the `iata` to the airport and returns the name, icao code and coordinates.
### _get_weather(self)
- This requests the target airport weather information from the weather station web api by icao code, which is a free api open to anyone. Returns all the history data.
### _construct_weather(self, observation)
- This select the data in designated time period and make them in a proper form.
### _get_time_diff_by_now(self, time)
- This compute the `duration` by the user input.
### print_weather(self)
- This forms the output into proper style.
- After successfully printed the weather information, it returns 'report end'.



## API Samples
## Aquire the airport code
![Image description](https://github.com/BUEC500C1/api-design-Suli-Hu/blob/weather-api/step1.png)
## Aquire the time period
![Image description](https://github.com/BUEC500C1/api-design-Suli-Hu/blob/weather-api/step2.png)
## Normal Test 1
![Image description](https://github.com/BUEC500C1/api-design-Suli-Hu/blob/weather-api/normal1.png)
## Normal Test 2
![Image description](https://github.com/BUEC500C1/api-design-Suli-Hu/blob/weather-api/normal2.png)
## Normal Test 3
![Image description](https://github.com/BUEC500C1/api-design-Suli-Hu/blob/weather-api/normal3.png)


## Workflow
1. Proposed a new feature.
2. Create a new branch on git to develop the feature.
3. Complete code and commit to feature branch.
4. Ran CB (linter) on GitHub Action and revise the code until meet the linter requirements.
5. Ran CI (unit tests) by purest on GitHub Action and fixed spotted bugs.
6. Made a final review and ready to merge feature branch to stable branch.
7. Merged into master and completed feature development.
