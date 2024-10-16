import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Salaries.csv')

df = df.drop(['Id', 'Notes', 'Agency', 'Status'], axis=1, errors='ignore')
df['BasePay'] = pd.to_numeric(df['BasePay'], errors='coerce')
df['EmployeeName'] = df['EmployeeName'].replace('Not provided', np.nan)

print("Descripción estadística de los datos:")
print(df.describe())

print(f"Número total de empleados: {len(df)}")
print(f"Número de títulos de trabajo únicos: {df['JobTitle'].nunique()}")

# Los 10 títulos de trabajo más comunes
top_titles = df['JobTitle'].value_counts().head(10)
print("\nLos 10 títulos de trabajo más comunes y su cantidad:")
for title, count in top_titles.items():
    print(f"{title}: {count}")

captains = df[df['JobTitle'].str.contains('CAPTAIN', case=False)]
print(f"Total de CAPTAIN: {len(captains)}")

fire_employees_count = df[df['JobTitle'].str.contains('fire', case=False)].shape[0]
print(f"Empleados con 'fire' en el título: {fire_employees_count}")

base_pay_min = df['BasePay'].min()
base_pay_max = df['BasePay'].max()
base_pay_mean = df['BasePay'].mean()
print(f"BasePay - Mínimo: {base_pay_min}, Máximo: {base_pay_max}, Promedio: {base_pay_mean:.2f}")

max_base_pay_row = df[df['BasePay'] == df['BasePay'].max()]
if not max_base_pay_row.empty:
    max_base_pay_employee = max_base_pay_row['EmployeeName'].values[0]
    print(f"Empleado con mayor BasePay: {max_base_pay_employee}")
else:
    print("No se encontró información del empleado con mayor BasePay.")

# Gráficos
try:
    df.groupby('Year').mean()['BasePay'].plot(kind='bar', title='Salario promedio por año')
    plt.xlabel('Año')
    plt.ylabel('Salario promedio')
    plt.show()
except Exception as e:
    print(f"Error al graficar el salario promedio por año: {e}")

try:
    plt.scatter(df['BasePay'], df['TotalPay'], alpha=0.5)
    plt.title('Relación entre BasePay y TotalPay')
    plt.xlabel('BasePay')
    plt.ylabel('TotalPay')
    plt.show()
except Exception as e:
    print(f"Error al graficar la relación entre BasePay y TotalPay: {e}")
