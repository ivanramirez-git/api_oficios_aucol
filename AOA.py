import pandas as pd

Asociados=pd.read_csv('Asociados_df.csv', sep=';', decimal=',')
Oficios=pd.read_csv('FORMATO_DE_OFICIOS_MENSUALES.csv', sep=';', decimal=',')
print(Oficios.head())

s_Asociados=Asociados.sort_values("N OFICIOS")

print(s_Asociados.head())





