from pympler import asizeof

word = input("Type the word for serching: ")
print(word)

def find_in_file(file_name: str, pattern: str):
    with open(file_name, "r", encoding="utf-8") as file:
        with open("./lesson3/results.txt", "w", encoding="utf-8") as output:    
            while True:
                line = file.readline().replace("\n", "")
                if not line:
                    break
                if pattern in line:
                    output.write(line+"\n")
                    yield line
        with open("./lesson3/results.txt", "r", encoding="utf-8") as fp:
            lines = len(fp.readlines())
            print('Total number of lines:', lines)


print(asizeof.asized(list(find_in_file(
    file_name="./lesson3/rockyou.txt",
    pattern=word
)), detail=1).format())

