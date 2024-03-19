import tkinter as tk

CANVAS_WIDTH = 600     # largeur de la zone de dessin (nombre de pixels)
CANVAS_HEIGHT = 400    # hauteur de la zone de dessin (nombre de pixels)


racine = tk.Tk()  # racine de la fenetre graphique

canvas = tk.Canvas(racine, width=CANVAS_WIDTH, height=CANVAS_HEIGHT) # creation de la zone de dessin dans la fenetre graphique

# Code commenté : Sert à créer le schéma horizontal du début de l'exercice.
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
canvas.create_line((x0, y), (x1, y))                                       # creation d'une ligne a partir des points p1(x0,y) et p2(x1,y)
canvas.create_oval((x0 - 50, y + 50), (x0 + 50, y - 50))                   # creation d'un cercle (inclus dans un rectangle imaginaire dont le pt en haut a gauche est p1(x0 - 50, y + 50) et le pt en bas a droite est p2(x0 + 50, y - 50))
canvas.create_oval((x1 - 50, y + 50), (x1 + 50, y - 50))
canvas.create_oval(((x0 + x1) / 2 - 50, y + 50), ((x0 + x1) / 2 + 50, y - 50))


# y0 = 100
# y1 = CANVAS_HEIGHT - 100
# x = CANVAS_WIDTH / 2
# canvas.create_line((, ), (, ))
# canvas.create_oval((x - 50, y0 + 50), (x + 50, y0 - 50))
# canvas.create_oval((, ), (, ))
# canvas.create_oval((x - 50, (y1 + y0) / 2 + 50), (x + 50, (y1 + y0) / 2 - 50))

# Fin de votre code

canvas.grid(row=0, column=0)  #position du canvas dans la fenetre graphique
racine.mainloop()
