def append(list1:list, list2:list) ->list:
    return [*list1, *list2]


def concat(lists:list) ->list:
    rl = []
    for l in lists:
        rl.extend(l)
    return rl


def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    """...Or just len(list)
    """
    return sum(1 for i in list)


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    a = initial
    for i in list:
        a = function(a, i)
    return a


def foldr(function, list, initial):
    a = initial
    for i in list[::-1]:
        a = function(a, i)
    return a


def reverse(list):
    return list[::-1]
