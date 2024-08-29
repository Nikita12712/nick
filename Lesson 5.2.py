import string


def generate_hashtag(input_string):

    cleaned_string = ''.join(char for char in input_string if char not in string.punctuation).replace(" ", "")

    words = cleaned_string.split()

    capitalized_words = [word.capitalize() for word in words]

    hashtag = '#' + ''.join(capitalized_words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


print(generate_hashtag("hello world"))
print(generate_hashtag("python! programming, is awesome."))  

