import fileinput

numbers_string = list(fileinput.input())[0]
numbers = list(map(lambda n : int(n), list(numbers_string)))

result = sum([numbers[i] for i in range(len(numbers)) if numbers[i] == numbers[(i+1)%len(numbers)]])

print(result)
