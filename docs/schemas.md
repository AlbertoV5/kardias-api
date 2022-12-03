# Schemas

## Patient

### POST Request
```json
{
  "amount": 20,
  "page": 0,
  "columns": {
    "gender": {
      "min": 0,
      "max": 1
    },
    "age_days": {
      "min": 0,
      "max": 36500
    },
    "weight_kg": {
      "min": 0,
      "max": 200
    },
    "height_cm": {
      "min": 0,
      "max": 2000
    },
    "cx_previous": {
      "min": 0,
      "max": 10
    },
    "date_birth": {
      "min": "1900-01-01",
      "max": "2100-01-01"
    },
    "date_procedure": {
      "min": "2000-01-01",
      "max": "2100-01-01"
    },
    "rachs": {
      "min": 1,
      "max": 6
    },
    "stay_days": {
      "min": 0,
      "max": 500
    },
    "expired": {
      "min": 0,
      "max": 1
    }
  }
}
```

### Response

```json
[
  {
    "patient_id": 0,
    "gender": 0,
    "age_days": 0,
    "weight_kg": 0,
    "height_cm": 0,
    "cx_previous": 0,
    "date_birth": "2022-12-03",
    "date_procedure": "2022-12-03",
    "rachs": 0,
    "stay_days": 0,
    "expired": 0
  }
]
```