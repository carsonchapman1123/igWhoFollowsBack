import json


followers_path = "followers_1.json"
following_path = "following.json"

with open(followers_path, 'r', encoding='utf-8') as file:
    followers = json.load(file)

with open(following_path, 'r', encoding='utf-8') as file:
    following = json.load(file)


followers = {x["string_list_data"][0]["value"] for x in followers}
following = {x["title"] for x in following["relationships_following"]}
not_following_back = list(following - followers)


print("Users not following you back:")
for x in not_following_back:
    print(x)
