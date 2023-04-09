def function():
    print("--------------------------------------------------")
    print("| x | y | not (x and y) | z | not (x and y) or z |")
    print("--------------------------------------------------")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"| {x} | {y} |      {int(not (x and y))}        | {z} |          {int((not x and y) or z)}         |")
    print("--------------------------------------------------")
function()