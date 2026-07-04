import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Excel dataset
data = pd.read_excel("Dataset for Data Analytics.xlsx")

print("First 5 rows:")
print(data.head())

# Remove missing values
data = data.dropna()

# Remove Date column
data = data.drop("Date", axis=1)

# Convert text columns into numbers
encoder = LabelEncoder()

for column in data.columns:
    if data[column].dtype == "object":
        data[column] = encoder.fit_transform(data[column])

# Features
X = data.drop("OrderStatus", axis=1)

# Target
y = data["OrderStatus"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy * 100)

print("\nActual Values:")
print(y_test.values[:10])

print("\nPredicted Values:")
print(predictions[:10])