def word_count(s):
    cache = {}
    removed_letters = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', "|", '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for letter in removed_letters:
        s = s.replace(letter, "")

    # print("String: ", s)
    for word in s.split():
        if word.lower() not in cache:
            cache[word.lower()] = 1
        else: 
            cache[word.lower()] += 1

    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))