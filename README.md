# igWhoFollowsBack
igWhoFollowsBack is a Python script that prints a list of users who don't follow you back on Instagram. This used to be a builtin feature on Instagram, however it no longer is so I decided to make this program.

## Instructions
First you'll need to download your profile information from https://accountscenter.instagram.com/info_and_permissions/dyi/. Select your Instagram profile if prompted and click on `Export to device`. Under `Customize information` you can select only `Followers and following`. For `Date range` you'll want to use `All time` to ensure that all desired data is present. For `Format` select `JSON`. The Media quality setting does not matter.

Once you've downloaded your information, you'll need to run:
```
git clone https://github.com/carsonchapman1123/igWhoFollowsBack
```

Open main.py in the igWhoFollowsBack directory and set followers_path and following_path variables to the file paths of your followers and following json files. I personally moved those files into the igWhoFollowsBack directory so that I could use just the file names as the paths.

Then run:
```
python main.py
```
and you should see a printed list of users who you follow but do not follow you back.

This program could be modified to show users who follow you but you don't follow back by adding the lines
```
you_dont_follow_back = list(followers - following)
print("Followers who you don't follow back:")
for x in you_dont_follow_back:
    print(x)
```
however this is already a builtin feature on Instagram.