from genericpath import exists
from os import mkdir
from PIL import Image

img2 = Image.open("images_bot/emote_stuff/blanc_original_64.png")


def ab(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/ability_dobler.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def bdu(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/bombDamage_Reduction.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def sbpu(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/bombDistance_Up.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def cbk(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/ComeBack.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def hnt(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/DeathMarking.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def lde(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/EndAllUp.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def rsp(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/Exorcist.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def rsu(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/HumanMove_Up.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")




def iru(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/InkRecovery_Up.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def qsj(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/JumpTime_Save.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def ism(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/MainInk_Save.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def mpu(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/MainPowerUp.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def tnty(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/MinorityUp.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def os(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/ObjectEffect_Up.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def ir(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/OpInkEffect_Reduction.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def ss(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/RespawnSpecialGauge_Save.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def qr(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/RespawnTime_Save.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def dr(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/SomersaultLanding.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def scu(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/SpecialIncrease_Up.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def spu(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/SpecialTime_Up.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def ssu(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/SquidMove_Up.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def ns(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/SquidMoveSpatter_Reduction.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def og(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/StartAllUp.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def iss(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/SubInk_Save.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def sj(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/SuperJumpSign_Hide.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                p=img.getpixel((i,j))

                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                p=img.getpixel((i,j))
                
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def thi(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/ThermalInk.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def uk(position,img = img2) :
    img = Image.open("images_bot/emote_stuff/Unknown.png")
    
    colonne,ligne = img.size
    
    if position == 1 :
        for i in range(colonne):
            for j in range(ligne):
            
                p=img.getpixel((i,j))
                img2.putpixel((i,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 2 :
        for i in range(colonne):
            for j in range(ligne):

                p=img.getpixel((i,j))
                img2.putpixel((i+64,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 3 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    elif position == 4 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 5 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 6 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 7 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 8 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+64),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 9 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 10 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+64,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 11 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+128,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")

    elif position == 12 :
        for i in range(colonne):
            for j in range(ligne):
                
                p=img.getpixel((i,j))
                img2.putpixel((i+192,j+128),(p[0],p[1],p[2]))
        img2.save("images_bot/emote_stuff/blanc_resultat.png")



def clear() :
    img = Image.open("images_bot/emote_stuff/blanc_resultat.png")

    colonne,ligne = img.size

    
    for i in range(colonne):
        for j in range(ligne):
            
            p=img.getpixel((i,j))
            img2.putpixel((i,j),(255,255,255))
    img2.save("images_bot/emote_stuff/blanc_resultat.png")
    
    
from csv import *

def addincsv(url_file,objet,newline =True, delimiter =  None):
    csv = open(url_file,'a',encoding='utf-8')
    if newline:
        csv.write((str(objet)+'\n'))
    else:
        csv.write(str(objet))
        csv.write(str(delimiter))
    csv.close()

def save(id,nom_stuff) :
    img = Image.open("images_bot/emote_stuff/blanc_resultat.png")
            
    img.save(f"stuffs/{id}/{nom_stuff}.png")

    
    
    

#clear()
