from typing import List, Tuple
from collections import Counter
from functions import read_json
import re

#the defaul file_path argument needed was deleted so i can store it inside just one function, instead of passing it as an argument for every question
def q3_time() -> List[Tuple[str, int]]:
    file_name = "farmers-protest-tweets-2021-2-4.json"
    json_folder = "json"
    tweets = read_json(file_name, json_folder, date=False, user=False, content=True)

    usernames = []
    for tweet in tweets:
        usernames.extend(re.findall(r'@(\w+)', tweet))

    return [(user, count) for user, count in Counter(usernames).most_common(10)]

if __name__ == "__main__":
    print(q3_time())