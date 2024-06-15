from typing import List, Tuple
from collections import Counter
import emoji
from functions import read_json, get_emojis

#the defaul file_path argument needed was deleted so i can store it inside just one function, instead of passing it as an argument for every question
def q2_time() -> List[Tuple[str, int]]:
    file_name = "farmers-protest-tweets-2021-2-4.json"
    json_folder = "json"
    tweets = read_json(file_name, json_folder, date=False, user=False, content=True)
    emoji_counter = Counter()

    for text in tweets:
        emojis = get_emojis(text)
        emoji_counter.update(emojis)

    return [(emoji.emojize(emoji_symbol), count) for emoji_symbol, count in emoji_counter.most_common(10)]
    
if __name__ == "__main__":
    print(q2_time())