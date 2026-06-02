import tkinter as tk
import math  # Nodig voor het berekenen van de cirkelstraal en formules
import random  # Nodig voor het schudden van de memorykaarten
from tkinter import messagebox, colorchooser  # Voor pop-ups en de kleurkiezer

# GLOBALE VARIABELEN VOOR HET TEKENEN
old_x = None
old_y = None
huidige_kleur = "black"  # Standaard tekenen we met zwart
fill_kleur = None       # Standaard zijn vormen niet gevuld (transparant)
dikte = 1

# NIEUWE VARIABELEN VOOR DE VORMEN MODUS
# Modus kan zijn: "vrij", "lijn_klik1", "lijn_klik2", "rechthoek_klik1", "rechthoek_klik2", "cirkel_klik", "txt_klik1"
modus = "vrij"          
start_x = None
start_y = None
tijdelijke_vorm = None  # Houdt de vorm vast tijdens het slepen

# FUNCTIES VOOR NAVIGATIE
def toon_pagina1():
    pagina1.tkraise()

def toon_pagina2():
    pagina2.tkraise()

def toon_pagina3():
    pagina3.tkraise()
    
def toon_pagina4():
    pagina4.tkraise()
    
def toon_pagina5():
    pagina5.tkraise()
    
def toon_pagina6():
    pagina6.tkraise()

# FUNCTIES VOOR THEMA'S
def dark_mode():
    venster.config(bg="darkgrey")
    pagina1.config(bg="darkgrey")
    pagina2.config(bg="darkgrey")
    pagina3.config(bg="darkgrey")
    pagina4.config(bg="darkgrey")
    pagina5.config(bg="darkgrey")
    pagina6.config(bg="darkgrey")
    canvas_tekenen.config(bg="lightgrey")

def light_mode():
    venster.config(bg="#f0f0f0")
    pagina1.config(bg="white")
    pagina2.config(bg="white")
    pagina3.config(bg="white")
    pagina4.config(bg="white")
    pagina5.config(bg="white")
    pagina6.config(bg="white")
    canvas_tekenen.config(bg="white")

# FUNCTIE VOOR DE QUIZ (PAGINA 2)
def controleer():
    rb1.config(fg="black")
    rb2.config(fg="black")
    rb21.config(fg="black")
    rb22.config(fg="black")
    rb23.config(fg="black")
    rb24.config(fg="black")
    lb.config(fg="black")
    cb41.config(fg="black")
    cb42.config(fg="black")
    cb43.config(fg="black")
    cb44.config(fg="black")
    rb51.config(fg="black")
    rb52.config(fg="black")

    score = 0
    fouten = 0    
    
    if v1.get() == "Parijs":
        score += 1
        rb1.config(fg="green")
    else:
        fouten += 1
        if v1.get() == "Lyon":
            rb2.config(fg="red")

    if v2.get() == "Niger":
        score += 1
        rb21.config(fg="green")
    else:
        fouten += 1
        if v2.get() == "Nigeria":
            rb22.config(fg="red")
        elif v2.get() == "België":
            rb23.config(fg="red")
        elif v2.get() == "Chad":
            rb24.config(fg="red")

    chosen = lb.curselection()
    if len(chosen) == 1 and lb.get(chosen[0]) == "Italië":
        score += 1
        lb.config(fg="green")
    else:
        fouten += 1
        lb.config(fg="red")

    if v4_optie2.get() == 1 and v4_optie1.get() == 0 and v4_optie3.get() == 0 and v4_optie4.get() == 0:
        score += 1
        cb42.config(fg="green")
    else:
        fouten += 1
        if v4_optie1.get() == 1:
            cb41.config(fg="red")
        if v4_optie3.get() == 1:
            cb43.config(fg="red")
        if v4_optie4.get() == 1:
            cb44.config(fg="red")

    if v5.get() == "Seine":
        score += 1
        rb51.config(fg="green")
    else:
        fouten += 1
        if v5.get() == "Rijn":
            rb52.config(fg="red")

    resultaat.config(text=f"Score: {score} juist, {fouten} fout", fg="white", bg="blue")

    if score == 5:
        messagebox.showinfo("Perfect!", "Wauw, je hebt alle vragen goed! 🏆")
    elif score >= 3:
        messagebox.showinfo("Goed gedaan", f"Netjes! Je score is {score}/5.")
    else:
        messagebox.showwarning("Helaas", f"Oeps, je had {fouten} fouten. Volgende keer beter! 🙃")
    
