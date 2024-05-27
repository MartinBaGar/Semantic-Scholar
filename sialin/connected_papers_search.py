import requests
import time

# bib_file = "ConnectedPapers-for-A-dual-diffusion-model-enables-3D-molecule-generation-and-lead-optimization-based-on-target-pockets.bib"
bib_file = "ConnectedPapers-for-PocketFlow-is-a-data_20and_20knowledge_20driven-structure_20based-molecular-generative-model.bib"

semantic_ids = []

with open(bib_file, 'r') as file:
    for line in file:
        if line.startswith('url'):
            url = line.split('{')[1].split('}')[0]
            id = url.split('/')[-1]
            semantic_ids.append(id)


# Define the API endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/'

#Define which details about the paper you would like to receive in the response
paperDataQueryParams = {'fields': 'title,abstract,tldr'}

for id in semantic_ids:
  success = False
  while not success:
    response = requests.get(url + id, params=paperDataQueryParams)
    if response.status_code == 200:
      response = response.json()
      print("success")
      with open('results.md', 'a') as file:
        file.write(f"# {response['title']}\n\n")
        file.write(f"Abstract: {response['abstract']}\n\n")
        file.write(f"TLDR: {response['tldr']}\n\n")
      success = True
    else:
      print(f"response failed with errorcode:{response.status_code}")
      time.sleep(5)
