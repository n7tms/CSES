# CSES Weird Algorithm
import sys

def main():
    d = int(input())

    ol = [d]
    while d != 1:
        if d % 2:
            d = (d * 3) + 1
        else:
            d = d // 2
        ol.append(d)
    print(' '.join(map(str, ol)))

if __name__ == "__main__":
    main()