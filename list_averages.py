lst = [-5,-3]
def list_averages(lst):
    positive = []
    odd = []

    for num in lst:
        if num > 0:
            positive.append(num)

        if num % 2 != 0:
            odd.append(num)

    if len(positive) > 0:
        positive_avg = sum(positive) / len(positive)   

    else: 
       positive_avg = None

    if len(odd) > 0:
        odd_avg = sum(odd) / len(odd)
    else: 
        odd_avg = None

    return positive_avg, odd_avg

print(list_averages(lst))