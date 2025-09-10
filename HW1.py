import requests

# API endpoint
url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

# Data 
data = {
    "UCID": "jmr",  
    "first_name": "Jarnel",
    "last_name": "Rancy",
    "github_username": "JayRay15",
    "discord_username": "jahlah3000",
    "favorite_cartoon": "Star Wars: The Clone Wars",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Destiny 2",
    "section": "103"
}
#error handling
try:
    response = requests.post(url, json=data, timeout=10)

    # Check for HTTP status
    if response.status_code == 200:
        print("Your Data has been Successfully submitted!")
        
        check_url = f"{url}?UCID={data['UCID']}&section={data['section']}"
        check_response = requests.get(check_url, timeout=10)

        if check_response.status_code == 200:
            print(" Verification successful! Record was found:")
            print(check_response.json())
        else:
            print(f" Could not verify record (status {check_response.status_code})")
            print("Details:", check_response.text)
        
    else:
        print(f" Request failed status: {response.status_code}")
        print("Details:", response.text)

except requests.exceptions.Timeout:
    print(" Error: The request timed out. Try again .")
except requests.exceptions.ConnectionError:
    print(" Error: Failed to connect. Check the internet or the API URL.")
except requests.exceptions.RequestException as e:
    print(" An unexpected error occurred:", e)
