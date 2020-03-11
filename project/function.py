import sklearn
from sklearn.model_selection import train_test_split






def split_data(df):
    """
    split df into .7 train, .15 val, 15 test
    """

    train, test = train_test_split(df, test_size=.15)

    train, val = train_test_split(df, test_size=.15)

    return train, test, val







def target_features(target):
    """
    target = target from the dataframe
    """
    target = target
    features = train.columns.drop(target)

    x_train = train[features]
    y_train = train[target]

    x_val = val[features]
    y_val = val[target]

    x_test = test[features]
    y_test = test[target]

    return x_train, y_train, x_val, y_val, x_test, y_test






def describe_nunique(df):
    """
    describe method including nunique for numeric descriptions
    """
    df_described = df.describe(include='number').T
    df_described['unique'] = df.select_dtypes(include='number').nunique()
    return df_described[['count', 'unique', 'mean', 'std', 'min', 'max', '25%', '50%', '75%']]






def describe_other(df):
    """
    describe method including other descriptors not included in describe()
    """
    data = {
      'type' : df.dtypes,
      'unique' : df.nunique(),
      'count' : df.notnull().sum(),
      'nulls' : df.isnull().sum(),
      'mode' : [f'{df[column].mode()[0]}' for column in df.columns]
  }
    return pd.DataFrame(data)


