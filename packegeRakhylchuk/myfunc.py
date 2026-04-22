def F4(string):
   
    if not string:
        print("Рядок порожній")
    # max() знаходить елемент з найбільшою кількістю повторів
    # string.count як ключ вказує функції max шукати за кількістю входжень
    most_frequent = max(set(string), key=string.count)
    print(f"Рядок: '{string}'")
    print(f"Символ, який зустрічається найчастіше: '{most_frequent}'")

if __name__== "__main__": 
    test_str = "Рахильчук Михайло"
    F4(test_str)
 

    