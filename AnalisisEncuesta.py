#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from textwrap import wrap

fontsize1 = 16
fontsize2 = 16

# Read the excel file as a dataframe
df = pd.read_excel('Encuesta.xlsx')

# Get information about the dataframe
# Tipo de contrato. Column 1
print('\n\n')
print('#### CONTRATO ####')
# Get the column
column = df.iloc[:, 1]
# Check if the column contains the strings
# Junta, cargo a proyecto, UGR, FPI, FPU
# Create a dictionary to store the counts
contratos = {
    'Junta': 0,
    'Cargo a proyecto': 0,
    'UGR': 0,
    'FPI': 0,
    'FPU': 0,
    'Otro': 0
}
# Iterate over the column
for value in column: # en minúsculas todo
    try:
        value = value.lower()
        if 'junta' in value: 
            contratos['Junta'] += 1
        elif 'cargo a proyecto' in value:
            contratos['Cargo a proyecto'] += 1
        elif 'ugr' in value:
            contratos['UGR'] += 1
        elif 'fpi' in value:
            contratos['FPI'] += 1
        elif 'fpu' in value:
            contratos['FPU'] += 1
        else:
            contratos['Otro'] += 1
    except:
        print('contrato no válido:', value)

# Sum all the values and compare to the number of rows
total = sum(contratos.values())
print('Respuestas consideradas:', total, 'de', len(column))

# Associate colors to each type of contract
colors = {
    'Junta': 'green',
    'Cargo a proyecto': 'blue',
    'UGR': 'red',
    'FPI': 'orange',
    'FPU': 'purple',
    'Otro': 'gray'
}

# Create a bar plot
fig, ax = plt.subplots(figsize=(14, 5))
#ax.bar(contratos.keys(), contratos.values())
for i, (key, value) in enumerate(contratos.items()):
    ax.bar(key, value, color=colors[key])
