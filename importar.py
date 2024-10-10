import numpy as np

my_array = np.array([1, 2, 3, 4, 5])

print("Array original:")
print(my_array)

squared_array = my_array ** 2 # Elevando ao quadrado
sum_of_elements = np.sum(my_array)

print("Array ao quadrado:")
print(squared_array)
print("Soma dos elementos:")
print(sum_of_elements)

element_at_index_2 = my_array[2] # Acessa o índice 2
print("Elemento no índice 2:", element_at_index_2)