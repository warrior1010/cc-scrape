import requests
import concurrent.futures
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL certificate verification warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Get the file name from the user
file_name = input("Enter the name of the text file containing URLs: ")

# Open the file and read the URLs
with open(file_name, "r") as file:
    urls = file.read().splitlines()

# Function to check Laravel presence for a single URL
def check_laravel(url):
    try:
        # Add "https://" if not present in the URL
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        # Disable SSL certificate verification
        response = requests.get(url, verify=False, timeout=5)
        
        # Check if the response contains the "laravel_session" or "laravel_token" cookie
        if "laravel_session" in response.cookies or "laravel_token" in response.cookies:
            # Write the URL to the file instantly
            with open("laravel.txt", "a") as output_file:
                output_file.write(url + "\n")
            return True  # Return True if Laravel is found
        else:
            return False  # Return False if Laravel is not found
    except requests.exceptions.RequestException as e:
        print(f"{url} --> Error with URL")
        return False

# Use ThreadPoolExecutor to run the URL checks concurrently with 100 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Submit each URL check task to the executor
    future_to_url = {executor.submit(check_laravel, url): url for url in urls}

    # Process the completed tasks
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            result = future.result()  # Get the result of the task
            if result:
                print(f"{url} --> Found Laravel")
            else:
                print(f"{url} --> No Laravel")
        except Exception:
            print(f"{url} --> Error with URL")
