# Accept a file name from user and print extension of that. 
fname=input("Enter a file name:")
extension=fname.split('.')
print("Extension=",extension[-1])