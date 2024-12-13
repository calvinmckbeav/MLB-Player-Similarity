import pandas as pd

# excel path
file_path = "Stats.xlsx"

# Read file
try:
    players_data = pd.read_excel(file_path).fillna(0)
    print("Excel file successfully read.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")



def getPlayerByID(pid):
    return players_data[players_data['Player ID'] == pid]

def getPlayerByName(playername):
    return players_data[players_data['Player Name'].str.lower() == playername.lower()]

#takes string for name, returns print statement for end cases, or returns playerID
def nameCheck(query):
    result = getPlayerByName(query)
    if result.empty:
        # no player message
        print("No player exists in 2024 named " + query.title())
        exit()
    elif result.shape[0] > 1:
        # choice if multiple players by name
        print(result)
        row = int(input(f"Multiple players with name {query}, enter row number of desired player: "))
        result = result.iloc[row-1]
        if (result['Games Played'] == 0).any():
            print(query.title() + ", " + str(result.iloc[2]) + ", " + str(result.iloc[4]) + ": did not play in 2024")
            exit()
        else:
            return result.iloc[0]
    elif (result['Games Played'] == 0).any():
        # did not play message
        print(query.title() + ", " + str(result.iloc[0,2]) + ", " + str(result.iloc[0,4]) + ": did not play in 2024")
        exit()
    else:
        return result.iloc[0,0]
        
# takes in one row of player info, returns formatted string
def formatOriginalPlayer(oneRow):
    string = ""
    string += str(oneRow.iloc[0,1]) + ", "
    string += str(oneRow.iloc[0,3]) + ", "
    string += str(oneRow.iloc[0,4]) + ":\n"
    # pitcher or batter
    if oneRow.iloc[0,2] == 'P':
        string += "Production:\n"
        string += "  " + str(oneRow.iloc[0, 5]) + " Games Played, "
        string += "  " + str(oneRow.iloc[0,19]) + " Innings Pitched.\n"
        string += "Efficiency:\n"
        string += "  " + str(oneRow.iloc[0,20]) + " ERA, "
        string += "  " + str(oneRow.iloc[0,16]) + " Strikeouts.\n"
        string += "Results:\n"
        string += "  " + str(oneRow.iloc[0,21]) + " Wins, "
        string += "  " + str(oneRow.iloc[0,22]) + " Losses, "
        string += "  " + str(oneRow.iloc[0,23]) + " Saves, "
        string += "  " + str(oneRow.iloc[0,24]) + " Blown Saves."
    else:
        string += "Production:\n"
        string += "  " + str(oneRow.iloc[0,5]) + " Games Played, "
        string += "  " + str(oneRow.iloc[0,13]) + " Homeruns, "
        string += "  " + str(oneRow.iloc[0,16]) + " Strikeouts.\n"
        string += "Efficiency:\n"
        string += "  " + str(oneRow.iloc[0,25]) + " BA, "
        string += "  " + str(oneRow.iloc[0,28]) + " OPS.\n"
        string += "Results:\n"
        string += "  " + str(oneRow.iloc[0,14]) + " Steals, "
        string += "  " + str(oneRow.iloc[0,8]) + " Runs, "
        string += "  " + str(oneRow.iloc[0,9]) + " RBIs."
    print(string + '\n')

# takes in one row of player info, returns formatted string
def formatComparedPlayer(orig, comp):
    string = ""
    string += str(comp.iloc[0,1]) + ", "
    string += str(comp.iloc[0,3]) + ", "
    string += str(comp.iloc[0,4]) + ":\n"
    # pitcher or batter
    if comp.iloc[0,2] == 'P':
        string += "Production:\n"
        string += "  " + str(comp.iloc[0, 5]) + " Games Played (" + str(round(comp.iloc[0,5] - orig.iloc[0,5],3)) + "), "
        string += "  " + str(comp.iloc[0,19]) + " Innings Pitched (" + str(round(comp.iloc[0,19] - orig.iloc[0,19],3)) + ").\n"
        string += "Efficiency:\n"
        string += "  " + str(comp.iloc[0,20]) + " ERA (" + str(round(comp.iloc[0,20] - orig.iloc[0,20],3)) + "), "
        string += "  " + str(comp.iloc[0,16]) + " Strikeouts (" + str(round(comp.iloc[0,16] - orig.iloc[0,16],3)) + ").\n"
        string += "Results:\n"
        string += "  " + str(comp.iloc[0,21]) + " Wins (" + str(round(comp.iloc[0,21] - orig.iloc[0,21],3)) + "), "
        string += "  " + str(comp.iloc[0,22]) + " Losses (" + str(round(comp.iloc[0,22] - orig.iloc[0,22],3)) + "), "
        string += "  " + str(comp.iloc[0,23]) + " Saves (" + str(round(comp.iloc[0,23] - orig.iloc[0,23],3)) + "), "
        string += "  " + str(comp.iloc[0,24]) + " Blown Saves (" + str(round(comp.iloc[0,24] - orig.iloc[0,24],3)) + ")."
    else:
        string += "Production:\n"
        string += "  " + str(comp.iloc[0,5]) + " Games Played (" + str(round(comp.iloc[0,5] - orig.iloc[0,5],3)) + "), "
        string += "  " + str(comp.iloc[0,13]) + " Homeruns (" + str(round(comp.iloc[0,13] - orig.iloc[0,13],3)) + "), "
        string += "  " + str(comp.iloc[0,16]) + " Strikeouts (" + str(round(comp.iloc[0,16] - orig.iloc[0,16],3)) + ").\n"
        string += "Efficiency:\n"
        string += "  " + str(comp.iloc[0,25]) + " BA (" + str(round(comp.iloc[0,25] - orig.iloc[0,25],3)) + "), "
        string += "  " + str(comp.iloc[0,28]) + " OPS (" + str(round(comp.iloc[0,28] - orig.iloc[0,28],3)) + ").\n"
        string += "Results:\n"
        string += "  " + str(comp.iloc[0,14]) + " Steals (" + str(round(comp.iloc[0,14] - orig.iloc[0,14],3)) + "), "
        string += "  " + str(comp.iloc[0,8]) + " Runs (" + str(round(comp.iloc[0,8] - orig.iloc[0,8],3)) + "), "
        string += "  " + str(comp.iloc[0,9]) + " RBIs (" + str(round(comp.iloc[0,9] - orig.iloc[0,9],3)) + ")."
    print(string + '\n')

