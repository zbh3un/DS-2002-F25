import csv

# Create the messy dataset with type inconsistencies
data = [
    ['student_id', 'major', 'GPA', 'is_cs_major', 'credits_taken'],
    [1, 'Computer Science', 3.8, 'Yes', '120.5'],
    [2, 'Biology', 3, 'No', '95.0'],
    [3, 'Engineering', 3.5, 'Yes', '110'],
    [4, 'Mathematics', 4, 'No', '105.5'],
    [5, 'Computer Science', 3.2, 'Yes', '98']
]

# Write to CSV file
with open('raw_survey_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'raw_survey_data.csv' created successfully!")


import json

# Task 2: Create hierarchical JSON data
courses = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "DS2003",
        "section": "001",
        "title": "Communicating with Data",
        "level": 200,
        "instructors": [
            {"name": "Antonios Mamalakis", "role": "Primary"}
        ]
    },
    {
        "course_id": "PSYC 4260",
        "section": "001",
        "title": "Epigenetic research",
        "level": 300,
        "instructors": [
            {"name": "Jessica Connelly", "role": "Primary"},
            {"name": "Taylor", "role": "TA"}
        ]
    }
]

# Write to JSON file
with open('raw_course_catalog.json', 'w') as file:
    json.dump(courses, file, indent=2)

print("JSON file 'raw_course_catalog.json' created successfully!")

import pandas as pd

# Task 3: Clean and Validate the CSV Data
print("\n--- Task 3: Cleaning CSV Data ---")

# 1. Load the CSV into a DataFrame
df = pd.read_csv('raw_survey_data.csv')
print("Original DataFrame:")
print(df)
print("\nOriginal data types:")
print(df.dtypes)

# 2. Enforce Boolean Type: Convert is_cs_major from 'Yes'/'No' to True/False
df['is_cs_major'] = df['is_cs_major'].replace({'Yes': True, 'No': False})

# 3. Enforce Numeric Type: Convert GPA and credits_taken to float
df = df.astype({'GPA': 'float64', 'credits_taken': 'float64'})

print("\nCleaned DataFrame:")
print(df)
print("\nCleaned data types:")
print(df.dtypes)

# 4. Save the cleaned DataFrame to a new CSV file
df.to_csv('clean_survey_data.csv', index=False)
print("\nCleaned data saved to 'clean_survey_data.csv'!")

# Task 4: Normalize the JSON Data
print("\n--- Task 4: Normalizing JSON Data ---")

# 1. Load the JSON file
with open('raw_course_catalog.json', 'r') as file:
    courses_data = json.load(file)

print("Original JSON data loaded:")
print(courses_data)

# 2. Normalize: Flatten the hierarchical data, extracting the nested instructors list
df_normalized = pd.json_normalize(
    courses_data,
    record_path=['instructors'],
    meta=['course_id', 'title', 'level', 'section']
)

print("\nNormalized DataFrame:")
print(df_normalized)

# 3. Save the normalized DataFrame to a CSV file
df_normalized.to_csv('clean_course_catalog.csv', index=False)
print("\nNormalized data saved to 'clean_course_catalog.csv'!")