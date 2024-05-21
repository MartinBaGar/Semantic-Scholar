import requests
import json

# Define the API endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

# More specific query parameter
query_params = {
    'query': 'sialin',
    'fields': 'title,abstract,tldr,citationCount',
}

# Directly define the API key (Reminder: Securely handle API keys in production environments)
api_key = 'ZmGnIfcVmW6e3VJ3YOfr68xse88DZoo7aM4grcZq'  # Replace with the actual API key

# Define headers with API key
headers = {'x-api-key': api_key}

# Initialize an empty list to hold all results
all_results = []

# Loop until all results are retrieved
while True:
    # Send the API request
    response = requests.get(url, params=query_params, headers=headers)

    # Check response status
    if response.status_code == 200:
        response_data = response.json()
        
        # Add the results to the list if citationCount >= 10
        for paper in response_data['data']:
            if paper['citationCount'] >= 50:
                all_results.append(paper)

        # Check if there are more results
        if 'next' in response_data:
            query_params['offset'] = response_data['next']  # Update the offset for the next request
        else:
            break  # No more results, exit the loop
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        break  # Exit the loop in case of an error

# Sort all_results by citationCount in descending order
all_results_sorted = sorted(all_results, key=lambda paper: paper['citationCount'], reverse=True)

# Write the sorted results to a Markdown file
with open('results.md', 'w') as f:
    for paper in all_results_sorted:
        f.write(f"# {paper['title']}\n\n")
        f.write("## Abstract\n")
        f.write(f"{paper['abstract']}\n\n")
        f.write("## Summary\n")
        f.write(f"{paper['tldr']}\n\n")
        f.write("## Citation Count\n")
        f.write(f"{paper['citationCount']}\n\n")