# API Documentation

## Endpoints

### 1. POST /rates/

| **Field**            | **Details**                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------|
| **Description**       | Upload a JSON file with rate data for different cargo types.                                           |
| **Request**           | Multipart/form-data                                                                                   |
| **File (required)**   | Type: `UploadFile`, Description: JSON file containing rate data (must be a `.json` file).              |
| **Request Body (Example)** | ```json { "2024-11-01": [{ "cargo_type": "electronics", "rate": 1.23 }, { "cargo_type": "clothing", "rate": 0.75 }], "2024-11-02": [{ "cargo_type": "electronics", "rate": 1.25 }] } ``` |
| **Responses**         | **200 OK**: `{ "message": "Rates successfully added." }` <br> **400 Bad Request**: `{ "detail": "File must be a JSON file" }` <br> **500 Internal Server Error**: `{ "detail": "Error adding rates: <error_message>" }` |
  
---

### 2. POST /calculate/

| **Field**               | **Details**                                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| **Description**          | Calculate the insurance cost based on declared value and cargo type using the latest rate for that cargo. |
| **Request**              | `application/json`                                                                                     |
| **Body (required)**      | `cargo_type` (string): Type of cargo, `rate_date` (string, date format "YYYY-MM-DD"): Rate date, `declared_value` (float): Declared value. |
| **Request Body (Example)** | ```json { "cargo_type": "electronics", "rate_date": "2024-11-01", "declared_value": 1000.00 } ``` |
| **Responses**            | **200 OK**: ```json { "cargo_type": "electronics", "rate": 1.23, "declared_value": 1000.00, "insurance_cost": 1230.00, "date": "2024-11-01" } ``` <br> **404 Not Found**: `{ "detail": "Rate not found for the given date and cargo type" }` <br> **400 Bad Request**: `{ "detail": "Invalid JSON file" }` |
