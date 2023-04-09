def function():
    line1 = "one"
    line2 = "onetwonine"
    result = list()
    for i in line1:
        count = 0
        for y in line2:
            if i == y:
                count +=1
        result.append(str(f"{i} - {count}"))
    print(", ".join(result))
function()