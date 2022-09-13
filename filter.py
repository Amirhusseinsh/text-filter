def main():
    file_name = input(" Enter your file name: ")
    file = open(f"{file_name}.txt", "r")
    filter_text = input(" Enter your filter text: ")
    filter(filter_text, file)


def filter(filter_text, file):
    filtered = open(f"{filter_text}.txt", "a")
    for link in file:
        if filter_text in link:
            print(" " + link)
            filtered.writelines(link)


if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            print("Error")
