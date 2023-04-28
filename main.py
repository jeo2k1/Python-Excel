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
     alumnos_list = sorted(list(df['NOMBRE'].drop_duplicates()))
     asignatura_list = sorted(list(df['ASIGNATURA'].drop_duplicates()))
     for al in alumnos_list:
         for asig in asignatura_list:
             filt_alt_as_df = df[(df['NOMBRE'] == al)& (df['ASIGNATURA'] == asig)]
             print('')

             if (len(filt_alt_as_df) == 0):
                 print(f'Error: El alumno {al} no tiene la asignatura {asig} asignada')

             elif(len(filt_alt_as_df) > 1):
                 print(f'El alumno {al} tiene la asignatura {asig} repetida {len(filt_alt_as_df)} veces')






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

    deteccionErrores(excel_df)


if __name__ == '__main__':
    main()
