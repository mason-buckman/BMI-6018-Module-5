#!/usr/bin/env python
# coding: utf-8

# In[9]:


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

def get_inner_lists(input):
    '''
    This is a helper function that returns the contents of the "inner lists" found inside an input list
    EX: input = [[1,2],[1,[1,2]]], output = [1,2,1,[1,2]]
    '''
    inner_lists = []
    for i in input:
        if isinstance(i, list):
            for k in i:
                inner_lists.append(k)
    return inner_lists

def recursive_inner_plus(input_list):
    '''
    This function returns the innermost list given an input list and adds 1 to each value of the innermost list.
    '''
    if contains_list(input_list) == False:
        return generate_output(input_list)
    else:
        input = get_inner_lists(input_list)
        return recursive_inner_plus(input)

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            # Parse the list from command-line string safely
            input_list = ast.literal_eval(sys.argv[1])
            output = recursive_inner_plus(input_list)
            print("Innermost list after +1:", output)
        except Exception as e:
            print("Error parsing input:", e)
    else:
        print("No command-line arguments provided.")


# In[ ]:




