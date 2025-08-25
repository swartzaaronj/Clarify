import json

#Indexes:
#   0: Timestamp (endTime)
#   1: Artist (artistName)
#   2: Song Title (trackName)
#   3: Time Streamed (ms.) (msPlayed)

def parse_json_file(targets):
    output = []
    for a in targets:
        try:
            with open(a, 'r', encoding="utf8") as file:
                json_string = file.read()
                parsed_data = json.loads(json_string)
                output.append(parsed_data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error parsing JSON file: {e}")
            return None
    return output

def parse_dict(passed_dict):
    intermediateArray = []
    for value in passed_dict.values():
        if isinstance(value, int) and value < 10000:
            return None
        #Filters out all streams that were less than ten seconds long.
        if value == "Unknown Track" or value == "Unknown Artist":
            return None
        intermediateArray.append(value)
    return intermediateArray

def format_data(parsed_data):
    formatted_list = []
    # Assumes parsed_data is structured as a two-dimensional array
    for a in parsed_data:
        for b in a:
            # Assumes items in parsed_data[a] are structured as dicts
            b = parse_dict(b)
            if b:
                formatted_list.append(b)        
    return formatted_list

def most_streamed(data, index):
    tListIndex = index - 1
    trackList = [[], [], []]
    for a in data:
        try:
            trackIndex = trackList[tListIndex].index(a[index])
            trackList[2][trackIndex] += a[3]
        except:
            trackList[0].append(a[1])
            trackList[1].append(a[2])
            trackList[2].append(a[3])
    longestStreamed = trackList[2].index(max(trackList[2]))
    return [trackList[0][longestStreamed], trackList[1][longestStreamed], trackList[2][longestStreamed]]

def print_data_plain(data):
    for streamstat in data:
        print(f"{streamstat[0]}: Streamed {streamstat[2]} by {streamstat[1]} for {streamstat[3]} ms.")

def most_streamed_song(data):
    mostStreamed = most_streamed(data, 2)
    streamTime = convert_time(mostStreamed[2])
    return f"Your most streamed song this year was {mostStreamed[1]} by {mostStreamed[0]}. You streamed it for a total of {streamTime[0]} hours, {streamTime[1]} minutes, and {streamTime[2]} seconds."

def most_streamed_artist(data):
    mostStreamed = most_streamed(data, 1)
    streamTime = convert_time(mostStreamed[2])
    return f"Your most streamed artist this year was {mostStreamed[0]}. You streamed them for a total of {streamTime[0]} hours, {streamTime[1]} minutes, and {streamTime[2]} seconds."

def convert_time(ms):
    hours = 0
    minutes = 0
    seconds = 0
    if ms >= 3600000:
        hours = (ms - ms % 3600000) / 3600000
        ms = ms % 3600000
    if ms >= 60000:
        minutes = (ms - ms % 60000) / 60000
        ms = ms % 60000
    if ms >= 1000:
        seconds = (ms - ms % 1000) / 1000
    return [int(hours), int(minutes), int(seconds)]

# ================STOP HERE, VERY IMPORTANT!!!================
target_jsons = ["./StreamingHistory0.json"]
# The parser expects the target director(ies) to be inside of an array.
# This script was designed with scalability in mind. If you have more JSONS, you can append them!
# There are more robust ways of finding out the amount of target files, but this script was made in about two hours, three years ago, and hasn't been touched since.
parsed_data = parse_json_file(target_jsons)
formatted_data = format_data(parsed_data)
choice = input("1: Raw Data\n2: Most Streamed Song\n3: Most Streamed Artist\n")
while choice not in ["1", "2", "3"]:
    choice = input("1: Raw Data\n2: Most Streamed Song\n3: Most Streamed Artist\n")
if choice == "1":
    print_data_plain(formatted_data)
elif choice == "2":
    print(most_streamed_song(formatted_data))
elif choice == "3":
    print(most_streamed_artist(formatted_data))

most_streamed_artist(formatted_data)
