import requests
import json

API_KEY = "f3e8594a38087f01df7a23ede1712147"
TOKEN = "ATTA91a020f75bfc3b8c2dd598d93acdf4649bee3ad3aadbac25e923bb94b4e529ff558E2FCD"
BOARD_ID = "vQYgiQ8t"


def get_all_cards(board_id):
    url_cards = f"https://api.trello.com/1/boards/{board_id}/cards"
    query = {
        'key': API_KEY,
        'token': TOKEN
    }
    headers = {
        "Accept": "application/json"
    }

    response_cards = requests.get(url_cards, headers=headers, params=query)
    if response_cards.status_code == 200:
        cards = response_cards.json()
    else:
        print(f"Error fetching cards: {response_cards.status_code}")
        return

    for card in cards:
        card_id = card['id']
        list_id = card['idList']
        url_card_details = f"https://api.trello.com/1/cards/{card_id}"
        response_card_details = requests.get(url_card_details, headers=headers, params=query)
        if response_card_details.status_code == 200:
            card_details = response_card_details.json()

            extracted_data = {
                "list_id": list_id,
                "card_id": card_id,
                "title": card_details.get("name"),
                "description": card_details.get("desc"),
                "label": card_details.get("labels", []),
                "cover_color": card_details.get("cover", {}).get("color", "No cover color")
            }
            print(json.dumps(extracted_data, sort_keys=True, indent=4, separators=(",", ": ")))
        else:
            print(f"Error fetching details for card {card_id}: {response_card_details.status_code}")
# get_all_cards(BOARD_ID)


def create_card(title, description):
    url = f"https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }
    query = {
        'key': API_KEY,
        'token': TOKEN,
        'name': title,
        'desc': description,
        'idList': '664a76a32bd00ccff6b9696c'
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )
    if response.status_code == 200:
        print("Success")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


create_card("Kartica 4", "Opis kartice 4")
