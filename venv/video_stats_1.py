import requests 
import json

API_KEY = "AIzaSyCi26rkfKgB2p03qjDqsGl-Ll8y16Zoqbg"
CHANNEL_HANDLE = "@MrBeast"

# Step 1: Get channel ID from handle
url_channel = f"https://www.googleapis.com/youtube/v3/channels?part=id&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
response_channel = requests.get(url_channel)
channel_data = response_channel.json()

print("Channel Response:")
print(json.dumps(channel_data, indent=4))

if channel_data.get('items'):
    channel_id = channel_data['items'][0]['id']
    print(f"\nChannel ID: {channel_id}")
    
    # Step 2: Search for videos using channel ID
    url_search = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=5&type=video&key={API_KEY}"
    response_search = requests.get(url_search)
    search_data = response_search.json()
    
    print("\nSearch Response:")
    print(json.dumps(search_data, indent=4))
    
    # Step 3: Extract video IDs
    video_ids = []
    if 'items' in search_data:
        for item in search_data['items']:
            video_ids.append(item['id']['videoId'])
    
    print(f"\nFound Video IDs: {video_ids}")
    
    # Step 4: Get CONTENT DETAILS for each video
    if video_ids:
        ids_string = ','.join(video_ids)
        url_details = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,snippet&id={ids_string}&key={API_KEY}"
        response_details = requests.get(url_details)
        details_data = response_details.json()
        
        print("\nVideo Content Details:")
        print(json.dumps(details_data, indent=4))
else:
    print("Channel not found")