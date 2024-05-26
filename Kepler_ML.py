import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Define a function to clean the CSV file
def clean_csv(file_path, output_path, expected_columns):
    cleaned_lines = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.count(',') == expected_columns - 1: 
                cleaned_lines.append(line)
    
    with open(output_path, 'w') as f:
        f.writelines(cleaned_lines)

# Clean the CSV file
kepler_data_url = "D:\\WebScrapping_AI_ML\\kepler_data.csv"
cleaned_data_url = "D:\\WebScrapping_AI_ML\\cleaned_kepler_data.csv"
expected_columns = 49 
clean_csv(kepler_data_url, cleaned_data_url, expected_columns)

# cleaned Kepler data
kepler_data = pd.read_csv(cleaned_data_url)

# features and target variable
X = kepler_data.drop(columns=['koi_disposition'])
y = kepler_data['koi_disposition']

X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier()

# Fit the model on the training data
rf_classifier.fit(X_train, y_train)

# Predict the target variable
predictions = rf_classifier.predict(X_test)

# accuracy Calculation
accuracy = accuracy_score(y_test, predictions)


print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, predictions))
