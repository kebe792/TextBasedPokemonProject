import pandas as pd

def FetchSave_Data(SaveFile = "save_game.csv"):
    
    Saves = pd.read_csv(SaveFile)
    
    return Saves