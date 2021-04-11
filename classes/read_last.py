def main() :
    with open("configs/last/last.txt", "r") as f :
        for line in f :
            last = line

    return last

if __name__ == "__main__" :
    main()