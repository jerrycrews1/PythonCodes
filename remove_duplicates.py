def remove_duplicates(list1):
    """
    receives a list of items and returns a  new list containing only the unique items.
    """
    new_list = []
    if list1:  # checks that a list is provided
        for item in list1:  # for each item in the list
            if item not in new_list:  # check that the item is not in the new list
                new_list.append(item)  # if it isn't in the  new list, add it
    else:
        return list1
    return new_list


# test
print(remove_duplicates([1, 2, 3, 3, 4]))
