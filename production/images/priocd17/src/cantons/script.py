import pandas as pd 

df = pd.read_csv('prio.csv', delimiter=';')

print df['BDV'][df['Priorisation a l echelle de la commune']=="Pas Prioritaire"].tolist()
















# def code_BDV(row):
# 	return str(row['CODDPT'])+'0'+str(row['CODSUBCOM'])+str(row['CODBURVOT'])

# df['code_bdv'] = df.apply(lambda row : code_BDV(row), axis=1)


# canton3 = list(set(df['code_bdv'][(df['NUMTOUR']==1) &  (df['CODDPT'] == 33) & (df['CODCAN']== 3)].tolist()))
# canton4 =  list(set(df['code_bdv'][(df['NUMTOUR']==1) & (df['CODDPT'] == 33) & (df['CODCAN']== 4)].tolist()))
# canton5 =  list(set(df['code_bdv'][(df['NUMTOUR']==1) & (df['CODDPT'] == 33) & (df['CODCAN']== 5)].tolist()))
# canton7 =  list(set(df['code_bdv'][(df['NUMTOUR']==1) & (df['CODDPT'] == 33) & (df['CODCAN']== 7)].tolist()))

# canton = canton3 + canton4 + canton5 + canton7

# print canton