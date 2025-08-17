import pandas as pd
import numpy as np


class Character():
    def __init__(self):
        self.Team = pd.DataFrame(
            np.zeros((6, 4)),  # 6 rows, 4 columns of zeros
            columns=["Pokemon", "Level", "Health", "XP"]
        )