# Survey Data Schema

This document describes the final, cleaned schema for the survey data.

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | INT | Unique identifier for the student. |
| `major` | VARCHAR(50) | The student's major/field of study. |
| `GPA` | FLOAT | The student's grade point average (0.0-4.0 scale). |
| `is_cs_major` | BOOL | Boolean indicating if the student is a Computer Science major. |
| `credits_taken` | FLOAT | Total number of credits the student has taken. |