
def areRotations(s1, s2):
    s1 = s1 + s1
    rotation_index=s1.index(s2)
    rotation=s1[rotation_index:] + s1[:rotation_index]
    print(rotation,rotation_index)
    # find s2 in concatenated string
    return s2 in s1

if __name__ == "__main__":
    s1 = "ABCD"
    s2 = "CDAB"

    print("true" if areRotations(s1, s2) else "false")