# FUNCTIES VOOR HET TEKENEN (PAGINA 3)
def activeer_text_modus():
    global modus
    modus = "txt_klik1"
    canvas_tekenen.config(cursor="xterm") # Text-cursor look

def activeer_lijn_modus():
    global modus, fill_kleur
    modus = "lijn_klik1"
    fill_kleur = None # Lijnen kunnen niet gevuld worden
    canvas_tekenen.config(cursor="cross")

def activeer_rechthoek_modus():
    global modus
    modus = "rechthoek_klik1"
    canvas_tekenen.config(cursor="cross")

def activeer_cirkel_modus():
    global modus
    modus = "cirkel_klik"
    canvas_tekenen.config(cursor="tcross") 

def start_tekenen(event):
    global old_x, old_y, modus, start_x, start_y
    
    if modus == "lijn_klik1":
        start_x = event.x
        start_y = event.y
        modus = "lijn_klik2"
        
    elif modus == "lijn_klik2":
        canvas_tekenen.create_line(
            start_x, start_y, event.x, event.y, 
            width=dikte, fill=huidige_kleur, capstyle=tk.ROUND
        )
        modus = "vrij"
        canvas_tekenen.config(cursor="")
        
    elif modus == "rechthoek_klik1":
        start_x = event.x
        start_y = event.y
        modus = "rechthoek_klik2"
        
    elif modus == "rechthoek_klik2":
        canvas_tekenen.create_rectangle(
            start_x, start_y, event.x, event.y, 
            width=dikte, outline=huidige_kleur, fill=fill_kleur
        )
        modus = "vrij"
        canvas_tekenen.config(cursor="")
        
    elif modus == "cirkel_klik":
        start_x = event.x
        start_y = event.y
        
    elif modus == "txt_klik1":
        # Haal de tekst op uit de entrybox
        tekst_om_te_tekenen = entry_canvas_tekst.get()
        if tekst_om_te_tekenen == "":
            tekst_om_te_tekenen = "Tekst" # Standaard fallback
            
        # Bereken de lettergrootte op basis van de lijndikte (minimaal 10)
        font_grootte = max(10, dikte * 3)
        
        # Teken de tekst op het canvas
        canvas_tekenen.create_text(
            event.x, event.y, 
            text=tekst_om_te_tekenen, 
            fill=huidige_kleur, 
            font=("Arial", font_grootte),
            anchor="w" # Tekst begint vanaf het klikpunt naar rechts
        )
        modus = "vrij"
        canvas_tekenen.config(cursor="")
        
    else:
        old_x = event.x
        old_y = event.y

def teken(event):
    global old_x, old_y, huidige_kleur, dikte, modus, start_x, start_y, tijdelijke_vorm
    
    if modus == "vrij":
        if old_x is not None and old_y is not None:
            canvas_tekenen.create_line(
                old_x, old_y, event.x, event.y, 
                width=dikte, fill=huidige_kleur, capstyle=tk.ROUND, smooth=tk.TRUE
            )
        old_x = event.x
        old_y = event.y
        
    elif modus == "cirkel_klik" and start_x is not None and start_y is not None:
        if tijdelijke_vorm is not None:
            canvas_tekenen.delete(tijdelijke_vorm)
            
        straal = math.sqrt((event.x - start_x)**2 + (event.y - start_y)**2)
        
        tijdelijke_vorm = canvas_tekenen.create_oval(
            start_x - straal, start_y - straal, 
            start_x + straal, start_y + straal, 
            width=dikte, outline=huidige_kleur, fill=fill_kleur
        )

