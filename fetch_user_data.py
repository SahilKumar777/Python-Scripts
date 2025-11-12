"""
Script Name: fetch_user_data.py

Description: Fetch data from a public API and display it in a readable format by looping through each user and displays the
following details:
• Name
• Username
• Email
• City (from address.city).

Author: Sahil Kumar
Date: 2025-11-11
"""

## Imports
import requests

## Functions
def fetch_json(url, params=None, timeout=10):
    """
    Fetch JSON data from a given URL using HTTP GET.

    Args:
        url (str): The API endpoint.
        params (dict, optional): Query parameters for the request.
        timeout (int, optional): Timeout in seconds for the request.

    Returns:
        dict or list: Parsed JSON data if successful.
        None: If request fails or JSON is invalid.
    """
    try:
        # Send GET request
        response = requests.get(url, params=params, timeout=timeout)

        # Raise an error for bad HTTP status codes (4xx, 5xx)
        response.raise_for_status()

        # Parse JSON safely
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except ValueError:
        print("Error: Response is not valid JSON.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None

def print_user_data(user_data):
    """
    Prints user data(json) into readable format.

    Args:
        user_data (json): The json data fetched from the API.

    Returns:

    """
    print(f"User {user_data['id']} : ")
    print("\tName : ",user_data['name'])
    print("\tUsername : ",user_data['username'])
    print("\tEmail : ",user_data['email'])
    print("\tCity : ",user_data['address']['city'])
    print("")


def print_city_based_user_data(json_data):
    """
    Prints user data whose city name starts with "S".

    Args:
        json_data (json): The json data fetched from the API.

    Returns:

    """
    for user_data in json_data:
      if user_data['address']['city'][0] == 'S' :
        print_user_data(user_data)


## Main (Execution)
if __name__ == "__main__":
    # Example API (public placeholder API)
    api_url = "https://jsonplaceholder.typicode.com/users"

    # Fetch JSON data
    json_data = fetch_json(api_url, params={})

    if json_data is not None:
        print("Fetched JSON data successfully!")
        # Print first item for demonstration
        if isinstance(json_data, list) and json_data:
            print("Printing all users data... \n")
            for user_data in json_data:
              print_user_data(user_data)

            print("\nPrinting only user details whose city name starts with letter 's'")
            print_city_based_user_data(json_data)
        else:
            print_user_data(json_data)
    else :
      print("No Data Fetched")
