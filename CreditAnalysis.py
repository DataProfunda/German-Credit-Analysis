import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split
from MultiClassifierModule import MultiClassifier

#Read csv file
df = pd.read_csv("ger_creditability.csv")

target = df['Creditability']

df = df.drop('Creditability', axis=1)


#Outliers detection with GaussianMixture#
gm = GaussianMixture( n_components=len(df.columns), n_init=10 )

gm.fit(df)

densities = gm.score_samples(df)

density_threshold = np.percentile(densities, 4)

#inliers = df[densities >= density_threshold]
outliers = df[densities < density_threshold] #Detected outliers

df = pd.DataFrame(df).drop(outliers.index) #Drop outliers 
target = pd.DataFrame(target).drop(outliers.index) #Drop outliers

print('Detected anomalies: ', len(outliers))

X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.15)

multi_clf = MultiClassifier(X_train, X_test, y_train, y_test,n_repetition=10)

multi_clf.compile_fit()

multi_clf.evaluate()