def stop_tekenen(event):
    global old_x, old_y, modus, start_x, start_y, tijdelijke_vorm
    if modus == "vrij":
        old_x = None
        old_y = None
    elif modus == "cirkel_klik":
        start_x = None
        start_y = None
        tijdelijke_vorm = None
        modus = "vrij"
        canvas_tekenen.config(cursor="")

def dikker_lijn():
    global dikte
    dikte += 5
    label_dikte_waarde.config(text=dikte)

def dunner_lijn():
    global dikte
    if dikte > 5:
        dikte -= 5
    else:
        dikte = 1
    label_dikte_waarde.config(text=dikte)

def wis_canvas():
    canvas_tekenen.delete("all")

def kies_kleur(kleur):
    global huidige_kleur
    huidige_kleur = kleur
    
def teken_scoregrafiek():
    canvas1.delete("all")  
    punten = [int(entry_alex.get()), int(entry_sam.get()), int(entry_noor.get())]
    namen = ["Alex", "Sam", "Noor"]
    kleuren = ["blue", "green", "red"]
    
    canvas1.create_line(40, 250, 350, 250, width=2)
    
    x = 60
    for i in range(len(punten)):
        hoogte = punten[i]
        kleur = kleuren[i]
        naam = namen[i]
        
        canvas1.create_rectangle(x, 250 - hoogte, x + 50, 250, fill=kleur)
        canvas1.create_text(x + 25, 250 - hoogte - 10, text=str(hoogte))
        canvas1.create_text(x + 25, 265, text=naam)
        x += 90   

# ==================== LOGIEK MEMORY (PAGINA 5) ====================
memory_knoppen = []
memory_waarden = []
omgedraaid = []
gevonden_paartjes = 0

def start_memory():
    global memory_waarden, omgedraaid, gevonden_paartjes, memory_knoppen
    gevonden_paartjes = 0
    omgedraaid = []
    
    kleuren = ["red", "blue", "green", "yellow", "purple", "orange", "brown", "pink"]
    memory_waarden = kleuren + kleuren
    random.shuffle(memory_waarden)
    
    for i, knop in enumerate(memory_knoppen):
        knop.config(bg="gray", text="?", state="normal")

def kaart_klik(index):
    global omgedraaid, gevonden_paartjes
    
    if index in omgedraaid or len(omgedraaid) >= 2:
        return
        
    memory_knoppen[index].config(bg=memory_waarden[index], text="")
    omgedraaid.append(index)
    
    if len(omgedraaid) == 2:
        venster.after(1000, controleer_match)

def controleer_match():
    global omgedraaid, gevonden_paartjes
    idx1, idx2 = omgedraaid[0], omgedraaid[1]
    
    if memory_waarden[idx1] == memory_waarden[idx2]:
        memory_knoppen[idx1].config(state="disabled", bg="white")
        memory_knoppen[idx2].config(state="disabled", bg="white")
        gevonden_paartjes += 1
        if gevonden_paartjes == 8:
            messagebox.showinfo("Gefeliciteerd!", "Je hebt alle paartjes gevonden! 🎉")
    else:
        memory_knoppen[idx1].config(bg="gray", text="?")
        memory_knoppen[idx2].config(bg="gray", text="?")
        
    omgedraaid = []

# ==================== LOGIEK REKENMACHINE (PAGINA 6) ====================
def bereken_pythagoras():
    try:
        a = float(entry_zijde_a.get())
        b = float(entry_zijde_b.get())
        c = math.sqrt(a**2 + b**2)
        label_res_pyth.config(text=f"Schuine zijde (c) = {c:.2f}")
        lijst_historie.insert(tk.END, f"Pythagoras: a={a}, b={b} -> c={c:.2f}")
    except ValueError:
        messagebox.showerror("Fout", "Vul geldige getallen in!")

def bereken_cirkel():
    try:
        r = float(entry_straal.get())
        opp = math.pi * (r**2)
        omtrek = 2 * math.pi * r
        label_res_cirkel.config(text=f"Opp: {opp:.2f} | Omtrek: {omtrek:.2f}")
        lijst_historie.insert(tk.END, f"Cirkel r={r} -> Opp={opp:.2f}, Omtr={omtrek:.2f}")
    except ValueError:
        messagebox.showerror("Fout", "Vul een geldig getal in!")

