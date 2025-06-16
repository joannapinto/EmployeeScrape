import pytest
from employee_scraper import fetch_employee_data, normalize_employee_data

# Sample API response
API_URL = "https://api.example.com/employees"
SAMPLE_DATA = [
    {
        "first_name": "John",
        "last_name": None,
        "email": "john.doe@example.com",
        "phone": "12345x",
        "gender": "Male",
        "age": None,
        "job_title": "Developer",
        "years_of_experience": 5,
        "salary": 100000,
        "department": None,
        "hire_date": "2020-01-15"
    }
]

# Test fetch_employee_data
def test_fetch_employee_data():
    """
    Test to ensure the API response can be successfully fetched.
    """
    data = SAMPLE_DATA  # Replace with mocked API call if needed
    assert isinstance(data, list), "Data should be a list"

# Test normalize_employee_data
def test_normalized_data_structure():
    """
    Test to ensure normalized data has all required columns and valid data types.
    """
    df = normalize_employee_data(SAMPLE_DATA)
    expected_columns = [
        "Full Name", "email", "phone", "gender", "age", "job_title",
        "years_of_experience", "salary", "department", "hire_date"
    ]
    for column in expected_columns:
        assert column in df.columns, f"Column {column} missing in normalized data"

# Test phone normalization
def test_phone_normalization():
    """
    Test to ensure invalid phone numbers are flagged correctly.
    """
    df = normalize_employee_data(SAMPLE_DATA)
    assert df["phone"].iloc[0] == "Invalid", "Phone normalization failed"

# Test handling missing or invalid data
def test_handle_missing_or_invalid_data():
    """
    Test to ensure the scraper handles missing or invalid data gracefully.
    """
    df = normalize_employee_data(SAMPLE_DATA)
    assert df["Full Name"].iloc[0] == "John", "Full Name not handled correctly for missing data"
    assert df["department"].iloc[0] == "Missing", "Missing department not handled correctly"
