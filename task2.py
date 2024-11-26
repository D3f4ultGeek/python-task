dictionary = {}
n = int(input("Number of books: "))
for i in range(n):
    print("Book Title - Days")
    pair = input().split(" - ")
    dictionary[pair[0]] = int(pair[1])
print(" the most borrowed : " , max(dictionary , key= dictionary.get))
print("the least borrowed : " , min(dictionary , key= dictionary.get))
print(f"unique books: {set(dictionary.keys())}")
sortedDic = dict(sorted(dictionary.items() , key= lambda b : b[1] , reverse=True))
average_days = sum(dictionary.values()) / len(dictionary)
print(f"Average days borrowed: {average_days:.2f}")
print(f"sortedbooks {sortedDic}")