#formatOriginalPlayer(getPlayer("Aaron Hicks"))
#formatComparedPlayer(getPlayer("Aaron Hicks"), getPlayer("Aaron Judge"))


# takes two pitchers and gives simScore
def comparePitchers(qplayer, nplayer):
    score = 0
    score += abs(qplayer.iloc[0,5] - nplayer.Games_Played)
    score += abs(qplayer.iloc[0,20]*100 - nplayer.ERA*100)
    score += abs(qplayer.iloc[0,19] - nplayer.Innings_Pitched)
    score += abs(qplayer.iloc[0,16] - nplayer.Strikeouts)
    score += abs(qplayer.iloc[0,21] - nplayer.Wins)/2
    score += abs(qplayer.iloc[0,22] - nplayer.Losses)/2
    score += abs(qplayer.iloc[0,23] - nplayer.Saves) * 5
    score += abs(qplayer.iloc[0,24] - nplayer.Blown_Saves) * 5
    return score
# takes two Batters and gives simScore
def compareBatters(qplayer, nplayer):
    score = 0
    if qplayer.iloc[0,5] < 10:
        score += abs(qplayer.iloc[0,5] - nplayer.Games_Played) * 2
        score += abs(qplayer.iloc[0,25]*100 - nplayer.BA*100)
        score += abs(qplayer.iloc[0,28]*100 - nplayer.OPS*100)
        score += abs(qplayer.iloc[0,13]-nplayer.Homeruns) * 2
        score += abs(qplayer.iloc[0,16]- nplayer.Strikeouts) *2
        score += abs(qplayer.iloc[0,14]- nplayer.Steals)
        score += abs(qplayer.iloc[0,8]- nplayer.Runs)
        score += abs(qplayer.iloc[0,9]- nplayer.RBIs)
    else:
        score += abs(qplayer.iloc[0,5] - nplayer.Games_Played)
        score += abs(qplayer.iloc[0,25]*1000 - nplayer.BA*1000)
        score += abs(qplayer.iloc[0,28]*1000 - nplayer.OPS*1000)
        score += abs(qplayer.iloc[0,13]-nplayer.Homeruns)
        score += abs(qplayer.iloc[0,16]- nplayer.Strikeouts)/2
        score += abs(qplayer.iloc[0,14]- nplayer.Steals)/2
        score += abs(qplayer.iloc[0,8]- nplayer.Runs)/2
        score += abs(qplayer.iloc[0,9]- nplayer.RBIs)/2
    return score

# the grand function
def findSimilar(playerName):
    id = nameCheck(playerName)
    player = getPlayerByID(id)
    # trimmed DF based on position
    if player.iloc[0,2] == 'P':
        df = players_data[
            (players_data["Position"] == 'P') &
            (players_data['Innings Pitched'] >= (player.iloc[0,19] - 50)) &
            (players_data['Innings Pitched'] <= (player.iloc[0,19] + 50)) &
            (players_data['ERA'] >= (player.iloc[0,20] - 0.5)) &
            (players_data['ERA'] <= (player.iloc[0,20] + 0.5))
                ]
        if df.shape[0] < 6:
            df = players_data[
            (players_data["Position"] == 'P') &
            (players_data['Innings Pitched'] >= (player.iloc[0,19] - 10)) &
            (players_data['Innings Pitched'] <= (player.iloc[0,19] + 10))
                ]
    else:
        df = players_data[
            (players_data["Position"] != 'P') &
            (players_data['Games Played'] >= (player.iloc[0,5] - 50)) &
            (players_data['Games Played'] <= (player.iloc[0,5] + 50)) &
            (players_data['BA'] >= (player.iloc[0,25] - 0.05)) &
            (players_data['BA'] <= (player.iloc[0,25] + 0.05))
                ]
        if df.shape[0] < 6:
            df = players_data[
            (players_data["Position"] != 'P') &
            (players_data['Games Played'] >= (player.iloc[0,5] - 50)) &
            (players_data['Games Played'] <= (player.iloc[0,5] + 50)) &
            (players_data['BA'] >= (player.iloc[0,25] - 0.2)) &
            (players_data['BA'] <= (player.iloc[0,25] + 0.2))
            ]
    df.columns = df.columns.str.replace(' ', '_')
    df.fillna(0)
    # player ID : similarity score (0-8)
    simScores = {}
    for index, row in df.iterrows():
        if player.iloc[0,2] == 'P':
            simScores[row['Player_ID']] = comparePitchers(player,row)
        else:
            simScores[row['Player_ID']] = compareBatters(player,row)
            
    sorted_dict= dict(sorted(simScores.items(), key=lambda item: item[1], reverse=False))
    formatOriginalPlayer(getPlayerByID(id))
    for key in list(sorted_dict.keys())[1:6]:
        formatComparedPlayer(getPlayerByID(id), getPlayerByID(key))
    
findSimilar('blair henley')


