import pandas as pd
import sys
from docxtpl import DocxTemplate
import shutil
import os

# Ruta Plantilla Excel
NOTAS_ALUMNOS_PATH = r'inputs/Notas_Alumnos.xlsx'

# Ruta Documento Word
PLANTILLA_CURSO_PATH = r'inputs/Plantilla_notas.docx'

# Ruta Salidas
PATH_OUTPUT = r'.\outputs'

CURSO = "2021/2022"



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


def deteccionerrores(df):
    err1, err2, err3 = False, False, False

    # Ordena la lista por Nombre
    alumnos_list = sorted(list(df['NOMBRE'].drop_duplicates()))
    # Ordena la lista por Asignatura
    asignatura_list = sorted(list(df['ASIGNATURA'].drop_duplicates()))
    for al in alumnos_list:
        for asig in asignatura_list:
            filt_alt_as_df = df[(df['NOMBRE'] == al) & (df['ASIGNATURA'] == asig)]
            print('')
            # Devuelve error si el alumno no tiene la asignatura asignada
            if (len(filt_alt_as_df) == 0):
                print(f'Error: El alumno {al} no tiene la asignatura {asig} asignada')
                err1 = True
            # Devuelve error si un alumno tiene una asignatura repetida
            elif (len(filt_alt_as_df) > 1):
                print(f'El alumno {al} tiene la asignatura {asig} repetida {len(filt_alt_as_df)} veces')
                err2 = True

    # Devuelve error si una nota es menor a 0 y mayor a 10
    for index, row in df.iterrows():
        trimestre_list = ['NOTA T1', 'NOTA T2', 'NOTA T3']
        for trim in trimestre_list:
            if not ((row[trim] >= 0.0 and (row[trim]) <= 10.0)):
                print(
                    f'Error: El alumno {al} no tiene el campo {trim} de la asignatura {asig} fuera de rango {str(row[trim])}')
                err3 = True

    if (err1 == True) or (err2 == True) or (err3 == True):
        print('')
        print('Debes corregir los errores para continuar la ejecucion')
        sys.exit(1)
    else:
        print('Ningun error detectado')

def eliminarTildes (texto):
    tildes_dict ={
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
    }
    textoSinTilde = texto

    for key in tildes_dict:
        textoSinTilde = textoSinTilde.replace(key,tildes_dict[key])

    return textoSinTilde

def eliminarCrearcarpetas(path):
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)

def crearWordAsignarTag(datos_alumnos, excel_df):
    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
    filter_td_asig = []  # lista vacia
    for item in asig_list:
        valor_td = dict_asig[item]
        filter_td_asig.append(valor_td.upper())  # rellena la lista vacia con cada item del diccionario
    print('')
    #### Documento Word
    docs_tpl = DocxTemplate(PLANTILLA_CURSO_PATH)
    nombre_alumno_list = sorted(list(datos_alumnos['NOMBRE']))
    #  nombre_alumno = nombre_alumno_list[0]
    for nombre_alumno in nombre_alumno_list:
        filt_datos_alumnos_df = datos_alumnos[(datos_alumnos['NOMBRE'] == nombre_alumno)]
        CLASE = filt_datos_alumnos_df.iloc[0]['CLASE']

        #Crear tabla de notas
        asignatura_list = []

        #Iterar sobre los items de asignatura
        for asig_idx in range(len(asig_list)):
            asign = asig_list[asig_idx]
            filt_al_as_excel_df = excel_df[(excel_df['NOMBRE'] == nombre_alumno) & (excel_df['ASIGNATURA'] == asign)]
            print('')


            asignatura_dic = {
                'nombre_asignatura': filter_td_asig[asig_idx],
                't1': round(filt_al_as_excel_df.iloc[0]['NOTA T1'],1),
                't2': round(filt_al_as_excel_df.iloc[0]['NOTA T2'],1),
                't3': round(filt_al_as_excel_df.iloc[0]['NOTA T3'],1),
            }
            asignatura_list.append(asignatura_dic)

        # Contexto, son las variables definidas en el archivo Word
        context = {
            'curso': CURSO,
            'nombre_alumno': nombre_alumno,
            'clase': CLASE,
            'asignatura_list': asignatura_list,
        }
        # Renderizacion de documento
        docs_tpl.render(context)
        titulo = 'NOTAS_' + nombre_alumno
        titulo = titulo.upper()
        titulo = eliminarTildes(titulo)
        titulo = titulo.replace(" ", "_")
        titulo += '.docx'

        # Guardamos el documento y definimos el nombre
        docs_tpl.save(PATH_OUTPUT + '\\' + titulo)


def main():

    eliminarCrearcarpetas(PATH_OUTPUT)


#### Planilla Excel
    ####### Leemos excel hoja notas y datos alumnos
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')
    datos_alumnos = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Datos_Alumnos')

#    for index, row in excel_df.iterrows():
#        print(index, row['NOMBRE'])


    deteccionerrores(excel_df)


    crearWordAsignarTag(datos_alumnos,excel_df)



if __name__ == '__main__':
    main()