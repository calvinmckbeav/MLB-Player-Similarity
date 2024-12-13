import pandas as pd

# excel path
file_path = "All Players.xlsx"

# Read file
try:
    players_data = pd.read_excel(file_path)
    print("Excel file successfully read.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# BA column
players_data['BA'] = round(players_data['Hits'] / players_data['At Bats'], 3)
# OBP column
players_data['OBP'] = round((players_data['Hits'] + players_data['Walks'] + players_data['Hit By Pitch']) / (players_data['At Bats'] + players_data['Walks'] + players_data['Hit By Pitch']),3)
# SLG column
players_data['SLG'] = round(((players_data['Singles']) + (players_data['Doubles']*2) + (players_data['Triples']*3) + (players_data['Homeruns']*4)) / players_data['At Bats'],3)
# OPS column
players_data['OPS'] = round(players_data['OBP'] + players_data['SLG'],3)


# Output results to an Excel file
with pd.ExcelWriter('Stats.xlsx') as writer:
    players_data.to_excel(writer, sheet_name='Players DB', index=False)