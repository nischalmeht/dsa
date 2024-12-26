def print_h_pattern(height):
    width = height // 2  # Width of the two vertical lines of H
    for i in range(height):
        if i == height // 2:  # Middle horizontal line
            print('*' * height)
        else:  # Vertical lines
            print('*' + ' ' * (height - 2) + '*')

# Example usage
print_h_pattern(7)
