def PrintName(i, n):
    # Base case: stop recursion when i exceeds n
    if i > n:
        return
    print("Nischal")
    # Recursive call with incremented i
    PrintName(i + 1, n)

# Example usage
PrintName(1, 5)