def wis_historie():
    lijst_historie.delete(0, tk.END)


# HOOFDVENSTER
venster = tk.Tk()
venster.title("Menu Voorbeeld")
venster.geometry("600x750")

# CONTAINER VOOR PAGINA'S
container = tk.Frame(venster)
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# DE PAGINA-FRAMES (Nu alle 6)
pagina1 = tk.Frame(container, bg="white")
pagina2 = tk.Frame(container, bg="white")
pagina3 = tk.Frame(container, bg="white")
pagina4 = tk.Frame(container, bg="white")
pagina5 = tk.Frame(container, bg="white")
pagina6 = tk.Frame(container, bg="white")

pagina1.grid(row=0, column=0, sticky="nsew")
pagina2.grid(row=0, column=0, sticky="nsew")
pagina3.grid(row=0, column=0, sticky="nsew")
pagina4.grid(row=0, column=0, sticky="nsew")
pagina5.grid(row=0, column=0, sticky="nsew")
pagina6.grid(row=0, column=0, sticky="nsew")


# PAGINA 1: INSTELLINGEN
label1 = tk.Label(pagina1, text="Instellingen", font=("Arial", 16), bg="white")
label1.pack(pady=20)

knop_dark = tk.Button(pagina1, text="Dark Mode", command=dark_mode, width=20)
knop_dark.pack(pady=10)

knop_light = tk.Button(pagina1, text="Light Mode", command=light_mode, width=20)
knop_light.pack(pady=10)


# PAGINA 2: DE QUIZ
v1 = tk.StringVar()
tk.Label(pagina2, text="1. Wat is de hoofdstad van Frankrijk?", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=(15,5))
rb1 = tk.Radiobutton(pagina2, text="Parijs", variable=v1, value="Parijs", bg="white")
rb1.grid(row=1, column=0, sticky="w", padx=20)

rb2 = tk.Radiobutton(pagina2, text="Lyon", variable=v1, value="Lyon", bg="white")
rb2.grid(row=2, column=0, sticky="w", padx=20)

tk.Label(pagina2, text="2. Welke land is dit?", font=("Arial", 10, "bold"), bg="white").grid(row=3, column=0, sticky="w", padx=10, pady=(15,5))
try:
    img_orig = tk.PhotoImage(file="Nigeria.png")    
    img = img_orig.subsample(3, 3)                  
    lbl_img = tk.Label(pagina2, image=img, bg="white") 
    lbl_img.image = img                                                              
    lbl_img.grid(row=4, column=0, pady=5)
except:
    tk.Label(pagina2, text="[Afbeelding mist]", bg="white").grid(row=4, column=0)

v2 = tk.StringVar()
rb21 = tk.Radiobutton(pagina2, text="Niger", variable=v2, value="Niger", bg="white")
rb21.grid(row=5, column=0, sticky="w", padx=20)

rb22 = tk.Radiobutton(pagina2, text="Nigeria", variable=v2, value="Nigeria", bg="white")
rb22.grid(row=6, column=0, sticky="w", padx=20)

rb23 = tk.Radiobutton(pagina2, text="België", variable=v2, value="België", bg="white")
rb23.grid(row=7, column=0, sticky="w", padx=20)

rb24 = tk.Radiobutton(pagina2, text="Chad", variable=v2, value="Chad", bg="white")
rb24.grid(row=8, column=0, sticky="w", padx=20)

tk.Label(pagina2, text="3. Land volledig in Europa?", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=(10,5))
lb = tk.Listbox(pagina2, selectmode=tk.MULTIPLE, height=4, width=15)
lb.insert(0, "Turkije"), lb.insert(1, "Canada"), lb.insert(2, "Italië"), lb.insert(3, "Japan")
lb.grid(row=1, column=1, rowspan=2, padx=20, sticky="w")

