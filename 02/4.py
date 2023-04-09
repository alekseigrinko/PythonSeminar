def moveRight(numbers, step:int):
    result = list()
    for n in range(step, 0, -1):
        result.append(numbers[len(numbers)-n])
    for i in range(len(numbers)-step):
        result.append(numbers[i])    
    return result

def function():
    number = int(input("Введите число N для определения промежутка [-N, N]: "))
    numbers = list()
    for i in range (-number, number+1):
        numbers.append(str(i))
    print("Результат смещения всех элементов списка на 2 позиции направо: ")
    print(f"{number} -> [" + ", ".join(moveRight(numbers, 2)) + "]")
function()