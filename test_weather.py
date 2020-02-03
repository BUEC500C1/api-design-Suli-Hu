# copyright Suli sulihu@bu.edu 2020

from weather import AirportWeather


def test_normal():
    aw1 = AirportWeather('BOS', 3)
    aw2 = AirportWeather('BOS', 6)
    aw3 = AirportWeather('BOS', 12)
    aw4 = AirportWeather('JFK', 12)
    aw5 = AirportWeather('ITH', 12)
    aw6 = AirportWeather('ATL', 12)
    assert aw1.print_weather() == 'Report End'
    assert aw2.print_weather() == 'Report End'
    assert aw3.print_weather() == 'Report End'
    assert aw4.print_weather() == 'Report End'
    assert aw5.print_weather() == 'Report End'
    assert aw6.print_weather() == 'Report End'

def test_nonexist():
    aw1 = AirportWeather('Nowhere',5)
    assert aw1.print_weather() == 'Report End'

def test_internet():
    pass

def test_typo():
    aw1 = AirportWeather('bos', 3)
    aw2 = AirportWeather('BOS', three)
    assert aw1.print_weather() == 'Report End'
    assert aw2.print_weather() == 'Report End'

    

def main():
    pass

if __name__ == "__main__":
    main()
