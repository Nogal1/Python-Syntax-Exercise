def print_upper_words(words):
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"])