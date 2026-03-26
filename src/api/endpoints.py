BASE = "https://americas.api.riotgames.com"

def account(game_name, tag):
    return f"{BASE}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag}"

def matches(puuid):
    return f"{BASE}/lol/match/v5/matches/by-puuid/{puuid}/ids"

def match_detail(match_id):
    return f"{BASE}/lol/match/v5/matches/{match_id}"