

import sklearn 
from sklearn.model_selection import train_test_split

class ease:
    def __init__(self):
        pass

    def split_data(self, df):
        self.df = df
        """
        split df into .7 train, .15 val, 15 test
        """
        self.train, self.test = train_test_split(self.df, test_size=.15)
        self.train, self.val = train_test_split(self.df, test_size=.15)
        return self.train, self.test, self.val

        def target_features(self, target):
        """
        target = target from the dataframe
        """
        self.target = target
        self.features = self.train.columns.drop(target)

        self.x_train = self.train[self.features]
        self.y_train = self.train[self.target]

        self.x_val = self.val[self.features]
        self.y_val = self.val[self.target]

        self.x_test = self.test[self.features]
        self.y_test = self.test[self.target]

        return self.x_train, self.y_train, self.x_val, self.y_val, self.x_test, self.y_test

    
    def describe_nunique(self, df):
        """
        describe method including nunique for numeric descriptions
        """
        self.df_described = self.df.describe(include='number').T
        self.df_described['unique'] = self.df.select_dtypes(include='number').nunique()
        return self.df_described[['count', 'unique', 'mean', 'std', 'min', 'max', '25%', '50%', '75%']]


    def describe_other(self, df):
        """
        describe method including other descriptors not included in describe()
        """
        self.data = {
                'type' : self.df.dtypes,
                'unique' : self.df.nunique(),
                'count' : self.df.notnull().sum(),
                'nulls' : self.df.isnull().sum(),
                'mode' : [f'{self.df[column].mode()[0]}' for column in self.df.columns]
                }
        return pd.DataFrame(self.data)



