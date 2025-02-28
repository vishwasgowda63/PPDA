import lab1 as np
data1 = [6, 7, 5, 8, 0, 1] 
arr1 = np.array(data1) 
print(arr1) 
print("Type:",type(arr1)) 
print("Shape:", arr1.shape)
print("Size:",arr1.size) 
print("Dimensions:", arr1.ndim) 
print("Data type:", arr1.dtype)
print("Item_Size:",arr1.itemsize) 
print("total_memory: =", arr1.size * arr1.itemsize,"bytes")
