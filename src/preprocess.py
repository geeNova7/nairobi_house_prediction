import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

def preprocess_data(path='../data/nairobi_property_prices.csv'):
    df = pd.read_csv(path)

    #drop any ID columns
    if 'ID' in df.columns:
        df = df.drop(columns=['ID'])

    #separate target
    x = df.drop('Price',axis=1)
    y = df['Price']

    #identify feature types
    categorical = x.select_dtypes(include='object').columns
    numerical = x.select_dtypes(include=['int64','float64']).columns

    #preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num',StandardScaler(), numerical),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)
        ]
    )

    x_processed = preprocessor.fit_transform(x)

    return x_processed,y,preprocessor
