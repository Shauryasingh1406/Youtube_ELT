import requests 
import json
API_KEY="AIzaSyCi26rkfKgB2p03qjDqsGl-Ll8y16Zoqbg"
CHANNEL_HANDLE="MrBeast"
url = f"https://youtube.googleapis.com/youtube/v3/videos?part=ContentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
response = requests.get(url)  
print(response);

data = response.json()
print(data)
json.dumps(data, indent=4)
print(json.dumps(data, indent=4))

#import requests 
#import json

#API_KEY = "AIzaSyCi26rkfKgB2p03qjDqsGl-Ll8y16Zoqbg"
#CHANNEL_HANDLE = "@MrBeast"

# Step 1: Search for videos from the channel
#url_search = f"https://www.googleapis.com/youtube/v3/search?part=snippet&forHandle={CHANNEL_HANDLE}&maxResults=5&key={API_KEY}"
#response_search = requests.get(url_search)
#search_data = response_search.json()

#print("Search Response:")
#print(json.dumps(search_data, indent=4))

# Step 2: Extract video IDs
#video_ids = []
#if 'items' in search_data:
 #   for item in search_data['items']:
  #      if 'videoId' in item.get('id', {}):
   #         video_ids.append(item['id']['videoId'])

#print(f"\nFound Video IDs: {video_ids}")

# Step 3: Get statistics for each video
#if video_ids:
 #   ids_string = ','.join(video_ids)
  #  url_stats = f"https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&id={ids_string}&key={API_KEY}"
   # response_stats = requests.get(url_stats)
    #stats_data = response_stats.json()
    
    #print("\nVideo Statistics:")
    #print(json.dumps(stats_data, indent=4))
#else:
 #   print("No videos found")