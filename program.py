#Ссылка на документацию https://docs.google.com/document/d/1lVHqGkCCJLshke8UorBDPSFwRdjJmTN7QpZ0qnbGUjc/edit?usp=sharing


#Расчёт полюса и вычеты передаточной функции.

import control
import scipy.signal

# Определение передаточной функции
numerator = [1, 3]  # числитель
denominator = [1, 2, 3]  # знаменатель

# Создание передаточной функции
tf = control.TransferFunction(numerator, denominator)

# Расчет полюсов и вычетов с использованием функции из SciPy
residues, poles, _ = scipy.signal.residue(numerator, denominator)

# Вывод результатов
print("Полюса функции:", poles)
print("Вычеты функции:", residues)

#Расчёт полюса и вычеты передаточной функции.