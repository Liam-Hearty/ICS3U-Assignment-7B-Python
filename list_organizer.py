#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Dec 2019
# This program organizes your lists.


def list_organizer(list1_num, list2_num, list1, list2):

    counter = 0
    final_list_num = list1_num + list2_num
    final_list = []

    for counter in range(0, final_list_num):
        if counter < list1_num:
            final_list.append(list1[counter])
        if counter < list2_num:
            final_list.append(list2[counter])
        counter += 1

    return final_list


def main():
    list1 = []
    list2 = []
    final_list = []

    try:
        list1_num = int(input("How many items to add to your 1st list: "))
        list2_num = int(input("How many items to add to your 2nd list: "))

    except ValueError:
        print("Please enter a valid response.")

    final_list_num = list1_num + list2_num

    counter = 0
    for counter in range(0, list1_num):
        item = str(input("Enter an item to add to your 1st list: "))
        list1.append(item)
        counter += 1

    counter = 0
    for counter in range(0, list2_num):
        item = str(input("Enter an item to add to your 2nd list: "))
        list2.append(item)
        counter += 1

    final_list = list_organizer(list1_num, list2_num, list1, list2)

    counter = 0
    for counter in range(0, final_list_num):
        print(final_list[counter])
        counter += 1


if __name__ == "__main__":
    main()