ax.set_xlabel('Tipo de contrato', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Número de personas por tipo de contrato', fontsize=fontsize2)
# Escribir sobre cada columna el porcentaje
for i, value in enumerate(contratos.values()):
    ax.text(i, value, f'{value/total*100:.2f}%', ha='center', va='bottom')
# Increase font size
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.tight_layout()
plt.savefig('1-contratos.png')



# Facultad. Column 2
print('\n\n')
print('#### FACULTAD ####')
# Get the column
column = df.iloc[:, 2]
# Create a dictionary to store the counts
facultades = {
    'Psicología': 0,
    'Económicas y Empresariales': 0,
    'Filosofía y Letras': 0,
    'ETSIIT y CITIC': 0, # decsai = computacion = telecomunicación
    'Comunicación y Documentación': 0,
    'Ciencias de la Educación': 0,
    'Traducción e Interpretación': 0,
    'Medicina': 0,
    'Trabajo Social': 0,
    'Bellas Artes': 0,
    'Ciencias del Deporte': 0,
    'CEAMA': 0,
    'Caminos y Puentes': 0, # Estructuras,
    'Genyo y CIBM': 0,
    'Farmacia': 0,
    'Derecho': 0,
    'Ciencias': 0
}

# Iterate over the column
for value in column:
    try:
        value = value.lower()
        if 'psicología' in value or 'psicologia' in value:
            facultades['Psicología'] += 1
        elif 'empresariales' in value:
            facultades['Económicas y Empresariales'] += 1
        elif 'filosofía' in value or 'filosofia' in value:
            facultades['Filosofía y Letras'] += 1
        elif 'ettsiit' in value or 'citic' in value or 'computación' in value or 'telecomunicación' in value or 'telecomunicacion' in value:
            facultades['ETSIIT y CITIC'] += 1
        elif 'comunicación' in value or 'documentación' in value or 'documentacion' in value:
            facultades['Comunicación y Documentación'] += 1
        elif 'educación' in value or 'educacion' in value:
            facultades['Ciencias de la Educación'] += 1
        elif 'traducción' in value or 'traduccion' in value or 'interpretación' in value:
            facultades['Traducción e Interpretación'] += 1
        elif 'medicina' in value:
            facultades['Medicina'] += 1
        elif 'trabajo social' in value:
            facultades['Trabajo Social'] += 1
        elif 'bellas artes' in value:
            facultades['Bellas Artes'] += 1
        elif 'deporte' in value:
            facultades['Ciencias del Deporte'] += 1
        elif 'caminos' in value or 'puentes' in value or 'estructuras' in value:
            facultades['Caminos y Puentes'] += 1
        elif 'farmacia' in value:
            facultades['Farmacia'] += 1
        elif 'derecho' in value:
            facultades['Derecho'] += 1
        elif 'ceama' in value:
            facultades['CEAMA'] += 1
        elif 'genyo' in value or 'cibm' in value:
            facultades['Genyo y CIBM'] += 1
        elif 'ciencias' in value:
            facultades['Ciencias'] += 1
        else:
            print('Facultad no reconocida:', value)
    except:
        print('Facultad no válida:', value)

# Sum all the values and compare to the number of rows
total = sum(facultades.values())
print('Respuestas consideradas:', total, 'de', len(column))

# Create a bar plot
fig, ax = plt.subplots(figsize=(20, 5))
labels = ['\n'.join(wrap(label, 10)) for label in facultades.keys()]
ax.bar(labels, facultades.values())
ax.set_xlabel('Facultad', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Número de personas por facultad', fontsize=fontsize2)
# Fontsize
plt.xticks(fontsize=fontsize1-3)
plt.yticks(fontsize=fontsize1-3)
plt.tight_layout()
plt.savefig('2-facultades.png')





print('\n\n')
print('#### TIEMPO DE CONTRATO ####')
# Get the column
column = df.iloc[:, 3]

# Create a dictionary to store the counts
tiempos = {
    'más de 1 año': 0,
    'menos de 1 año': 0,
}

# Iterate over the column
for value in column:
    try:
        value = value.lower()
        if 'más ' in value or 'mas' in value:
            tiempos['más de 1 año'] += 1
        elif 'menos' in value:
            tiempos['menos de 1 año'] += 1
        else:
            print('Tiempo de contrato no reconocido:', value)
    except:
        print('Tiempo de contrato no válido:', value)

# Sum all the values and compare to the number of rows
total = sum(tiempos.values())
print('Respuestas consideradas:', total, 'de', len(column))

# Associate colors to each answer
colors = {
    'más de 1 año': 'purple',
    'menos de 1 año': 'green',
}

# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))
#ax.bar(tiempos.keys(), tiempos.values())
for i, (key, value) in enumerate(tiempos.items()):
    ax.bar(key, value, color=colors[key])
ax.set_xlabel('Tiempo de contrato', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Tiempo de contrato', fontsize=fontsize2)
# Escribir sobre cada columna el porcentaje
for i, value in enumerate(tiempos.values()):
    ax.text(i, value, f'{value/total*100:.2f}%', ha='center', va='bottom')
# Fontsize
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.tight_layout()
plt.savefig('3-TiempoContrato.png')



print('\n\n')
print('#### ESPACIO PROPIO ####')
# Get the column
column = df.iloc[:, 4]

# Create a dictionary to store the counts
espacios = {
    'Sí': 0,
    'No': 0,
}

# Iterate over the column
for value in column:
    try:
        value = value.lower()
        if 'no' in value:
            espacios['No'] += 1
        elif 'sí' in value or 'si' in value:
            espacios['Sí'] += 1
        else:
            print('Espacio propio no reconocido:', value)
    except:
        print('Espacio propio no válido:', value)

# Sum all the values and compare to the number of rows
total = sum(espacios.values())
print('Respuestas consideradas:', total, 'de', len(column))

colors = {
    'Sí': 'green',
    'No': 'red',
}
# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))
#ax.bar(espacios.keys(), espacios.values())
for i, (key, value) in enumerate(espacios.items()):
    ax.bar(key, value, color=colors[key])
ax.set_xlabel('Espacio propio', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Número de personas con espacio propio', fontsize=fontsize2)
# Escribir sobre cada columna el porcentaje
for i, value in enumerate(espacios.values()):
    ax.text(i, value, f'{value/total*100:.2f}%', ha='center', va='bottom')
# Fontsize
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.tight_layout()
plt.savefig('4-EspacioPropio.png')




print('\n\n')
print('#### TIPO DE DESPACHO ####')

# Get the column
column_prev = df.iloc[:, 4]
column = df.iloc[:, 5]

# Create a dictionary to store the counts
despachos = {
    'Individual': 0,
    'Compartido o Comunitario': 0,
    'Laboratorio': 0,
    'Otro': 0,
    'No tengo despacho': 0
}

# Iterate over the column
for value, value_prev in zip(column, column_prev):
    try:
        value_prev = value_prev.lower()
        if 'no' in value_prev:
            despachos['No tengo despacho'] += 1
        else:
            value = value.lower()

            if 'laboratorio' in value:
                despachos['Laboratorio'] += 1
            elif 'individual' in value:
                despachos['Individual'] += 1
            elif 'compartido' in value or 'comunitario' in value:
                despachos['Compartido o Comunitario'] += 1
            else:
                despachos['Otro'] += 1
    except:
        print('Tipo de despacho no válido:', value)

# Sum all the values and compare to the number of rows
total = sum(despachos.values())
print('Respuestas consideradas:', total, 'de', len(column))

colors = {
    'Individual': 'green',
    'Compartido o Comunitario': 'orange',
    'Laboratorio': 'red',
    'Otro': 'gray',
    'No tengo despacho': 'black'
}
# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))
labels = ['\n'.join(wrap(label, 15)) for label in despachos.keys()]
#ax.bar(labels, despachos.values())
for i, (key, value) in enumerate(despachos.items()):
    ax.bar(labels[i], value, color=colors[key])
ax.set_xlabel('Tipo de despacho', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Número de personas por tipo de despacho', fontsize=fontsize2)
# Escribir sobre cada columna el porcentaje
for i, value in enumerate(despachos.values()):
    ax.text(i, value, f'{value/total*100:.2f}%', ha='center', va='bottom')
# Fontsize
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.tight_layout()
plt.savefig('5-TipoDespacho.png')




print('\n\n')
print('#### PERSONAS COMPARTIENDO DESPACHO ####')
# Get the column
column = df.iloc[:, 6]

# Create a dictionary to store the counts
personas = {
    '2 a 5': 0,
    '5 a 10': 0,
    'Más de 10': 0
}

# As a curiosity, keep the maximum number of people in the column
max_people = 0

# Iterate over the column
for value in column:
    try:
        # Check if the value is a string or a number
        if isinstance(value, (int, float)):
            number = int(value) + 1
        else:
            value = value.lower()
            # Look for numbers in the string
            separators = ['-', '/', '+', '.']

            # Split the string by the separators and spaces
            for separator in separators:
                value = value.replace(separator, ' ')
            
            # Split the string by spaces
            numbers = [int(s) for s in value.split() if s.isdigit()]

            # Get the highest number in the list, and add 1 because the range is inclusive
            number = max(numbers) + 1
        
        # Add the number to the corresponding range
        if number <= 5:
            personas['2 a 5'] += 1
        elif number <= 10:
            personas['5 a 10'] += 1
        else:
            personas['Más de 10'] += 1

        # Keep the maximum number of people
        if number > max_people:
            max_people = number
            print('Nuevo máximo:', max_people, 'en', value)
        #max_people = max(max_people, number)
    except:
        print('Número de personas no válido:', value)

print('## Máximo número de personas compartiendo despacho:', max_people)

# Sum all the values and compare to the number of rows
total = sum(personas.values())
print('Respuestas consideradas:', total, 'de', len(column))

colors = {
    '2 a 5': 'green',
    '5 a 10': 'orange',
    'Más de 10': 'red'
}
# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))
#ax.bar(personas.keys(), personas.values())
for i, (key, value) in enumerate(personas.items()):
    ax.bar(key, value, color=colors[key])
ax.set_xlabel('Número de personas compartiendo despacho', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Número de personas compartiendo despacho', fontsize=fontsize2)
# Escribir sobre cada columna el porcentaje
for i, value in enumerate(personas.values()):
    ax.text(i, value, f'{value/total*100:.2f}%', ha='center', va='bottom')
# Fontsize
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.tight_layout()
plt.savefig('6-PersonasCompartiendo.png')





print('\n\n')
print('#### EQUIPAMIENTO DE TRABAJO ####')
# Get the column
column = df.iloc[:, 7]

# Create a dictionary to store the counts
equipamiento = {
    'Ordenador UGR': 0,
    'Pantalla auxiliar': 0,
    'Escritorio propio': 0,
    'Espacio siempre disponible': 0,
    'Otro': 0
}

total = 0
# Iterate over the column
for value in column:
    try:
        value = value.lower()
        if 'ordenador' in value or 'ugr' in value:
            equipamiento['Ordenador UGR'] += 1
        if 'pantalla' in value:
            equipamiento['Pantalla auxiliar'] += 1
        if 'escritorio' in value:
            equipamiento['Escritorio propio'] += 1
        if 'siempre' in value or 'disponible' in value:
            equipamiento['Espacio siempre disponible'] += 1
        else:
            equipamiento['Otro'] += 1
        total += 1
    except:
        print('Equipamiento no válido:', value)

# Sum all the values and compare to the number of rows
total = len(column)
print('Respuestas consideradas:', total, 'de', len(column))

colors = {
    'Ordenador UGR': 'green',
    'Pantalla auxiliar': 'blue',
    'Escritorio propio': 'red',
    'Espacio siempre disponible': 'orange',
    'Otro': 'gray'
}
# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))
labels = ['\n'.join(wrap(label, 10)) for label in equipamiento.keys()]
#ax.bar(labels, equipamiento.values())
for i, (key, value) in enumerate(equipamiento.items()):
    ax.bar(labels[i], value, color=colors[key])
ax.set_xlabel('Equipamiento de trabajo', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Equipamiento de trabajo disponible', fontsize=fontsize2)
# Escribir sobre cada columna el porcentaje
for i, value in enumerate(equipamiento.values()):
    ax.text(i, value, f'{value/total*100:.2f}%', ha='center', va='bottom')
# Fontsize
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.tight_layout()
plt.savefig('7-Equipamiento.png')





print('\n\n')
print('#### COMPARACIÓN ####')
# Get the column
column = df.iloc[:, 11]

# Create a dictionary to store the counts
comparacion = {
    'Mejor': 0,
    'Igual': 0,
    'Peor': 0,
}

# Iterate over the column
for value in column:
    try:
        value = value.lower()
        if 'mejor' in value:
            comparacion['Mejor'] += 1
        elif 'igual' in value:
            comparacion['Igual'] += 1
        elif 'peor' in value:
            comparacion['Peor'] += 1
        else:
            print('Comparación no reconocida:', value)
    except:
        print('Comparación no válida:', value)

# Sum all the values and compare to the number of rows
total = sum(comparacion.values())
print('Respuestas consideradas:', total, 'de', len(column))

colors = {
    'Mejor': 'green',
    'Igual': 'blue',
    'Peor': 'red',
}
# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))
#ax.bar(comparacion.keys(), comparacion.values())
for i, (key, value) in enumerate(comparacion.items()):
    ax.bar(key, value, color=colors[key])
ax.set_xlabel('Percepción de la situación', fontsize=fontsize2)
ax.set_ylabel('Número de personas', fontsize=fontsize2)
ax.set_title('Percepción de tu situación frente a los compañeros', fontsize=fontsize2)
# Escribir sobre cada columna el porcentaje
for i, value in enumerate(comparacion.values()):
    ax.text(i, value, f'{value/total*100:.2f}%', ha='center', va='bottom')
# Fontsize
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.tight_layout()
plt.savefig('12-Percepcion.png')


# %%

