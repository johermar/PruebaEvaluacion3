def move_stone(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 stones from source to auxiliary tower
        move_stone(n-1, source, auxiliary, target)
        
        # Move the nth stone from source to target tower
        print(f"Move stone {n} from {source} to {target}")
        
        # Move the n-1 stones from auxiliary to target tower
        move_stone(n-1, auxiliary, target, source)

# Number of stones in the pyramid
num_stones = 3

# Towers
source_tower = "A"
target_tower = "B"
auxiliary_tower = "C"

# Call the function to solve the puzzle
move_stone(num_stones, source_tower, target_tower, auxiliary_tower)