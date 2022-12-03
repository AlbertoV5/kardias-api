# General

## Description

The objective of a REST API is to tie together all services involved in performing Data Analytics and Machine Learning for internal and end-users. The characteristics of the API are:

- Use async processes to provide a smoother user experience.
- Call external services and resources to perform complex/blocking tasks.
- A single two-way connection to the SQL database for consistency.
- Provide user authentication.

## Requirements

### Data Lake Connectivity

1. Read a CSV file and store it in Amazon S3
2. Get a list of CSV files stored in Amazon S3

### ETL / ML Connectivity

1. Ask another service to process a CSV file from Amazon S3.
2. Read Patient data and tell another service to perform ML.

### Perform CRUD Operations

1. Create or Update Patient data.
2. Read from Patient id.
3. Delete from Patient id.

### Admin Tasks

1. Create a new User with a name, API key and privilege.
2. Perform database maintenance (remove orphans, verify metadata).