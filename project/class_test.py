

import sklearn 
from sklearn.model_selection import train_test_split

class Ease:
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

