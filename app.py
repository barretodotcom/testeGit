import openpyxl
import pandas as pd

base_alunos_planilha = 'Base de Alunos.xlsx'
base_dengue = 'Base de Dengue.xlsx'
df_alunos = pd.read_excel(base_alunos_planilha)
df_dengue = pd.read_excel(base_dengue)

df_merge = pd.merge(df_alunos,df_dengue, how = 'inner', on = ['Nome','Nome do Pai'])

df_merge.to_excel('Mixed.xlsx')





