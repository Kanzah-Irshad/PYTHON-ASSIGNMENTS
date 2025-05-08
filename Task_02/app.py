# --------------------------- A RIGHT HAND HALR PYRAMID, BOTH STRAIGHT AND REVERSED FORM ----------------------
#----------------------------------------------TASK 2----------------------------------------------------------
# CREATE A RIGHT HAND HALR PYRAMID, BOTH STRAIGHT AND REVERSED FORM

rows = int(input("ENTER THE NUMBER OF ROWS:"))

print("Straight Form:")
# CONDITION : The loop runs from 1 to rows (inclusive)
for i in range(1, rows + 1):
    print(" " * (rows - i) + "#" * i)
# " " * (rows - i): prints the spaces to shift the # to the right
# "#" * i: prints the hash symbols. The number of hashes equals the row number.

print("\nReverse Form:")
# CONDITION : This loop counts down from rows to 1.
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "#" * i)