tk.Label(pagina2, text="4. Hoeveel landen zijn er?", font=("Arial", 10, "bold"), bg="white").grid(row=3, column=1, sticky="w", padx=10, pady=(15,5))
v4_optie1, v4_optie2, v4_optie3, v4_optie4 = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
cb41 = tk.Checkbutton(pagina2, text="185", variable=v4_optie1, bg="white")
cb41.grid(row=4, column=1, sticky="w", padx=20, pady=2)

cb42 = tk.Checkbutton(pagina2, text="195", variable=v4_optie2, bg="white")
cb42.grid(row=5, column=1, sticky="w", padx=20, pady=2)

cb43 = tk.Checkbutton(pagina2, text="205", variable=v4_optie3, bg="white")
cb43.grid(row=6, column=1, sticky="w", padx=20, pady=2)

cb44 = tk.Checkbutton(pagina2, text="215", variable=v4_optie4, bg="white")
cb44.grid(row=7, column=1, sticky="w", padx=20, pady=2)

tk.Label(pagina2, text="5. Rivier door Parijs?", font=("Arial", 10, "bold"), bg="white").grid(row=8, column=1, sticky="w", padx=10, pady=(15,5))
v5 = tk.StringVar()
rb51 = tk.Radiobutton(pagina2, text="Seine", variable=v5, value="Seine", bg="white")
rb51.grid(row=9, column=1, sticky="w", padx=20)

rb52 = tk.Radiobutton(pagina2, text="Rijn", variable=v5, value="Rijn", bg="white")
rb52.grid(row=10, column=1, sticky="w", padx=20)

tk.Button(pagina2, text="Controleer", command=controleer, width=20, bg="lightblue").grid(row=11, column=0, columnspan=2, pady=30)
resultaat = tk.Label(pagina2, text="Vul de quiz in!", bg="white")
resultaat.grid(row=12, column=0, columnspan=2)


# PAGINA 3: TEKENEN
label3 = tk.Label(pagina3, text="Microsoft paint 2.0", font=("Arial", 16), bg="white")
label3.pack(pady=10)

frame_kleuren1 = tk.Frame(pagina3, bg="white")
frame_kleuren1.pack(pady=5)
frame_kleuren2 = tk.Frame(pagina3,bg="white")
frame_kleuren2.pack(pady=5)

frame_dikte = tk.Frame(pagina3, bg="white")
frame_dikte.pack(pady=5)

frame_figuren = tk.Frame(pagina3, bg="white")
frame_figuren.pack(pady=5)

# INVOERVELD VOOR TEKST MODUS (Nieuw)
frame_tekst_invoer = tk.Frame(pagina3, bg="white")
frame_tekst_invoer.pack(pady=5)
tk.Label(frame_tekst_invoer, text="Tekst voor TXT-modus:", bg="white").pack(side="left", padx=5)
entry_canvas_tekst = tk.Entry(frame_tekst_invoer, width=20)
entry_canvas_tekst.insert(0, "Typ hier...")
entry_canvas_tekst.pack(side="left", padx=5)

# Kleurknoppen
tk.Button(frame_kleuren1, bg="black", width=4, command=lambda: kies_kleur("black")).pack(side="left", padx=5)
tk.Button(frame_kleuren1, bg="red", width=4, command=lambda: kies_kleur("red")).pack(side="left", padx=5)
tk.Button(frame_kleuren1, bg="blue", width=4, command=lambda: kies_kleur("blue")).pack(side="left", padx=5)
tk.Button(frame_kleuren1, bg="green", width=4, command=lambda: kies_kleur("green")).pack(side="left", padx=5)
tk.Button(frame_kleuren1, bg="yellow", width=4, command=lambda: kies_kleur("yellow")).pack(side="left", padx=5)
tk.Button(frame_kleuren1, bg="white", width=4, command=lambda: kies_kleur("white")).pack(side="left", padx=5)

tk.Button(frame_kleuren2, bg="brown",width=4, command= lambda: kies_kleur("brown")).pack(side="left",padx=5)
tk.Button(frame_kleuren2, bg="orange",width=4, command= lambda: kies_kleur("orange")).pack(side="left",padx=5)
tk.Button(frame_kleuren2, bg="lightblue",width=4, command= lambda: kies_kleur("lightblue")).pack(side="left",padx=5)
tk.Button(frame_kleuren2, bg="lightgreen",width=4, command= lambda: kies_kleur("lightgreen")).pack(side="left",padx=5)
tk.Button(frame_kleuren2, bg="purple",width=4, command= lambda: kies_kleur("purple")).pack(side="left",padx=5)
tk.Button(frame_kleuren2, bg="gray",width=4, command= lambda: kies_kleur("gray")).pack(side="left",padx=5)

# Dikteknoppen
tk.Button(frame_dikte, bg="white", width=10, command=dunner_lijn, text="Lijn dunner").pack(side="left", padx=5)
tk.Button(frame_dikte, bg="white", width=10, command=dikker_lijn, text="Lijn dikker").pack(side="left", padx=5)
label_dikte_waarde = tk.Label(frame_dikte, bg="white", text=dikte, font=("Arial", 10, "bold"))
label_dikte_waarde.pack(side="left", padx=5)

# Figuren
tk.Button(frame_figuren, bg="white", width=10, command=activeer_lijn_modus, text="Rechte Lijn").pack(side="left", padx=5)
tk.Button(frame_figuren, bg="white", width=10, command=activeer_rechthoek_modus, text="Rechthoek").pack(side="left", padx=5)
tk.Button(frame_figuren, bg="white", width=10, command=activeer_cirkel_modus, text="Cirkel").pack(side="left", padx=5)
tk.Button(frame_figuren, bg="white", width=10, command=activeer_text_modus, text="TXT").pack(side="left", padx=5)

# Het tekenveld
canvas_tekenen = tk.Canvas(pagina3, bg="white", highlightthickness=1, highlightbackground="black")
canvas_tekenen.pack(fill="both", expand=True, padx=20, pady=5)

canvas_tekenen.bind("<Button-1>", start_tekenen)
canvas_tekenen.bind("<B1-Motion>", teken)
canvas_tekenen.bind("<ButtonRelease-1>", stop_tekenen)

knop_wis = tk.Button(pagina3, text="Wis Tekening", command=wis_canvas)
knop_wis.pack(pady=10)


# PAGINA 4: GRAFIEKEN
label_titel4 = tk.Label(pagina4, text="Grafiek", font=("Arial", 12, "bold"), bg="white")
label_titel4.pack(pady=10)

frame_input4 = tk.Frame(pagina4, bg="white")
frame_input4.pack()

tk.Label(frame_input4, text="Alex:", bg="white").grid(row=0, column=0, padx=5)
entry_alex = tk.Entry(frame_input4, width=5)
entry_alex.insert(0, "150")  
entry_alex.grid(row=0, column=1, padx=5)

tk.Label(frame_input4, text="Sam:", bg="white").grid(row=0, column=2, padx=5)
entry_sam = tk.Entry(frame_input4, width=5)
entry_sam.insert(0, "230")  
entry_sam.grid(row=0, column=3, padx=5)

tk.Label(frame_input4, text="Noor:", bg="white").grid(row=0, column=4, padx=5)
entry_noor = tk.Entry(frame_input4, width=5)
entry_noor.insert(0, "180")  
entry_noor.grid(row=0, column=5, padx=5)

canvas1 = tk.Canvas(pagina4, width=400, height=300, bg="white", highlightthickness=1, highlightbackground="black")
canvas1.pack(pady=10)

knop_teken4 = tk.Button(pagina4, text="Teken Grafiek", command=teken_scoregrafiek)
knop_teken4.pack()


# ==================== PAGINA 5: MEMORY GAME ====================
label_titel5 = tk.Label(pagina5, text="Memory Spel", font=("Arial", 16, "bold"), bg="white")
label_titel5.pack(pady=10)

frame_grid = tk.Frame(pagina5, bg="white")
frame_grid.pack(pady=10)

# Maak 16 knoppen aan in een 4x4 grid
for i in range(16):
    knop = tk.Button(frame_grid, text="?", font=("Arial", 14, "bold"), bg="gray", width=6, height=3,
                     command=lambda i=i: kaart_klik(i))
    row = i // 4
    col = i % 4
    knop.grid(row=row, column=col, padx=5, pady=5)
    memory_knoppen.append(knop)

knop_restart = tk.Button(pagina5, text="Start / Reset Spel", command=start_memory, bg="lightblue")
knop_restart.pack(pady=15)

# Start de eerste memory-sessie
start_memory()


# ==================== PAGINA 6: WISKUNDIGE TOOLS ====================
label_titel6 = tk.Label(pagina6, text="Wiskundige Tools", font=("Arial", 16, "bold"), bg="white")
label_titel6.pack(pady=10)

# Deel 1: Pythagoras
frame_pyth = tk.LabelFrame(pagina6, text="Stelling van Pythagoras (a² + b² = c²)", bg="white", padx=10, pady=10)
frame_pyth.pack(fill="x", padx=20, pady=5)

tk.Label(frame_pyth, text="Zijde a:", bg="white").grid(row=0, column=0)
entry_zijde_a = tk.Entry(frame_pyth, width=8)
entry_zijde_a.grid(row=0, column=1, padx=5)

tk.Label(frame_pyth, text="Zijde b:", bg="white").grid(row=0, column=2)
entry_zijde_b = tk.Entry(frame_pyth, width=8)
entry_zijde_b.grid(row=0, column=3, padx=5)

tk.Button(frame_pyth, text="Bereken", command=bereken_pythagoras).grid(row=0, column=4, padx=10)
label_res_pyth = tk.Label(frame_pyth, text="Schuine zijde (c) = ...", font=("Arial", 10, "bold"), bg="white", fg="blue")
label_res_pyth.grid(row=1, column=0, columnspan=5, pady=5, sticky="w")

# Deel 2: Cirkel
frame_cirkel = tk.LabelFrame(pagina6, text="Cirkel Berekenaar", bg="white", padx=10, pady=10)
frame_cirkel.pack(fill="x", padx=20, pady=5)

tk.Label(frame_cirkel, text="Straal (r):", bg="white").grid(row=0, column=0)
entry_straal = tk.Entry(frame_cirkel, width=8)
entry_straal.grid(row=0, column=1, padx=5)

tk.Button(frame_cirkel, text="Bereken", command=bereken_cirkel).grid(row=0, column=2, padx=10)
label_res_cirkel = tk.Label(frame_cirkel, text="Oppervlakte & Omtrek = ...", font=("Arial", 10, "bold"), bg="white", fg="green")
label_res_cirkel.grid(row=1, column=0, columnspan=3, pady=5, sticky="w")

# Deel 3: Geschiedenis (Listbox)
frame_hist = tk.LabelFrame(pagina6, text="Geschiedenis van Berekeningen", bg="white", padx=10, pady=10)
frame_hist.pack(fill="both", expand=True, padx=20, pady=10)

lijst_historie = tk.Listbox(frame_hist, height=6)
lijst_historie.pack(fill="both", expand=True, side="left")

scroll_hist = tk.Scrollbar(frame_hist, command=lijst_historie.yview)
scroll_hist.pack(side="right", fill="y")
lijst_historie.config(yscrollcommand=scroll_hist.set)

knop_wis_hist = tk.Button(pagina6, text="Wis Geschiedenis", command=wis_historie)
knop_wis_hist.pack(pady=5)


# ==================== MENUBALK ====================
menubalk = tk.Menu(venster)

menu_paginas = tk.Menu(menubalk, tearoff=0)
menu_paginas.add_command(label="Instellingen", command=toon_pagina1)
menu_paginas.add_command(label="Quiz", command=toon_pagina2)       
menu_paginas.add_command(label="Tekenen", command=toon_pagina3)    
menu_paginas.add_command(label="Grafieken", command=toon_pagina4)
menu_paginas.add_command(label="Memory Spel", command=toon_pagina5)
menu_paginas.add_command(label="Rekenmachine", command=toon_pagina6)
menubalk.add_cascade(label="Pagina's", menu=menu_paginas)
venster.config(menu=menubalk)

# Starten op pagina 1
pagina1.tkraise()

venster.mainloop()
