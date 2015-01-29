
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
we simply print the item
"""
def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)
