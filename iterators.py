from email import iterators


list_instance = [1, 2, 3, 4]
iterator = iter(list_instance)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("list ended")
        break

iterator = (val for val in range(1, 20+1) if 20 % val == 0)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("list ended")
        break
