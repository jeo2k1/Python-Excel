import pandas as pd

NOTAS_ALUMNOS_PATH = r'inputs/Notas_Alumnos.xlsx'

print(NOTAS_ALUMNOS_PATH)

dict_asig = {
    'LENGUA CASTELLANA Y LITERATURA': 'Lengua Castellana y Literatura',
    'BIOLOGIA': 'Biología',
    'GEOGRAFIA E HISTORIA': 'Geografía e Historia',
    'MATEMATICAS': 'Matemáticas',
    'INGLES': 'Inglés',
    'EDUCACION FISICA': 'Educación Física',
    'ETICA': 'Ética',
    'CULTURA CLASICA': 'Cultura clásica',
    'MUSICA': 'Música',
    'TECNOLOGIA': 'Tecnología',
    'EDUCACION PLASTICA': 'Educación Plástica',
    'FRANCES': 'Francés',
}
def deteccionErrores(df):
     err1, err2, err3 = False, False, False


     # Ordena la lista por Nombre
     alumnos_list = sorted(list(df['NOMBRE'].drop_duplicates()))
     # Ordena la lista por Asignatura
     asignatura_list = sorted(list(df['ASIGNATURA'].drop_duplicates()))
     for al in alumnos_list:
         for asig in asignatura_list:
             filt_alt_as_df = df[(df['NOMBRE'] == al)& (df['ASIGNATURA'] == asig)]
             print('')
             # Devuelve error si el alumno no tiene la asignatura asignada
             if (len(filt_alt_as_df) == 0):
                 print(f'Error: El alumno {al} no tiene la asignatura {asig} asignada')
                 err1 = True
             # Devuelve error si un alumno tiene una asignatura repetida
             elif(len(filt_alt_as_df) > 1):
                 print(f'El alumno {al} tiene la asignatura {asig} repetida {len(filt_alt_as_df)} veces')
                 err2 = True

# Devuelve error si una nota es menor a 0 y mayor a 10
     for index, row in df.iterrows():
        trimestre_list = ['NOTA T1', 'NOTA T2', 'NOTA T3']
        for trim in trimestre_list:
            if not ((row[trim] >= 0.0 and (row[trim]) <= 10.0)):
                print(f'Error: El alumno {al} no tiene el campo {trim} de la asignatura {asig} fuera de rango {str(row[trim])}')
                err3 = True

     if (err1 == True) or (err2 == True) or (err3 == True):
         print('')
         print('Debes corregir los errores para continuar la ejecucion')



def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')
    for index, row in excel_df.iterrows():
        print(index, row['NOMBRE'])

    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
    #print(asig_list)

    filter_td_asig = []  # lista vacia
    for item in asig_list:
        valor_td = dict_asig[item]
        filter_td_asig.append(valor_td)  # rellena la lista vacia con cada item del diccionario
    print('')

    # Llama a la funcion deteccionErrores()
    deteccionErrores(excel_df)


if __name__ == '__main__':
    main()
