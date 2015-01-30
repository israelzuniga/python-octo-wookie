"""
Hello world!
Israel.
This code creates a recursive way to
explore and unfold nested lists up on to
1000 nested lists (Python 3 default limit).
Default limit can be changed if you require.
function print_lol(list)
This function takes a list as an argument.
What we do explore each item of the list,
if the item in the list, is a nested list
we call recursively the function to get
deeper in the nested items.
If the item is a string, integer or float
we simply print the item.


Arguments for function print_lol(the_list, indent, level)
1)the_list: The list object to iterate. Required.
2)indent: Printing with tabs ON or OFF. Optional. Off by default.
3)level: Desired level of tabs or indentation. Optional. 0 by default.
"""
def print_lol(the_list, indent=False, level=0):
        for each_item in the_list:
                if isinstance(each_item, list):
                        print_lol(each_item, indent, level+1)
                else:
                        if indent:
                                for tab_level in range(level):
                                        print("\t", end='')
                        print(each_item)

#test list
mylist = ["a", ["b",
                ["c", "d", "e", ["f", "j",
                                 ["k",
                                  ["l", "m", "n", ["o", "p"]]]]]]]
"""
v 1.3.1

RELASE NOTES:
Updates on 1.3.1:
-Added an example list for testing
Updates on 1.3.0:
-Added the "indent" optional argument to select if the programmer
wants or not use indentation or tabs.
Updates on 1.2.1:
Fixed typo.

Updates on 1.2.0:
-API changes on print_lol(). Now, level argument is optional.
"""
