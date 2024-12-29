import joblib
from data_loader import load_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_data("model_data.csv", "preprocessed", True)

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=25)

model = LogisticRegression()

model.fit(X_train, y_train)

joblib.dump(model, "model/model.pkl")
joblib.dump(X_test, "model/X_test.pkl")
joblib.dump(y_test, "model/y_test.pkl")