def main():
    A, B = map(int, input().split())
    if A > 9 or B > 9:
        print(-1)
        exit(0)
    else:
        print(A * B)


if __name__ == "__main__":
    main()
