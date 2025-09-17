import pyautogui
import pandas as pd
import time

# Passo 5: Repetir para todos os produtos

pyautogui.PAUSE = 0.8


# Passo 1: Entrar no site da empresa - http://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("http://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=813, y=376)
pyautogui.write("arthursiqueira@gmail.com")

# preencher a senha
pyautogui.press("tab")
pyautogui.write("senhaqualquer")

# logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados

produtos = pd.read_csv("produtos.csv")
print(produtos)

# Passo 4: Cadastrar 1 produto
for linha in produtos.index:
    pyautogui.click(x=756, y=257)

    codigo = produtos.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = produtos.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = produtos.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(produtos.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(produtos.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(produtos.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(produtos.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)



