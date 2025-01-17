# Addresse.py
#debut de code et presentation de l'application
 
print("""salut cher utilisateur vous etes
      le bienvenue sur notre application """)
while True:
    presentation=0
    try:
        presentation = int(input("""A present le choix est à vous :
                                tapez 1 si vous voulez lire la documentation
                                sinon 2 pour continue \n"""))
     # boucle cas d'erreurs   
    except:
        print("")
    if presentation== 1: 
        print("""MERCIE pour votre choix : Cette application est mise en place 
              pour vous pemettre de trouver et de 
              classifier les different Adresse IP(@IP)""")
        break
    elif presentation == 2:
        print("MERCIE pour votre choix : continuant ")
        break
    else:
        print(" ERROR de saisie :Verifier votre valeur, Faites un choix entre 1 ou 2 ")
#boucle et cas d'erreur:


    #initiation de octets 
    # verification de chaque octets   
    
    ## boucle 1 verification du premier octet ##       
while True:
       try:
          ip1=int(input("etant donnée que @ip est compose de quatre octet, entrez votre premier octet:  "))
          if ip1==127:
                  print ("OUPS cet octet n'est pas utilisable  ")  
          if ip1<0:
             print(" ERROR 1005") # presenntation à l'écran puis rebouclage  
              
          elif ip1>255:
                print(" ERROR 1005")       
          else:
            print("SUIT")
            break
       except ValueError:  # presentation propre de l'erreur type "ValueError"
               print("ERROR: Entrez un entier, la valeur entrer est ivalide ") 
               
   ## boucle 2 verification du premier octet ##              
while True:
        try:                   
            ip2=int(input("entrez votre deuxieme octet:"))
            if ip2==127:
                  print ("OUPS cet octet n'est pas utilisable  ")  
            if ip2<0:
                print("ERROR 4001 ")
            
            elif ip2>255:
                    print("ERROR 4001")       
            else:
                print("SUIT")
                break
        except ValueError:
               print("ERROR: Entrez un entier, la valeur entrer est ivalide ") 
   ## boucle 3 verification du premier octet ##              
while True :
           try:          
                ip3=int(input("entrez votre troisieme octet: "))   
                if ip3==127:
                  print ("OUPS cet octet n'est pas utilisable  ")  
                if ip3<0:
                    print(" ERROR 5520 ")
                     
                elif ip3>255:
                    print(" ERROR 5520")       
                else:
                    print("SUIT")
                    break
           except ValueError:
               print("ERROR: Entrez un entier, la valeur entrer est ivalide ")     
               
   ## boucle 4 verification du premier octet ##       
while True:
            try:        
                ip4=int(input("Entrez votre quatrieme octet: "))   
                if ip4==127:
                  print ("OUPS cet octet n'est pas utilisable  ")        
                if ip4<0:
                    print("ERROR 1050")
                     
                elif ip4>255:
                    print("ERROR 1050")       
                else:
                    print("  ") 
                    break
            except ValueError:
               print("ERROR: Entrez un entier, la valeur entrer est ivalide ")   

       # initialisation de la liste
ip_liste= []  
       # Ajout de chaque octet dans la liste  
ip_liste.append(ip1)
ip_liste.append(ip2)
ip_liste.append(ip3)
ip_liste.append(ip4)

if len(ip_liste)!= 4: ## Vérification de la longueur de la liste 
    #ce qui est unitile dans ce cas, car le nombre d'octet a été bloqué à 4 au début##
    print('ERROR FULL')

# presentation de chaque addresse et sa classe 

if 1<= ip1 <=126:  
    print("ADDRESSE VALIDE")
    print("-----------------------------")
    print ((ip_liste))
    print("-----------------------------")
    print("CLASSE A")
    print("@Masque: 255.0.0.0")
if 128<= ip1<=191:
    print("ADDRESSE VALIDE")
    print("-----------------------------")
    print ((ip_liste))
    print("-----------------------------")
    print("CLASSE B")
    print("@Masque: 255.255.0.0")
elif  192<= ip1<=223:  
    print("ADDRESSE VALIDE")
    print("-----------------------------")
    print ((ip_liste))
    print("-----------------------------")
    print("CLASSE C")
    print("@Masque: 255.255.255.0")
elif 224<= ip1<=239:   
    print("ADDRESSE VALIDE")
    print("-----------------------------")
    print ((ip_liste))
    print("-----------------------------")
    print("CLASSE D")     
if 240<=ip1<=255 :
    print("ADDRESSE VALIDE")
    print("-----------------------------")
    print ((ip_liste))
    print("-----------------------------")
    print("CLASSE E")    
if ip1==0: 
    print("ADDRESSE INVALIDE")
    print("-----------------------------")
    print ((ip_liste))
    print("-----------------------------")
    print("CLASSE ? ")
    # presentation cas unique de brodcast        
if ip4==255: 
    print("-----------------------------")
    print("ADDRESSE BRODCAST")         

# fin programme
                                    
           
               
                
