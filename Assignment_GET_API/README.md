# Assignment GET API
Script Name: fetch_user_data.py

Description: Fetch data from a public API and display it in a readable format by looping through each user and displays the
following details:
* Name
* Username
* Email
* City (from address.city).

#### Author: Sahil Kumar
#### Date: 2025-11-11
---
## How to run the script [3 Methods]

### 1. Run in Google Colab (No Local Setup)

* → Click on File [FetchUserData.ipynb]

* → Click button on the top "Open in Colab"

* → Run the Cell or Click Run All.

Script will run in Google Colab.

✅ No installation needed.

⚠ Requires internet.

###################################################################
### 2. Run Locally After Cloning
Clone the repository
* git clone https://github.com/SahilKumar777/Python-Scripts.git

Go into the repo folder
* cd Python-Scripts/Assignment_GET_API
  
Run the Python script
* python3 fetch_user_data.py

✅ Works offline after cloning.

⚠ Requires Python installed locally.

###################################################################
### 3. Run Directly Without Cloning (via curl/wget)
You can fetch the raw file and pipe it to Python:

curl -s https://raw.githubusercontent.com/SahilKumar777/Python-Scripts/refs/heads/main/Assignment_GET_API/fetch_user_data.py | python3

Or:

wget -qO- https://raw.githubusercontent.com/SahilKumar777/Python-Scripts/refs/heads/main/Assignment_GET_API/fetch_user_data.py | python3

✅ Quick one-liner.

⚠ No caching — downloads every time.

###################################################################
### 💡 Recommendation:
If you just want to quickly execute a Python script without cloning, method #1 is best.

