CREATE TABLE IF NOT EXISTS matches (
    match_id TEXT PRIMARY KEY,
    queue_id INTEGER,
    game_duration INTEGER
);

CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id TEXT,
    puuid TEXT,
    champion TEXT,
    team_id INTEGER,
    role TEXT,
    win INTEGER,

    kills INTEGER,
    deaths INTEGER,
    assists INTEGER,

    vision_score INTEGER,
    wards_placed INTEGER,
    wards_killed INTEGER,

    gold_earned INTEGER,
    damage INTEGER,

    total_minions_killed INTEGER,
    neutral_minions_killed INTEGER
);