"""
You are going to write a program that adds to the travel_log.
 You can see a travel_log which is a list that contzins travl_log
 add_new_country("Russia", 2, ["Moscow", "saint-petersburg"])
 print you visited russia 2 times
 print you visited moscow and saint-petersburg 
"""
travel_log = [
    {
    "country": "france",
    "visits": 12,
    "cities": ["paris", "lille", "Dijon"]
    }, 
    {
    "country": "Germant",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Sttugart"]
    }
]
def add_new_country(country, times, cities):
    
    #for dict in travel_log:
    #    print(dict)
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = times
    new_country["country"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "saint-petersburg"])
print(travel_log)