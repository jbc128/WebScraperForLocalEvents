import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_eventbrite_events(url: str = "https://www.eventbrite.com/d/tx--manor/events/") -> list:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    events = []
    

    script = soup.find('script', string=re.compile(r'window\.__SERVER_DATA__'))
    if script:
        server_data_line = next((line for line in script.string.splitlines() if line.strip().startswith('window.__SERVER_DATA__')), None)
        if server_data_line:
            json_str = server_data_line.split('=', 1)[1].strip().rstrip(';')
            try:
                server_data = json.loads(json_str)
            except json.JSONDecodeError:
                server_data = []
        else:
            server_data = []
    events = []
    for event in server_data['jsonld'][0]['itemListElement']:
        addressList = event['item']['location'].get('address', 'an Unknown address')
        if isinstance(addressList, dict):
            address = addressList['streetAddress']
        events.append(f"On {event['item']['startDate']}, '{event['item']['name']}' will be held at {address}.")
    return events

if __name__ == "__main__":
    events = scrape_eventbrite_events()
    for event in events:
        print(event)