from youtube_search import YoutubeSearch

# Perform a search
results = YoutubeSearch('Delhi travel vlogs', max_results=1).to_dict()

# Extract the video link
video_link = f"https://www.youtube.com/watch?v={results[0]['id']}"

print("YouTube Video Link:", video_link)
