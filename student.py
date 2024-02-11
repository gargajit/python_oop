def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house          # this is not returning 2 values rather it is returning one value in form of tuple


if __name__ == "__main__":
    main()
