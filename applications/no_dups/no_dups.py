def no_dups(s):
    cache = {}
    for word in s.split():
        if word not in cache:
            cache[word] = "random text"
    # answer = ""
    # for key in cache.keys():
    #     answer = answer + key + " "
    # return answer
    # print("cache: ", cache)
    return " ".join(cache)
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))