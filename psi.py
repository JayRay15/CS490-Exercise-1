import requests

# API endpoint
url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

# Data 
data = {
    "UCID": "JMR",  
    "first_name": "Jarnel",
    "last_name": "Rancy",
    "github_username": "JayRay15",
    "discord_username": "jahlah3000",
    "favorite_cartoon": "Star Wars: The Clone Wars",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Destiny 2",
    "section": "103"
}

# Send POST request
response = requests.post(url, json=data)

# Print results
print("Status Code:", response.status_code)
print("Response:", response.text)
