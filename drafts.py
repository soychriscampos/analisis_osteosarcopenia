# column rename
df = df.rename(columns={
    'altuna_en_cm': 'altura_cm',
    'imc1': 'imc_clas',
    'circunferencia_de_la_pantorrilla': 'circunferencia_pantorrilla',
    '%_de_grasa': '%_grasa',
    '%_de_musculo': '%_musculo',
    'masa_muscular_absoluta,_kg': 'masa_muscular_absoluta',
    'imme:_kg/m2': 'imme',
    'resultado': 'grasa_resultado',
    'resultado1': 'imme_resultado',
    'puntaje_sarc_-f': 'sarc_f_puntaje',
    'resultado_de_sarc-f': 'sarc_f_resultado',
    'resultado_de_lawton': 'resultado_lawton',
    'puntaje_de_katz': 'puntaje_katz',
    'resultado_de_katz': 'resultado_katz',
    'tiempo_de_ejercico': 'tiempo_ejercicio',
    'nivel_de_sarcopenia': 'nivel_sarcopenia'
})