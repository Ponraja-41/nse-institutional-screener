import pandas as pd

df = pd.DataFrame({
    "SYMBOL":["RELIANCE","INFY"],
    "OPEN":[1500,1800],
    "HIGH":[1525,1815],
    "LOW":[1490,1790],
    "CLOSE":[1518,1810],
    "VOLUME":[2500000,1800000]
})

df.to_csv("data/bhavcopy.csv",index=False)

print("Done")
