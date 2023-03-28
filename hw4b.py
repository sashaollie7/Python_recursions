##################   1a   ###################
def subset_sum_count(ls, sm):
    """
    a wrapper function for a recursion function
    :param ls:  list , a given list of positive numbers
    :param sm: int , a positive number bigger then 0
    :return: int , number of combinations which are sum of the given number
    """
    return subset_sum_count_helper(ls, sm, 0)


def subset_sum_count_helper(ls, sm, idx):
    """
    a main recursion function which count how many combinations are the sum of the given number
    :param ls: list , a given list of positive numbers
    :param sm: int , a positive number bigger then 0
    :param idx: int , the index of the list
    :return:int , number of combinations which are sum of the given number
    """
    if sm == 0:  # stop condition, when the combination is valid
        return 1
    elif sm < 0 or idx == len(ls):  # stop condition , no valid combination
        return 0
    option1 = subset_sum_count_helper(ls, sm - ls[idx], idx + 1)  # choose the number
    option2 = subset_sum_count_helper(ls, sm, idx + 1)  # dont choose the number
    return option1 + option2
    ##############   1b   #####################


def subset_sums(ls, sm):
    """
    a wrapper function for a recursion function
    :param ls: list , list of natural numbers
    :param sm: int , a natural number
    :return: list , list of combinations , each combination sum equals the given number
    """
    if subset_sum_count(ls, sm) == 0:
        return []
    return subset_sums_helper(ls, sm, [], [], 0)


def subset_sums_helper(ls, sm, sm_lst, ways, idx):
    """
    a main recursion function which shows all the combinations there are in the given list
    that are the sum of the given number
    :param ls: list , list of natural numbers
    :param sm: int , a natural number
    :param sm_lst: list , a sub-list of a combination that is added to the main list
    :param ways: list, a list of the all combination lists
    :param idx: int , the index of the given list
    :return: list , list of combinations , each combination sum equals the given number
    """
    if sm == 0:
        ways.append(sm_lst)  # adds a single combination to the main list
    elif idx < len(ls) and sm > 0:
        ways = subset_sums_helper(ls, sm - ls[idx], sm_lst + [ls[idx]], ways, idx + 1)  # choose the number
        ways = subset_sums_helper(ls, sm, sm_lst, ways, idx + 1)  # dont choose the number
    return ways
    ##############   1c   #####################


def subset_sum_memo(ls, sm):
    """
    a wrapper function for a recursion function
    :param ls: list , list of natural numbers
    :param sm: int , a natural number
    :return: boolean , returns true if there is a combination that is sun of the given number
    """
    return subset_sums_memo_helper(ls, sm, 0, {})


def subset_sums_memo_helper(arr, num, idx, comb_dict):
    """
    a main recursion function with memoization which check if there is a sum combination of the given number
    :param arr: list , list of natural numbers
    :param num: int , a natural number
    :param idx: int , the index of the given list
    :param comb_dict: dict, a dictionary with a number in the list and the remain of the given number for the key
    :return: boolean , returns true if there is a combination that is sum of the given number
    """
    if num == 0:  # stop condition when there is a sum combination
        return True
    elif num < 0 or idx == len(arr):  # stop condition when there is no combination
        return False
    if (arr[idx], num) not in comb_dict:
        comb_dict[(arr[idx], num)] = subset_sums_memo_helper(arr, num - arr[idx], idx + 1, comb_dict) \
                                or subset_sums_memo_helper(arr, num, idx + 1, comb_dict)   # choose the number or not to choose
    return comb_dict[(arr[idx], num)]
    ##############   1d   #####################


def subset_sum_with_repeats(ls, sm):
    """
    a wrapper function for a recursion function
    :param ls: list , sorted list from small to big of natural numbers
    :param sm: int , a natural number
    :return: list , list of combinations , each combination sum equals the given number with repeats
    """
    if ls == []:
        return []
    return subset_sum_with_repeats_helper(ls, sm, [], [])


def subset_sum_with_repeats_helper(lst, num, combinations_lst, combination):
    """
    a main recursion function which shows all the combinations with repeats there are in the given list
    that are the sum of the given number
    :param lst: list , sorted list from small to big of natural numbers
    :param num:  int , a natural number
    :param combinations_lst: list, a list of the all combination lists
    :param combination: list , a sub-list of a combination that is added to the main list
    :return: list , list of combinations , each combination sum equals the given number with repeats
    """
    if num == 0:  # the stop condition
        combinations_lst.append(combination)
    elif num > 0:
        for cell in lst:  # a loop to add the combinations to the combination lists
            combinations_lst = subset_sum_with_repeats_helper(lst, num - cell, combinations_lst, combination + [cell])
    return combinations_lst

    ##############   2a   #####################


