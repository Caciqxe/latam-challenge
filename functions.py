import os
import jsonlines
import emoji

from datetime import datetime
from collections import defaultdict

# This function will be used to return the list of emojis in the given string:
def get_emojis(text: str) -> list:
    return [char for char in text if char in emoji.EMOJI_DATA]


# This function will be used to return the array needed for the question.
def read_json(file_name: str, json_folder: str, date:bool, user:bool, content:bool) -> list:

    # The assumption is that the json files are in a folder called 'json' in the working directory.
    current_directory = os.path.dirname(os.path.abspath(__file__))
    json_folder_path = os.path.join(current_directory, json_folder)
    file_path = os.path.join(json_folder_path, file_name)
    
    # tweets will be the array that will be returned.
    tweets = []
    
    # Case for q1
    if date == True and user == True and content == False:
        with jsonlines.open(file_path, 'r') as f:
            for obj in f:
                date = datetime.strptime(obj['date'][:10], "%Y-%m-%d").date()
                user = obj['user']['username']
                tweets.append({'date': date, 'user': user})
        return tweets
    # Case for q2 and q3
    elif date == False and user == False and content == True:
        with jsonlines.open(file_path, 'r') as f:
            for obj in f:
                tweets.append(obj['content'])
        return tweets
    # Error case
    else:
        raise ValueError("Invalid combination of parameters. This function was created for this test, so please choose either 'date' and 'user' True with 'content' False for question 1, or 'date' and 'user' False with 'content' True for question 2 and 3 .")



