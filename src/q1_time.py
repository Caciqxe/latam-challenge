from typing import List, Tuple
from datetime import datetime
from collections import Counter, defaultdict
from functions import read_json

#the defaul file_path argument needed was deleted so i can store it inside just one function, instead of passing it as an argument for every question
def q1_time() -> List[Tuple[datetime.date, str]]:
    file_name = "farmers-protest-tweets-2021-2-4.json"
    json_folder = "json"
    tweets = read_json(file_name, json_folder, date=True, user=True, content=False)
    top_ten_dates = Counter([d['date'] for d in tweets]).most_common(10)
    ranking = [date[0] for date in top_ten_dates]
    
    matching_elements = [el for el in tweets if el['date'] in [d[0] for d in top_ten_dates]]

    user_counts = defaultdict(Counter)
    for d in matching_elements:
        date = d['date']
        user = d['user']
        user_counts[date][user] += 1

    most_repeated_user_per_date = {date: user_counter.most_common(1)[0][0] for date, user_counter in user_counts.items()}

    return [(date, most_repeated_user_per_date[date]) for date in ranking]

if __name__ == "__main__":
    print(q1_time())