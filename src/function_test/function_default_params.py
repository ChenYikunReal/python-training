def print_list(a, reverse=False):
    if (reverse):
        for i in a[-1::-1]:
            print(i)
    else:
        for i in a:
            print(i)


a = [1, 2, 3, 4, 5]
print_list(a)
print("---------------------------------------")
print_list(a, reverse=True)
