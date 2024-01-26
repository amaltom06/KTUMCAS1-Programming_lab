# Generate all factors of a number.
def facts(x):
 return [i for i in range(1, x + 1) if x % i == 0]
n = int(input("Enter a number: "))
factors = facts(n)
print(f"Factors of {n} are: {factors}")