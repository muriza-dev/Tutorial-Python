'''
    Sebelumnya kita sudah mengenal apa itu tipe ada, Tentunya kali ini kita akan mengenal lebih banyak apa itu tipe data didalam python dan bagaimana cara menggunakannya.
'''
# Tipe data: Angka satuan bulat, yang tidak menggunakan Koma
data_interger = 3 
print(type(data_interger))
print('Data : ', data_interger, '\n- Bertipe : ', type(data_interger), '\n')

# Tipe data: Float, yang memiliki koma dibelakang nya
data_float = 5.3 
print(type(data_float))
print('Data : ', data_float, '\n- Bertipe : ', type(data_float), '\n')

# Tipe data: String, yang mengumpulkan kumpulan data huruf
data_string = 'Muhammad Rizal'
print(type(data_string))
print('Data : ', data_string, '\n- Bertipe : ', type(data_string), '\n')

# Tipe data: biner true/false
data_true = True
print(type(data_true))
print('Data : ', data_true, '\n- Bertipe : ', type(data_true), '\n')

# Tipe data: kompleks, yang dikhusus kan untuk matematik
data_complex = complex(5.6)
print(type(data_complex))
print('Data : ', data_complex, '\n- Bertipe : ', type(data_complex), '\n')

# Tipe data: menggunakan tipe data dari bahasa C, karna keterbatasan tipe data di bahasa python, akan tetapi kita harus melakukan impor modulnya terlebih dahulu.

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print(type(data_c_double))
print('Data : ', data_c_double, '\n- Bertipe : ', type(data_c_double), '\n')

data_c_char = c_char(200)
print(type(data_c_char))
print('Data : ', data_c_char, '\n- Bertipe : ', type(data_c_char), '\n')