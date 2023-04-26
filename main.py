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


def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')
    for index, row in excel_df.iterrows():
        print(index, row['NOMBRE'])

    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
    print(asig_list)

    filter_td_asig = []
    for item in asig_list:
        valorTd = dict_asig[item]
        filter_td_asig.append(valorTd)
    print('')


if __name__ == '__main__':
    main()
