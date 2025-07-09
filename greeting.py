# Módulo para exibir a data e o horário atual, de forma amigável com base nas horas do dia
# Importando o módulo datetime para manipulação de datas e horas

from datetime import datetime
data_atual_aaaammdd = datetime.now().date()
dia_atual = datetime.now().day
mes_atual = datetime.now().month
ano_atual = datetime.now().year
horario_atual_hhmmsscccccc = datetime.now().time()
horario_atual_hhmmss = datetime.now().strftime('%H:%M:%S')
hora_atual = datetime.now().hour
min_atual = datetime.now().minute
seg_atual = datetime.now().second
cen_atual = datetime.now().microsecond 
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
dias_semana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 
               'Sexta-feira', 'Sábado', 'Domingo')

# Tratamento da data atual
mes_extenso = meses[int(mes_atual) - 1]
dia_semana_extenso = dias_semana[datetime.now().weekday()]

print (" ")
print (f" data_atual_aaaammdd: {data_atual_aaaammdd}, dia_atual: {dia_atual}, mes_atual: {mes_atual}, ano_atual: {ano_atual} ")
print (f" horario_atual: {horario_atual_hhmmsscccccc}, hora_atual : {hora_atual}, min_atual: {min_atual}, seg_atual: {seg_atual}, cen_atual: {cen_atual} ")

print (" ")
nome = input("Digite o seu nome: ")

if hora_atual >= 18:
    print(f"Boa noite, {nome}. Hoje é {dia_atual} de {mes_extenso} de {ano_atual}, {dia_semana_extenso}. Agora são {horario_atual.hhmmss} hs!")
elif hora_atual >= 12:
    print(f"Boa tarde, {nome}. Hoje é {dia_atual} de {mes_extenso} de {ano_atual}, {dia_semana_extenso}. Agora são {horario_atual_hhmmss} hs!")
else:   
    print(f"Bom dia, {nome}. Hoje é {dia_atual} de {mes_extenso} de {ano_atual}, {dia_semana_extenso}. Agora são {horario_atual.hhmmss} hs!")

print ("Aproveite o seu dia!")
print (" ")