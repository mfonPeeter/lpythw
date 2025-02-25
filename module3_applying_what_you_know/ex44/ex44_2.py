def talk(who, words):
    print(f"I am {who['name']} and {words}")

becky = {
    "name": "Becky",
    "age": 34,
    "eyes": "green",
    "talk": talk
}

becky['talk'](becky, "I am talking here!")