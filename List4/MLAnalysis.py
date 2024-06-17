
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load the dataset
file_path = 'List4/t-shirts.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())
print(data.describe(include='all'))

# Set up the matplotlib figure
plt.figure(figsize=(15, 10))

# Size distribution
plt.subplot(2, 3, 1)
sns.countplot(data['size'])
plt.title('Size Distribution')

# Material distribution
plt.subplot(2, 3, 2)
sns.countplot(data['material'])
plt.title('Material Distribution')

# Color distribution
plt.subplot(2, 3, 3)
sns.countplot(data['color'])
plt.title('Color Distribution')

# Sleeves distribution
plt.subplot(2, 3, 4)
sns.countplot(data['sleeves'])
plt.title('Sleeves Distribution')

# Demand distribution
plt.subplot(2, 3, 5)
sns.countplot(data['demand'])
plt.title('Demand Distribution')

plt.tight_layout()
plt.show()

# Encode categorical features
data_encoded = pd.get_dummies(data, columns=['size', 'material', 'color', 'sleeves'])

# Split the data into features and target variable
X = data_encoded.drop('demand', axis=1)
y = data_encoded['demand']

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Normalization
scaler = MinMaxScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_val_normalized = scaler.transform(X_val)

# Standardization
scaler = StandardScaler()
X_train_standardized = scaler.fit_transform(X_train)
X_val_standardized = scaler.transform(X_val)

# PCA
pca = PCA(n_components=0.95)  # Retain 95% of the variance
X_train_pca = pca.fit_transform(X_train_standardized)
X_val_pca = pca.transform(X_val_standardized)

# Handle missing values 
X_train_missing = X_train.copy()
X_val_missing = X_val.copy()

# Introduce missing values
np.random.seed(42)
missing_mask = np.random.rand(*X_train_missing.shape) < 0.05
X_train_missing[missing_mask] = np.nan

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train_missing)
X_val_imputed = imputer.transform(X_val_missing)

X_train_sets = {
    'original': X_train,
    'normalized': X_train_normalized,
    'standardized': X_train_standardized,
    'pca': X_train_pca,
    'imputed': X_train_imputed
}

X_val_sets = {
    'original': X_val,
    'normalized': X_val_normalized,
    'standardized': X_val_standardized,
    'pca': X_val_pca,
    'imputed': X_val_imputed
}

# Define classifiers
nb = GaussianNB()
dt1 = DecisionTreeClassifier(max_depth=5, random_state=42)
dt2 = DecisionTreeClassifier(max_depth=10, random_state=42)
dt3 = DecisionTreeClassifier(max_depth=15, random_state=42)

classifiers = {
    'Naive Bayes': nb,
    'Decision Tree (max_depth=5)': dt1,
    'Decision Tree (max_depth=10)': dt2,
    'Decision Tree (max_depth=15)': dt3
}

results = {}

# Train and evaluate classifiers
for name, clf in classifiers.items():
    results[name] = {}
    for set_name, X_train_set in X_train_sets.items():
        clf.fit(X_train_set, y_train)
        y_pred = clf.predict(X_val_sets[set_name])
        results[name][set_name] = classification_report(y_val, y_pred, output_dict=True)

# Additional classifiers with varied hyperparameters
additional_classifiers = {
    'Decision Tree (max_depth=5, criterion=entropy)': DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=42),
    'Decision Tree (max_depth=20)': DecisionTreeClassifier(max_depth=20, random_state=42),
    'Random Forest (n_estimators=200)': RandomForestClassifier(n_estimators=200, random_state=42),
    'Random Forest (n_estimators=50, max_depth=10)': RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42),
    'SVM (kernel=rbf)': SVC(kernel='rbf', random_state=42),
    'SVM (C=0.1)': SVC(C=0.1, kernel='linear', random_state=42)
}

# Train and evaluate classifiers
for name, clf in additional_classifiers.items():
    results[name] = {}
    for set_name, X_train_set in X_train_sets.items():
        clf.fit(X_train_set, y_train)
        y_pred = clf.predict(X_val_sets[set_name])
        results[name][set_name] = classification_report(y_val, y_pred, output_dict=True)

# Extract accuracy scores for updated results
updated_accuracy_scores = {
    classifier: {prep_method: results[classifier][prep_method]['accuracy'] for prep_method in results[classifier]}
    for classifier in results
}

# Convert to DataFrame
updated_accuracy_df = pd.DataFrame(updated_accuracy_scores).T

# Plot updated heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(updated_accuracy_df, annot=True, cmap='Reds', cbar=True)
plt.title('Classifier Accuracy Across Different Data Preparation Methods (Extended)')
plt.xlabel('Data Preparation Method')
plt.ylabel('Classifier')
plt.show()
