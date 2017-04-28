if __name__ == "__main__":
    nums = []
    with open("nums.txt", "r") as f:
        nums = [int(l.strip()) for l in f.readlines()]

    total = sum(nums)
    str_total = str(total)

    print(str_total[:10])
    print(str_total[-10:])
