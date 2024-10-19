# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler
# import pickle
# import pandas
# import warnings
# warnings.filterwarnings('ignore')
#
# df = pandas.read_csv('web_ready.csv')
# ds = pandas.read_csv('web_ready.csv')
#
# features_to_normalize = ['founded_at',  'funding_total_usd', 'milestones', 'closed_at_year', 'duration_days', 'log_funding_total_usd']
# scaler = MinMaxScaler()
# df[features_to_normalize] = scaler.fit_transform(df[features_to_normalize])
#
# min_values = {}
# max_values = {}
# ranges = {}
#
# for feature in features_to_normalize:
#   min_values[feature] = ds[feature].min()
#   max_values[feature] = ds[feature].max()
#   ranges[feature] = max_values[feature] - min_values[feature]
#
# ds[features_to_normalize] = scaler.fit_transform(ds[features_to_normalize])
#
# df.drop('status',axis=1, inplace=True)


# Logistic Regression
# X_df = df.drop('isClosed', axis=1)
# y_df = df['isClosed']
# X_train_df, X_test_df, y_train_df, y_test_df = train_test_split(X_df, y_df, test_size=0.2, random_state=109)
# logistic_model = LogisticRegression()
# logistic_model.fit(X_train_df, y_train_df)
# y_pred_df = logistic_model.predict(X_test_df)
# logistic_accuracy = accuracy_score(y_test_df, y_pred_df)
# print("Logistic Regression Accuracy:", logistic_accuracy*100)

# Random Forest
# X_ds = ds.drop('status', axis=1)
# y_ds = ds['status']
# X_train_ds, X_test_ds, y_train_ds, y_test_ds = train_test_split(X_ds, y_ds, test_size=0.2, random_state=42)
# random_forest_model = RandomForestClassifier()
# random_forest_model.fit(X_train_ds, y_train_ds)
# y_pred_ds = random_forest_model.predict(X_test_ds)
# random_forest_accuracy = accuracy_score(y_test_ds, y_pred_ds)
# print("Random Forest Accuracy:", random_forest_accuracy*100)
# print()
# print()