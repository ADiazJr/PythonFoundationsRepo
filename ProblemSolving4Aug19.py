
def task1():
    some_list = [5, 17, 77 , 50]
    index_target_finder(some_list, 51)

def index_target_finder(list, target_number):
    list_og = len(list)
    for item in range(len(list)):
        for item2 in range(len(list)):
            sum = 0
            sum = list[item] +list[item2+1]
            list.append(sum)
            if target_number in list:
                return True
            elif (item2 +1) == list_og:
                return False


task1()
    