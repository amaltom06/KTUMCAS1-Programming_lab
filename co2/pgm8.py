# Accept a list of words and return length of longest word.
n = int(input("Enter the size of the list: "))
a = [input("Enter word: ") for _ in range(n)]
temp = max(a, key=len)
print("Word with max length is", temp, "Its length is", len(temp))