import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    res = animals[animals['weight'] > 100]
    res = res.sort_values(by='weight', ascending=False)
    return res[['name']]
    