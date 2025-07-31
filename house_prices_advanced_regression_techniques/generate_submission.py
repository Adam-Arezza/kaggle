from joblib import load
import numpy as np
import pandas as pd
from sklearn.cross_decomposition import PLSRegression


df = pd.read_csv('test.csv')

def preProcess_data(df):
    # perform the same processing as the training set
    df = pd.get_dummies(df)
    df.fillna(int(df["LotFrontage"].mean()), inplace=True)
    df.drop(columns=['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF'], inplace=True)
    df["TotalSF"] = df["1stFlrSF"] + df["2ndFlrSF"] + df["TotalBsmtSF"]
    df.drop(columns=['1stFlrSF', '2ndFlrSF'], inplace=True)
    unique_ms_subclass = list(pd.unique(df["MSSubClass"]))
    for i in range(len(df)):
        df["MSSubClass"][i] = unique_ms_subclass.index(df["MSSubClass"][i])
    return df


def main():
    data = preProcess_data(test_data)
    print(data.shape)
    print(data.columns)
    # model = load('house_price_pls.joblib')
    # ids = data["Id"]
    # data.drop(columns=["Id"], inplace=True)
    # data = data.to_numpy()
    # predictions = model.predict(data)

    # submission = pd.DataFrame()
    # submission["Id"] = ids
    # submission["SalePrice"] = predictions.flatten()
    # print(submission.head(10))


if __name__ == "__main__":
    main()
