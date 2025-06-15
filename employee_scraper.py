import requests
import pandas as pd

# Constants
API_URL = "https://api.example.com/employees"

# Fetch employee data
def fetch_employee_data(url):
    """
    Fetch employee data from the provided API URL.
    """
    print("Fetching employee data...")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Normalize employee data
def normalize_employee_data(raw_data):
    """
    Normalize employee data to a structured DataFrame.
    """
    print("Normalizing data...")
    df = pd.DataFrame(raw_data)

    # Combine first and last names, handling missing values
    df["Full Name"] = df.apply(
        lambda row: f"{row['first_name']} {row['last_name']}" if pd.notna(row['last_name']) else row['first_name'],
        axis=1
    )

    # Normalize phone numbers
    df["phone"] = df["phone"].apply(lambda x: x if x.isdigit() else "Invalid")

    # Fill missing values
    df = df.fillna("Missing")

    return df

# Save data to CSV
def save_to_csv(df, filename):
    """
    Save the DataFrame to a CSV file.
    """
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
