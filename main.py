import json
import requests
from bs4 import BeautifulSoup as bs

class Place:
    def __init__(self, id):
        self.id = id
        self.name = ''
        self.visits = 0

    def __str__(self):
        return f"{self.name} ({self.id}): {self.visits}"

frontpage_data = json.load(open('data.json'))
places_dict = {}

with open('places.tsv', 'w', encoding='utf-8') as f:
    for section in frontpage_data:
        for place_id in section['places']:
            if place_id not in places_dict:
                place = Place(place_id)
                place_html = requests.get('https://www.roblox.com/games/' + place_id).content
                place_soup = bs(place_html, 'html.parser')

                name_element = place_soup.find('h2', { 'class': 'game-name' })
                place.name = name_element['title']

                visits_element = place_soup.find('p', { 'id': 'game-visit-count' })
                place.visits = int(visits_element['title'].replace(',', ''))

                places_dict[place_id] = place
                print(place)
                f.write(f"{place.name}\t{place.id}\t{place.visits}\n")

"""
for section in frontpage_data:
    for id in section['places']:
        if id in all_places:
            all_places[id] += 1
        else:
            all_places[id] = 1
        num_slots += 1

places_freq = []
for id in all_places:
    places_freq.append((all_places[id], id))

num_places = len(places_freq)
print("\nNumber of place slots: " + str(num_slots))
print("\nNumber of unique places: " + str(num_places))

places_freq = sorted(places_freq, key=lambda item: item[0])

print("\nNumber of times a specific place shows up on the front page")
for freq, id in places_freq:
    print(str(freq) + ": " + id)


freq_summary = {}
for freq, _ in places_freq:
    if freq in freq_summary:
        freq_summary[freq] += 1
    else:
        freq_summary[freq] = 1

print("\nNumber of times a place is shown the given number of times")
for times in freq_summary:
    print(str(times) + ': ' + str(freq_summary[times]))
"""