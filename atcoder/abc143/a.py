def main():
    A, B = map(int, input().split())
    if A < B * 2:
        print(0)
        exit(0)
    else:
        print(A - B * 2)


if __name__ == "__main__":
    main()