def abc_words(num):
    """
    a wrapper function for a recursion function
    :param num: int , the desired length of string combinations
    :return: list , list of a,b and c string combinations in Alphabetical order with the length of num
    """
    if num == 0:
        return []
    return abc_words_helper(num, [], '')


def abc_words_helper(num, comb_list, word):
    """

    :param num: num: int , the desired length of string combinations
    :param comb_list: list , the list of the string combinations
    :param word: string , the combination of the letters a,b,c
    :return: list , list of a,b and c string combinations in Alphabetical order with the length of num
    """
    if num == len(word):
        comb_list.append(word)  # adds the string to the list
    elif num > len(word):  # adds the letters in Alphabetical order
        comb_list = abc_words_helper(num, comb_list, word + 'a')
        comb_list = abc_words_helper(num, comb_list, word + 'b')
        comb_list = abc_words_helper(num, comb_list, word + 'c')
    return comb_list

    ##############   2b  #####################


def char_to_char_words(ch1, ch2, num):
    """
    a wrapper function for a recursion function
    :param ch1: string , a single letter between A and Z
    :param ch2: string , a single letter between ch1 and Z
    :param num: int, the desired length of string combinations
    :return: list , list of string combinations in Alphabetical order from ch1 to ch2 with the length of num
    """
    return char_to_char_words_helper(ord(ch1), ord(ch2), num, '', [])


def char_to_char_words_helper(start, end, num, word, comb_list):
    """

    :param start: int , the ascii value of a single letter between A and Z
    :param end:  int , the ascii value of a single letter between ch1 and Z
    :param num: int, the desired length of string combinations
    :param word: string , a single string combination
    :param comb_list: list , list of string combinations in Alphabetical order
    :return: list , list of string combinations in Alphabetical order from ch1 to ch2 with the length of num
    """
    if len(word) == num:  # the stop condition of the recursion
        comb_list.append(word)
    elif len(word) < num:
        for ASCII_value in range(start, end + 1):  # adds the characters to the word and comb list
            comb_list = char_to_char_words_helper(start, end, num, word + chr(ASCII_value), comb_list)
    return comb_list
    ##############   3  #####################


def solve_maze_monotonic(maze):
    """
    a wrapper function for a recursion function
    :param maze: list , a list of two-dimensional array which represents a maze
    :return: list , the path from the start point to the exit of the maze
    """
    route_lst = []
    if not maze:
        return []
    elif solve_maze_monotonic_helper(maze, 0, 0, route_lst):
        route_lst.insert(0, [0, 0])  # insert the initial point to the route
        return route_lst
    return []


def is_valid(maze, row, col, num):
    """
    a helper function for solve_maze_monotonic_helper which check if it is possible
    to proceed to the next place in the maze
    :param maze: list , a list of two-dimensional array which represents a maze
    :param row: int , the 'row' index of the maze
    :param col: int , the 'column' index of the maze
    :param num: int , the value of the previous cell in the maze
    :return: boolean , true if the cell is valid
    """
    if len(maze) > row >= 0 and len(maze[row]) > col >= 0:
        return maze[row][col] > num
    return False


def solve_maze_monotonic_helper(mat, row_idx, col_idx, route_lst):
    """
    a main recursion which finds and returns a path in the maze by a monotonic path
    :param mat: list , a list of two-dimensional array which represents a maze
    :param row_idx: int , the 'row' index of the maze
    :param col_idx: int , the 'column' index of the maze
    :param route_lst: list , the route from start point to the exit of the maze
    :return: list , the path from the start point to the exit of the maze
    """
    if len(mat) == row_idx + 1 and len(mat[row_idx]) == col_idx + 1:  # the stop condition
        return True
    num = mat[row_idx][col_idx]  # the value of the current place in the maze
    mat[row_idx][col_idx] = mat[-1][-1]  # marking the current position
    if is_valid(mat, row_idx, col_idx + 1, num) and solve_maze_monotonic_helper(mat, row_idx, col_idx + 1, route_lst):
        #  go right in the maze
        route_lst.insert(0, [row_idx, col_idx + 1])
        return True
    if is_valid(mat, row_idx + 1, col_idx, num) and solve_maze_monotonic_helper(mat, row_idx + 1, col_idx, route_lst):
        #  go down in the maze
        route_lst.insert(0, [row_idx + 1, col_idx])
        return True
    if is_valid(mat, row_idx - 1, col_idx, num) and solve_maze_monotonic_helper(mat, row_idx - 1, col_idx, route_lst):
        #  go up in the maze
        route_lst.insert(0, [row_idx - 1, col_idx])
        return True
    if is_valid(mat, row_idx, col_idx - 1, num) and solve_maze_monotonic_helper(mat, row_idx, col_idx - 1, route_lst):
        #  go left in the maze
        route_lst.insert(0, [row_idx, col_idx - 1])
        return True
    return False
