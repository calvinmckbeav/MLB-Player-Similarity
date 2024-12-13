import requests
import pandas as pd

formatted_data = []
# Replace with your API key
API_KEY = "f838d60a9e3b11ef"

# Base URL
BASE_URL = "http://rest.datafeeds.rolling-insights.com/api/v1/player-stats/2024/MLB?RSC_token=f838d60a9e3b11ef&team_id="


for i in range(1,31):
    # Make the API request
    response = requests.get(BASE_URL+f"{i}")

    # Check for successful response
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
    else:
        print(f"Error: {response.status_code}, {response.text}")

    mlb_data = data['data']['MLB']

    # Loop through each player and extract relevant details
    for player in mlb_data:
        if player["position"] == "P":
            player_info = {
                "Player ID": player["player_id"],
                "Player Name": player["player"],
                "Position": player["position"],
                "Position Category": player["position_category"],
                "Team": player["team"],
                "Games Played": player.get("regular_season", {}).get("games_played", 0),
                #Pitching
                "Innings Pitched": player.get("regular_season", {}).get("pitching", {}).get("IP"),
                "ERA": player.get("regular_season", {}).get("pitching", {}).get("ERA"),
                "Strikeouts": player.get("regular_season", {}).get("pitching", {}).get("K"),
                "Hits": player.get("regular_season", {}).get("pitching", {}).get("H"),
                "Walks": player.get("regular_season", {}).get("pitching", {}).get("BB"),
                "Hit By Pitch": player.get("regular_season", {}).get("pitching", {}).get("HBP"),
                "Wins": player.get("regular_season", {}).get("pitching", {}).get("W"),
                "Losses": player.get("regular_season", {}).get("pitching", {}).get("L"),
                "Saves": player.get("regular_season", {}).get("pitching", {}).get("S"),
                "Blown Saves": player.get("regular_season", {}).get("pitching", {}).get("BS"),
            }
        else: 
            player_info = {
                "Player ID": player["player_id"],
                "Player Name": player["player"],
                "Position": player["position"],
                "Position Category": player["position_category"],
                "Team": player["team"],
                "Games Played": player.get("regular_season", {}).get("games_played", 0),
                #batting
                "At Bats": player.get("regular_season", {}).get("batting", {}).get("AB"),
                "Hits": player.get("regular_season", {}).get("batting", {}).get("H"),
                "Runs": player.get("regular_season", {}).get("batting", {}).get("R"),
                "RBIs": player.get("regular_season", {}).get("batting", {}).get("RBI"),
                "Singles": player.get("regular_season", {}).get("batting", {}).get("1B"),
                "Doubles": player.get("regular_season", {}).get("batting", {}).get("2B"),
                "Triples": player.get("regular_season", {}).get("batting", {}).get("3B"),
                "Homeruns": player.get("regular_season", {}).get("batting", {}).get("HR"),
                "Steals": player.get("regular_season", {}).get("batting", {}).get("SB"),
                "Walks": player.get("regular_season", {}).get("batting", {}).get("BB"),
                "Strikeouts": player.get("regular_season", {}).get("batting", {}).get("SO"),
                "Hit By Pitch": player.get("regular_season", {}).get("batting", {}).get("HBP"),
                "Intentional Walks": player.get("regular_season", {}).get("batting", {}).get("IBB"),
            }
        formatted_data.append(player_info)

# Create a DataFrame
df = pd.DataFrame(formatted_data)

# Display the DataFrame
print(df)

# Output results to an Excel file
with pd.ExcelWriter('All Players.xlsx') as writer:
    df.to_excel(writer, sheet_name='Players DB', index=False)