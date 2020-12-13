#Have to find all the different types of sorting
#Gonna take in a list of numbers
#Start simple and then move my way up

def selection_sort(list):
    for i in range(len(list)):
        min_ind = i
        for j in range(i + 1, len(list)):
            if(list[j] < list[min_ind]):
                min_ind = j
        list[min_ind], list[i] = list[i], list[min_ind]

def mergeSort(list):
    if(len(list) > 1):
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while(i < len(L) and j < len(R)):
            if(L[i] < R[j]):
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1

        while(i < len(L)):
            list[k] = L[i]
            i += 1
            k += 1
        while(j < len(R)):
            list[k] = R[j]
            j += 1
            k += 1

def main():
    list = [2,5,87,5,3,543,23,54,5,1,0]
    selection_sort(list)
    print(list)
if __name__  == '__main__':
    main()
