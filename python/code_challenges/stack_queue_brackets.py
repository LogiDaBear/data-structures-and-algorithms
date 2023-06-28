from data_structures.stack import Stack

def multi_bracket_validation(str):
    stack = []
    opening_brackets = ['(','[','{']
    closing_brackets = [')',']','}']
    
    
    for char in str:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            
           
            top = stack.pop()
            opening_index = opening_brackets.index(top)
            closing_index = closing_brackets.index(char)
            if opening_index != closing_index:

                return False

    return len(stack) == 0