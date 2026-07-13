import random
import webbrowser

genres = [
    {
        "name": "Heavy Metal",
        "moods": ["frustrated", "suppressed"],
        "message": "you were probably annoyed at something today",
        "url": "https://www.youtube.com/results?search_query=heavy+metal+playlist",
    },
    {
        "name": "Lo-fi Hip Hop",
        "moods": ["tired", "procrastinating"],
        "message": "you have things to do but youre definitely not doing them",
        "url": "https://www.youtube.com/results?search_query=lofi+hip+hop+playlist",
    },
    {
        "name": "Classical",
        "moods": ["melancholic", "reflective"],
        "message": "you didnt really feel like talking to anyone today",
        "url": "https://www.youtube.com/results?search_query=classical+music+playlist",
    },
    {
        "name": "Pop",
        "moods": ["energetic", "attention-seeking"],
        "message": "you are in a good mood or at least trying to be",
        "url": "https://www.youtube.com/results?search_query=pop+hits+playlist",
    },
    {
        "name": "R&B",
        "moods": ["emotional", "nostalgic"],
        "message": "someone is on your mind",
        "url": "https://www.youtube.com/results?search_query=rnb+chill+playlist",
    },
    {
        "name": "Punk",
        "moods": ["irritated", "rebellious"],
        "message": "you are mad at something and dont really want to calm down yet",
        "url": "https://www.youtube.com/results?search_query=punk+rock+playlist",
    },
    {
        "name": "Jazz",
        "moods": ["relaxed", "unbothered"],
        "message": "you are just chilling, nothing special going on",
        "url": "https://www.youtube.com/results?search_query=jazz+chill+playlist",
    },
    {
        "name": "Trap",
        "moods": ["tense", "unsettled"],
        "message": "something feels off today but you cant really explain it",
        "url": "https://www.youtube.com/results?search_query=trap+music+playlist",
    },
]


def find_genre(genre_list, user_input):
    for i in range(len(genre_list)):
        if user_input.isdigit():
            if i + 1 == int(user_input):
                return genre_list[i]
        else:
            if genre_list[i]["name"].lower() == user_input.lower():
                return genre_list[i]
    return random.choice(genre_list)


def show_help():
    print("")
    print("type a number or the genre name")
    print("the program will guess your mood based on what youre listening to")
    print("at the end you can open a youtube playlist")
    print("")


print("")
print("music mood diagnosis")
print("")

for i in range(len(genres)):
    print(str(i + 1) + ". " + genres[i]["name"])

print("")

choice = input("what are you listening to right now? (h for help): ").strip()

if choice.lower() == "h":
    show_help()
    choice = input("pick a number or type the name: ").strip()

picked = find_genre(genres, choice)
mood = random.choice(picked["moods"])

print("")
print("genre: " + picked["name"])
print("mood:  " + mood)
print("")
print(picked["message"])
print("")

open_playlist = input("open a playlist? (y/n): ").strip().lower()

if open_playlist == "y":
    webbrowser.open(picked["url"])

print("")
