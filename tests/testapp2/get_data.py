import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
def get_data(): 
    df = pd.read_csv("~/a2ml/tests/data/baseball.csv", delimiter=",", quotechar='"')
    # get integer labels
    le = LabelEncoder()
    le.fit(df["RS"].values)
    y = le.transform(df["Label"].values)
    df = df.drop(["RS"], axis=1)
    df_train, _, y_train, _ = train_test_split(df, y, test_size=0.1, random_state=42)
    return { "X" : df, "y" : y }