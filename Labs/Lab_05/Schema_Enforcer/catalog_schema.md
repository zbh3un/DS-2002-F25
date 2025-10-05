# Course Catalog Schema

This document describes the final, normalized schema for the course catalog data.

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `name` | VARCHAR(100) | Name of the instructor. |
| `role` | VARCHAR(20) | Role of the instructor (e.g., Primary, TA). |
| `course_id` | VARCHAR(20) | Unique identifier for the course. |
| `title` | VARCHAR(100) | Title/name of the course. |
| `level` | INT | Course level (e.g., 200, 300). |
| `section` | VARCHAR(10) | Section number of the course. |