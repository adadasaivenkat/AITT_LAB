import numpy as np
a=np.array([1,2,3,4,5,6])
a1=np.array([[1,2,3],[4,5,6]])
print(f"Array : {a} and {a1}")
print(f"Type of the array : {type(a)} and {type(a1)}")
print(f"Length of the array : {len(a)} and {len(a1)}")
print(f"Total elements in the array : {a.size} and {a1.size}")
print(f"Number of dimensions : {a.ndim} and {a1.ndim}")
print(f"Shape of the array : {a.shape} and {a1.shape}")
new=np.arange(6).reshape(2,3)
print(f"New array : {new}")
print(f"Reshaped array : {new.reshape(3,2)}")
print(f"Item size (Bytes): {new.itemsize}")
print(f"Data type of the array : {new.dtype}")