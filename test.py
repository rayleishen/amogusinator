# Example RGB color lists
left_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow
right_colors = [(0, 255, 0), (255, 255, 0), (255, 0, 0), (0, 0, 255)]  # Green, Yellow, Red, Blue

# Find matching pairs
matching_pairs = []

for left_index, left_color in enumerate(left_colors):
    for right_index, right_color in enumerate(right_colors):
        if left_color == right_color:
            matching_pairs.append((left_index, right_index))

# Output the matching pairs
for left_index, right_index in matching_pairs:
    print(f"Left {left_index + 1} matches with Right {right_index + 1}")