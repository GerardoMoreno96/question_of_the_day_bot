import requests
import random
import os

URL = os.getenv("DISCORD_WEBHOOK_URL")

def make_http_request(question_of_the_day):
    payload = {'content': question_of_the_day}
    files = []
    headers = {}

    response = requests.request(
        "POST", URL, headers=headers, data=payload, files=files)

    print(response.text)


def get_random_row_from_random_file(directory):
    # Step 1: List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print("No files found in the directory.")
        return None

    # Step 2: Select a random file
    random_file = random.choice(files)
    file_path = os.path.join(directory, random_file)

    # Step 3: Read the selected file and retrieve a random row
    with open(file_path, 'r') as file:
        # Assuming the file contains rows of text, you can read lines and choose a random one
        lines = file.readlines()
        if not lines:
            print("Selected file is empty.")
            return None

        random_row = random.choice(lines)
        return random_row.strip()

# Example usage:
directory_path = './aws_services'
random_row = get_random_row_from_random_file(directory_path)

if random_row is not None:
    make_http_request(random_row)