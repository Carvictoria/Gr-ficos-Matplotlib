import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk


def pizza():
    dados  =  pd.read_csv('dados.csv')
    df =  pd.DataFrame(dados)
    print(df)
    plt.figure(figsize=(8,6))
    plt.pie(df['Vendas'], labels=df['Mês'], autopct='%1.1f%%')
    plt.title('VENDAS POR MÊS')
    plt.show()


def barra():
    dados  =  pd.read_csv('dados.csv')
    df =  pd.DataFrame(dados)
    print(df)
    plt.figure(figsize=(8,6))
    plt.bar(df['Mês'],df['Lucro'])
    plt.title('VENDAS E LUCRO')
    plt.show()

def dispersao():
    dados  =  pd.read_csv('dados.csv')
    df =  pd.DataFrame(dados)
    print(df)
    plt.figure(figsize=(8,6))
    plt.scatter(df['Vendas'],df['Lucro'])
    plt.title('VENDAS E LUCRO')
    plt.show()



def linha():
    dados  =  pd.read_csv('dados.csv')
    df =  pd.DataFrame(dados)
    print(df)
    plt.figure(figsize=(8,6))
    plt.plot(df['Mês'],df['Lucro'])
    plt.title('EVOLUÇÃO DO LUCRO AO  LONGO DO MÊS')
    plt.show()    

root =  tk.Tk()

root.geometry('400x400')

texto = tk.Label(root, text= 'Gerador de Graficos', font=('arial', 16))
texto.pack()

btn = tk.Button(root, text='Grafico de pizza',fg = 'blue', font=('arial', 16), command=pizza)
btn.pack(pady=10)

btn2 = tk.Button(root, text='Grafico de barra',fg = 'blue', font=('arial', 16), command=barra)
btn2.pack(pady=10)


btn3 = tk.Button(root, text='Grafico de dispersão',fg = 'blue', font=('arial', 16), command=dispersao)
btn3.pack(pady=10)

btn4 = tk.Button(root, text='Grafico de linha', font=('arial', 16), fg = 'blue', command = linha)
btn4.pack(pady=10)

root.mainloop()