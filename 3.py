def binarySearch (arr, l, r, x): 
  
    
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
         
        if arr[mid] == x: 
            return mid 
          
        
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
         
        return -1
  
arr=[]
n=int(input("Enter size of the array:\n"))
print("Enter numbers for the array one after the other\n")
for i in range(0,n):
    a=int(input("Enter number for the array:\n"))
    arr.append(a)

                
x =int(input("Enter the number to be searched: "))
  
#Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print("\nElement is present at index",result) 
else: 
    print("\nElement is not present in array")
