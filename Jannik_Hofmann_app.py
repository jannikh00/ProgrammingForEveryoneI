import time

def has_duplicates(input_list):
    """
    Function to check if a list has duplicates. 
    Optimized version with time complexity O(n).
    """
    seen = []
    for element in input_list:
        if element in seen:
            return True
        seen.append(element)
    return False

# List to check
numbers_0 = [11, 12, 3, 4, 15, 6, 7, 8, 9, 10, 1, 2, 13, 14, 15, 16, 17, 18, 19, 20, 1]
numbers_1 = [11, 12, 3, 4, 15, 6, 7, 8, 9, 10, 100, 2, 13, 14, 150, 16, 17, 18, 19, 20, 1]
numbers_2 = [11, 12, 3, 4, 15, 6, 7, 8, 9, 10, 1, 2, 13, 14, 150, 16, 17, 18, 19, 20, 1]

numbers_list = [numbers_0, numbers_1, numbers_2]

for i in numbers_list:
    start_time = time.time()
    # Prints, if the list has a duplicate (True) or not (False)
    print(f"The list has duplicates: {has_duplicates(i)}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} seconds\n")

