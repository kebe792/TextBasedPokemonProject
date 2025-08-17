import pandas as pd
import numpy as np


class Character():
    def __init__(self):
        # Explicitly set dtypes: Pokemon is object (string), rest are numeric
        self.Team = pd.DataFrame({
            "Pokemon": ["" for _ in range(6)],
            "ID": [0 for _ in range(6)],
            "Level": [0 for _ in range(6)],
            "Health": [0 for _ in range(6)],
            "XP": [0 for _ in range(6)]
        })