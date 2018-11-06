# Made by artor1as
"""
    Input: list with different int numbers (negative, zero, positive)
    Output: list with replaced number
    (left: negative numbers, middle: zero numbers, right: positive)
    Extra condition: use only one cycle to replace numbers
"""


def list_replace(lst=None):
    if lst is None:
        lst = []
    neg_lst = []
    pos_lst = []
    zero_lst = []
    for i in lst:
        if i < 0:
            neg_lst.append(i)
        elif i == 0:
            zero_lst.append(i)
        else:
            pos_lst.append(i)
    return neg_lst+zero_lst+pos_lst


if __name__ == '__main__':
    data_lst = []
    while True:
        num = input("Enter number (type \'exit\' to exit cycle): ")
        if num == "exit":
            break
        try:
            data_lst.append(int(num))
        except ValueError:
            print("Enter valid number")
            continue
    print(list_replace(data_lst))
