def getSeries():
    newList = []
    n = int(input("Series of how many numbers , you want ? : "))
    for i in range(n):
        print("Enter ", i+1, 'number of the series :  ')
        newList.append(int(input()))
    return newList
	
def NumberAnalysisProgram():
    List1 = getSeries()
    print("Original List : ", List1 )
    sorted_list = sorted(List1)
    print("Sorted List is : ", sorted_list)
    print("Lowest Number in the List is : ", sorted_list[0])
    print("Highest Number in the List is : ", sorted_list[-1])
    Sum = 0
    for i in sorted_list:
        Sum = Sum+i
    print("Total of all the numbers of List is : ", Sum)
    print("Average of list is : ", Sum/len(sorted_list))

def main():
    NumberAnalysisProgram()
	
main()