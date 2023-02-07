# 2D list and Nested lists
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][1])

nested_grid = [
    ["khan","shayan"],
    ["faraz","mujeeb"],
    ["ameena"]
]
print(nested_grid[1][1])

#nested for loop printeing all elements in column shape
for row in nested_grid:
    for col in row:
        print(col)

#buld a translator

def translate(phrase):
    translation = ""
    for letter in phrase :
        if letter.lower() in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G "
            else:
                translation = translation +"g"
        else:
            translation = translation + letter
    return  translation

print(translate(input("Enter a phrase")))







