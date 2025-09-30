#!/usr/bin/env python
# coding: utf-8

# In[5]:


# input_list1 = [1,2,3,4,[5,6,7,[8,9]]]                # Expected output [9, 10]
# input_list2 = [1,2,[3,4,[7,[5,5]]],4,[8,7],9]        # Expected output [6, 6]
# input_list3 = [2,2,[1,2,3],5,[9,8,[7,4],6],1,1]      # Expected output [8, 5]
# input_list4 = [1,2,3]                                # Expected output [2, 3, 4]
# input_list5 = [8,[2,2,[1,4],7],0,9,[0,[1,[4,[5]]]]]  # Expected output [6]
# input_list6 = [1,[4,[7]],3,[3,4,5]]                  # Expected output [8]
# input_list7 = [3,2,[1,5],7,7]                        # Expected output [2, 6]
# input_list8 = [[1,2],[3,4]]                          # Expected output [2, 3]

import sys
import ast

def contains_list(input_list):
    '''
    This is a helper function that returns True if a given list contains another list.
    EX: 
        input1 = [1,2,3], output1 = False
        input2 = [1,[2,2]], output2 = True
    '''

    for entry in input_list:
        if isinstance(entry, int):
            continue
        else:
            return True
    return False

def generate_output(input_list):
    '''
    This is a helper function that adds 1 to each value of a given list.
    EX: input = [0,1,2], output = [1,2,3]
    '''

    new_list = []
    for i in input_list:
        new_list.append(i + 1)
    return new_list


def while_inner_plus(input):
    '''
    This function takes in a list of any complexity or nestedness, finds finds the innermost (most nested) list within the input list 
    and adds 1 to each value. Finally, the function outputs the updated innermost list. The input list must only contain integers or
    lists of integers.

    EX: input = [1,2[3,4],5], output = [4,5]

    Note: If more than one list is present at the same innermost "level", then the first list is used in the calculation.

    EX: input = [1,[2,3],4,[5,6],7], output = [3,4]
    '''

    if contains_list(input) == False:
        return generate_output(input)
    max_depth = local_depth = 0
    lowest_list = []
    for item in input:
        if isinstance(item, int):
            continue
        if lowest_list == []:
            lowest_list = item
        max_index = len(item)
        index = 0
        scope = item
        while index < max_index:
            if isinstance(scope[index], list):
                local_depth += 1
                scope = scope[index]
                index = 0
                max_index = len(scope)

                if local_depth > max_depth:
                    max_depth = local_depth
                    lowest_list = scope
            else:
                index += 1
    return generate_output(lowest_list)

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            # Parse the list from command-line string safely
            input_list = ast.literal_eval(sys.argv[1])
            output = while_inner_plus(input_list)
            print("Innermost list after +1:", output)
        except Exception as e:
            print("Error parsing input:", e)
    else:
        print("No command-line arguments provided.")

# output = while_inner_plus(input_list1)
# print(output)


# In[ ]:




