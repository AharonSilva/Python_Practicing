# Args and Kwargs function exercises!


def multiply(*b):
    product = 1
    if len(b) == 1:
        product = b[0]
    else:
        for _i in b:
            product *= _i
    return product


def congratulations(pm, tester, *devs):
    print("Happy New Year! Take care of yourself and your loved ones!\nFor:")
    print(f"{pm}\n{tester}")
    for dev in devs:
        print(dev)


def final_deposit_amount(*interest, amount=1000):
    for rate in interest:
        amount += amount * rate / 100
    return round(amount, 2)


def say_bye(**names):
    for name in names:
        print("Au revoir,", name)
        print("See you on", names[name]["next appointment"])
        print()


humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}

tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love",
                   "Seventeen Seconds": "A Forest"}}


def tracklist(**dict_tracks):
    for artist, albums in dict_tracks.items():
        print(artist)
        for album in albums.items():
            print(f"ALBUM: {album[0]} TRACK: {album[1]}")
    return ""


