def search(lis, leading_char,  limit):
    result = []  # you need to have something so you can put your result in an empty list

    for word in lis:
        if word[0] == leading_char and len(word)<limit:
            result.append(word)
    return result


print(search(["Apple", "Banana", "Ball", "App", "Basketball"], "B", 5))
