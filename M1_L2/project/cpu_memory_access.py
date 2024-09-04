## Student Name: Jayesh Naidu 
## Student ID: 1233830964 
## Date: 31-08-24


def execute_instruction (action, value): 
    if action == "Add":
        return value + 1
    elif action == "Sub": 
        return value - 1
    else:
        return value
    
# Example of memory access with a list
memory = [0, 1, 2, 3]
print("Initial memory:", memory)
memory[-1] = execute_instruction ("Add", memory [-1]) # Execute ADD instruction
memory[-3] = execute_instruction ("Sub", memory [-3])
print("Memory after execution:", memory)
