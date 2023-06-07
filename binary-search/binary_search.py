def find(search_list, value, start=0):
    if not search_list:
        raise ValueError("value not in array")
    mid = len(search_list) // 2
    if search_list[mid] == value:
        return mid + start
    if search_list[mid] > value:
        return find(search_list[:mid], value, start)
    return find(search_list[mid + 1 :], value, start + mid + 1)
