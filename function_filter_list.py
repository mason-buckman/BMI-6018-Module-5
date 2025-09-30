#!/usr/bin/env python
# coding: utf-8

# In[8]:


# input1 = [1,2,3,4,5,6,7,8,9]
# input2 = [0,1,6,8,4,12,36,9,50,22,13,7]
# input3 = [42,15,18,20,29,21,34,40,31,9]
# threshold = 17

import ast

def function_filter_list(input_list, threshold):
    '''
    Given an input list (list of integers) and a threshold value (integer), this function outputs a list of values that are at or below
    the specified threshold.
    EX: input = [1,3,5,7,9,11], threshold = 8, output = [1,3,5,7]
    '''

    filtered_list = []
    for i in input_list:
        if i <= threshold:
            filtered_list.append(i)
    return filtered_list

if __name__ == "__main__":
    input_str = input("Please enter a list of integers (i.e. [1,2,3]): ")
    threshold_str = input("Enter an integer threshold (i.e. 8): ")

    try:
        input_list = ast.literal_eval(input_str)
        threshold = int(threshold_str)
    except Exception as e:
        print("Invalid input:", e)
        exit(1)

    output = function_filter_list(input_list, threshold)
    print("Filtered list:", output)


# In[ ]:




