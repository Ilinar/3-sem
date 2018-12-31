from tkinter import *
import tkinter as tk
import random
from sys import setrecursionlimit
setrecursionlimit(10000)

def menu():
    global window
    window = tk.Tk()
    window.title('RSA')
    
    bg_image = tk.PhotoImage(file = 'matrix.png')
    w = bg_image.width()
    h = bg_image.height()
    window.geometry('1000x700')
    cv = tk.Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bg_image, anchor='nw')
    
    
    key = tk.Button(cv, text = 'Tworzenie pary kluczy', command = keymenu, overrelief = RIDGE,
                    background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                    width = 20, font = ("Times New Roman", 40))
    key.pack(pady=30)
    
    szyfrowanie = tk.Button(cv, text = 'Szyfrowanie', command = szyfrowaniemenu, overrelief = RIDGE,
                            background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white',
                            width = 20, font = ("Times New Roman", 40))
    szyfrowanie.pack(pady=30)
    
    szyfrogram = tk.Button(cv, text = 'Czytaj szyfrogram', overrelief = RIDGE,
                           background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                           width = 20, font = ("Times New Roman", 40))
    szyfrogram.pack(pady=30)
    
    exit = tk.Button(cv, text = 'Wyjście', command = window.destroy, overrelief = RIDGE,
                     background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                     width = 20, font = ("Times New Roman", 40))
    exit.pack(pady=30)

    tk.mainloop()
    
###############################################################################################################################

def keymenu():
    global windowkey
    global text
    global text2
    windowkey = tk.Toplevel()
    windowkey.title('RSA')
    windowkey.configure(background='black')
    
    keygenerate = tk.Button(windowkey, text = "Stwórz klucze", command = printkey,
                             background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                             width = 60, font = ("Times New Roman", 40))
    keygenerate.pack()
    
    text = tk.StringVar()
    label = tk.Label(windowkey, textvariable = text,
                     background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                     width = 50, font = ("Times New Roman", 40))
    label.pack()
    text.set('Klucz prywatny:')
    
    text2 = tk.StringVar()
    label2 = tk.Label(windowkey, textvariable = text2,
                      background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                      width = 50, font = ("Times New Roman", 40))
    label2.pack()
    text2.set('Klucz publiczny:')
    
#-------------------------------------------------------------------------------------------------------------------------------#
    
def randomprime():
    """Losowanie liczby pierwszej."""
    global primenum
    primenum= random.randrange(100, 900)
    
    for i in range(2, primenum):
        if primenum % i == 0:
            randomprime()
            break
    else:
        return
    
def diffrentnum():
    """Ponowne losowanie w przypadku dwóch identycznych liczb pierwszych."""
    global q
    randomprime()
    q = primenum
    if q == p:
        diffrentnum()
    else:
        return
    
def euclidean():
    """Algorytm Euklidesa, losowanie i dopasowywanie liczby by tworzyć parę licz względnie pierwszych."""
    global num
    num = random.randrange(3,n)
    if num % 2 == 0:
        euclidean()
    else:
        if num == fi:
            euclidean()
        a = num
        b = fi
        while a != b:
            if a > b:
                a = a - b
            elif a < b:
                b = b - a
        if a == b == 1:
            return
        else:
            euclidean()

def ex_euclidean():
    """Rozszerzony algorytm Euklidesa, szukanie odwrotności modulo."""
    global d
    a = e
    b = fi
    u = 1
    x = 0
    w = a
    z = b
    while w != 0:
        if w < z:
            tym = w
            w = z
            z = tym
            tym = u
            u = x
            x = tym
        k = int(w / z)
        u = u - (k * x)
        w = w - (k * z)
    if x < 0:
        x = x + b
    d = x
    return d
    
def keygenerate():
    """Tworzenie pary kluczy."""
    randomprime()
    global p
    p = primenum
    diffrentnum()
    global fi
    fi = (p-1) * (q-1)
    global n
    n = p * q
    euclidean()
    global e
    e = num
    ex_euclidean()
    if e == d:
        keygenerate()
        return
    return    
    
def printkey():
    keygenerate()
    se = str(e)
    sd = str(d)
    sn = str(n)
    key = 'klucz publiczny: ' + se + ' ' + sn
    key2 = 'klucz prywatny: ' + sd + ' ' + sn
    text.set(key)
    text2.set(key2)
    
###############################################################################################################################

