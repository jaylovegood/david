
def main():
    numbers = list(map(float, input().split()))

    min_n = numbers[0]
    max_n = numbers[0]

    for num in numbers:
        if num < min_n:
            min_n = num
        elif num > max_n:
            max_n = num
    
    print(f"Min: {min_n}, Max: {max_n}")



if __name__=="__main__":
    main()
