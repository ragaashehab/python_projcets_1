# recursive binary search.
# Returns index of x in arr if present, else -1
# binary_search(list ,start_idx, end_idx , item):

def search(list ,s_idx, e_idx , item):
    mid_idx = s_idx + (e_idx - s_idx) // 2
    if list[mid_idx] == item:
        return mid_idx
    if mid_idx < s_idx or e_idx < s_idx:
        return  -1
    if list[mid_idx] > item:  # "list[mid_idx] > item"
        return (search(list, s_idx, mid_idx-1, item))
    elif list[mid_idx] < item: # "list[mid_idx] < item"
        return (search(list, mid_idx+1, e_idx, item))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr1 = [6, 9, 2, 7, 22, 8, 1, 83, 90]
    arr2 = [33, 6, 9, 2, 7, 22, 8, 1, 83, 90]
    item = 83
    arr1= sorted(arr1)
    idx= search(arr1, 0, (len(arr1)-1) ,item)
    if idx == -1:
        print("{} is not exist".format(item))
    else:
        print("{} exist at {}".format(item , idx))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