def readkey():
    global x , y
    klucz = entryklucz.get()
    klucz = klucz.split()
    try:
        x = int(klucz[0])
        y = int(klucz[1])
    except (ValueError, IndexError):
        szyfrogramtekst = 'Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.'
        szyfrogrambox.set(szyfrogramtekst)
        return
    try:
        z = (klucz[2])
        szyfrogramtekst = 'Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.'
        szyfrogrambox.set(szyfrogramtekst)
        return
    except (ValueError, IndexError):
        return
    return

###############################################################################################################################

def szyfrowaniemenu():
    global window2
    global entryklucz
    global entryjawny
    global szyfrogrambox
    global szyfrogramtekst
    global nazwastaregopliku
    global nazwanowegopliku
    window2 = tk.Toplevel()
    window2.title('RSA')
    window2.configure(background='black')
    
    szyfrogramtekst = 'Tutaj zobaczysz szyfrogram'
    
    label0 = tk.Label(window2, text = 'Podaj klucz:',
                     background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                     width = 50, font = ("Times New Roman", 40))
    label0.pack()
    
    entryklucz = tk.Entry(window2, background = 'black', foreground = 'white', width = 50, font = ("Times New Roman", 40))
    entryklucz.pack()
    
    label1 = tk.Label(window2, text = 'Tekst jawny:',
                    background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                    width = 50, font = ("Times New Roman", 40))
    label1.pack()
    
    entryjawny = tk.Entry(window2, background = 'black', foreground = 'white', width = 50, font = ("Times New Roman", 40))
    entryjawny.pack()
    
    label2 = tk.Label(window2, text = 'Szyfrogram:',
                     background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                     width = 50, font = ("Times New Roman", 40))
    label2.pack()
    
    szyfrogrambox = tk.StringVar()
    label3 = tk.Label(window2, textvariable = szyfrogrambox,
                     background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                     width = 0, font = ("Times New Roman", 40))
    label3.pack()
    szyfrogrambox.set(szyfrogramtekst)
    
    okszyfruj = tk.Button(window2, text = 'Szyfruj', command = szyfruj,
                    background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                    width = 20, font = ("Times New Roman", 40))
    okszyfruj.pack()
    
    nazwastaregopliku = tk.Entry(window2, background = 'black', foreground = 'white', width = 50, font = ("Times New Roman", 40))
    nazwastaregopliku.pack()
    
    nazwanowegopliku = tk.Entry(window2, background = 'black', foreground = 'white', width = 50, font = ("Times New Roman", 40))
    nazwanowegopliku.pack()
    
    okszyfrujplik = tk.Button(window2, text = 'Szyfruj plik', command = szyfrujplik,
                    background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white', 
                    width = 20, font = ("Times New Roman", 40))
    okszyfrujplik.pack()
    
#-------------------------------------------------------------------------------------------------------------------------------#

def wliczby(jawny):
    """Zamiana teksu jawnego na jawny ciąg liczb."""
    global liczby
    liczby = []
    lista = list(jawny)
    for i in range(len(lista)):
        liczby.append(ord(lista.pop(0)))
    return

def wszyfrogram(liczby):
    """Zamiana jawnego ciągu liczb na szyfrogram."""
    global szyfrogram
    szyfrogram = [(t**e) % n for t in liczby]
    return

#-------------------------------------------------------------------------------------------------------------------------------#

def szyfruj():
    readkey()
    global e,n,szyfrogram
    e = x
    n = y
    wliczby(entryjawny.get())
    wszyfrogram(liczby)
    szyfrogram = ' '.join(map(str,szyfrogram))
    szyfrogramtekst = szyfrogram
    szyfrogrambox.set(szyfrogramtekst)
    
#-------------------------------------------------------------------------------------------------------------------------------#
    
def szyfrujplik():
    readkey()
    global e,n,szyfrogram
    e = x
    n = y
    staryplik = nazwastaregopliku.get()
    nowyplik = nazwanowegopliku.get()
    
    try:
        plikjawny = open(staryplik)
        jawny = plikjawny.read()
    finally:
        plikjawny.close()
    
    wliczby(jawny)
    wszyfrogram(liczby)
    szyfrogram = ' '.join(map(str,szyfrogram))
    szyfrogramtekst = szyfrogram   
    
    try:
        zaszyfrowanyplik = open(nowyplik, 'w')
        zaszyfrowanyplik.write(szyfrogramtekst)
    finally:
        zaszyfrowanyplik.close()

###############################################################################################################################

menu()
