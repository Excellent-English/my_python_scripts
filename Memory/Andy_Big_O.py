# wersja slow = O(n^2), wersja fast = O(n)
def has_duplicates_slow(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


def my_version_has_duplicates_fast(items):
    unique = set()
    for i in range(len(items)):
        if i in unique:
            return True
        unique.add(i)
    return False

# --------------------------------------------------------------------------------------------

# wersja slow = O(n), wersja fast = O(1)
def user_exists_slow(users, target):
    for user in users:
        if user == target:
            return True
    return False


def user_exists_fast(users, target):
    group = set(users)
    if target in group:
        return True
    return False

def user_exists_fast2(users, target):
    group = set(users)
    return target in group


# --------------------------------------------------------------------------------------------

def common_slow(list_a, list_b):
    result = []

    for a in list_a:
        for b in list_b:
            if a == b:
                result.append(a)

    return result

# result = [1,1,1]


def common_fast(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    result = set_a.intersection(set_b)
    return result


def common_fast_single_line(list_a, list_b):
    return set(list_a).intersection(set(list_b))

# set(list_a) = {1,4,6}
# set(list_b) = {1,2,3,7,9}
# return {1}



# --------------------------------------------------------------------------------------------


def remove_duplicates_slow(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result

def remove_duplicates_fast():
    items = ["Stefan", "Piotr", "Andy", "Stefan", "Kasia"]
    print(dict.fromkeys(items))
    return list(dict.fromkeys(items))

remove_duplicates_fast()