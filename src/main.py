import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

BASE_URL = "https://americas.api.riotgames.com"


def get_puuid(game_name, tag_line):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()["puuid"]


def get_matches(puuid):
    url = f"{BASE_URL}/lol/match/v5/matches/by-puuid/{puuid}/ids"
    headers = {"X-Riot-Token": API_KEY}

    params = {
        "start": 0,
        "count": 10,
        "queue": 420  # ranked soloq
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()

def get_match_details(match_id):
    url = f"{BASE_URL}/lol/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()

def get_my_participant(match_data, puuid):
    participants = match_data["info"]["participants"]

    for p in participants:
        if p["puuid"] == puuid:
            return p

    return None

def extract_basic_stats(participant):
    return {
        "champion": participant["championName"],
        "role": participant.get("teamPosition"),
        "win": participant["win"],
        "kills": participant["kills"],
        "deaths": participant["deaths"],
        "assists": participant["assists"],
        "visionScore": participant["visionScore"],
        "wardsPlaced": participant["wardsPlaced"],
        "wardsKilled": participant["wardsKilled"],
        "gameDuration": participant["timePlayed"]
    }

if __name__ == "__main__":
    game_name = "eku"
    tag_line = "sadge"

    puuid = get_puuid(game_name, tag_line)
    matches = get_matches(puuid)

    for match_id in matches:
        match_data = get_match_details(match_id)

        participant = get_my_participant(match_data, puuid)
        stats = extract_basic_stats(participant)

        print(f"{stats['champion']} | {'WIN' if stats['win'] else 'LOSS'} | {stats['role']} | "
              f"{stats['kills']}/{stats['deaths']}/{stats['assists']} | Vision: {stats['visionScore']}")