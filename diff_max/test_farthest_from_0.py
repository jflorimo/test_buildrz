def get_farthest_from_0(number_list):
    if not number_list:
        return None
    min_num, max_num = min(number_list), max(number_list)
    if abs(min_num)>= max_num:
        return min_num
    else:
        return max_num

assert get_farthest_from_0(range(-9000, 8000)) == -9000
assert get_farthest_from_0(range(-500, 8000)) == 7999
assert get_farthest_from_0(range(5)) == 4
