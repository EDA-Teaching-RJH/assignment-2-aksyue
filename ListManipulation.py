### Part Three -- your code goes here. 
def main():

    list = [3,1,4,1,5,9,2,6,5,3]

    list.sort()

    x = 0 
    counter = list.count(1)

    while x < counter:
        x = x +1
        list.pop(list.index(int(1))) 
    
    extra = [7,8]

    list.extend(extra)
    print(list)

main()