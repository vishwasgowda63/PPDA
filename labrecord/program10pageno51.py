import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
df = pd.read_csv("laptops.csv")  # Ensure this file is in your working directory

# Print the columns to verify
print("Columns in dataset:", df.columns)

# Check if expected columns exist
if 'Operating System' not in df.columns or 'Storage' not in df.columns:
    raise ValueError("Expected columns 'Operating System' and 'Storage' not found in dataset.")

# OneHotEncoder for Operating System
one_hot_encoder = OneHotEncoder(sparse=False, drop='first', handle_unknown='ignore')
os_encoded = one_hot_encoder.fit_transform(df[['Operating System']])
os_encoded_df = pd.DataFrame(os_encoded, columns=one_hot_encoder.get_feature_names_out(['Operating System']))

# LabelEncoder for Storage
label_encoder = LabelEncoder()
df['Storage_Label'] = label_encoder.fit_transform(df['Storage'])

# Combine encoded OS with original data (excluding original 'Operating System')
df_encoded = pd.concat([df.drop(['Operating System'], axis=1), os_encoded_df], axis=1)

# Show the result
print("\nEncoded Data Sample:")
print(df_encoded.head())
