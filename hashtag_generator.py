def generate_hashtag(s):
    return "".join(['#'] + [i.capitalize() for i in s.split()])


print(generate_hashtag(input("Enter text:\n>")))
