# -*- coding: utf-8 -*- 

class client:
    def __init__(self, nom, date_naiss, abonnes, facture):
        self.nom = nom
        self.date_naiss = date_naiss
        self.abonnes = abonnes
        #self.facture = facture[abonnes]   
        
        
    
class cdr:
    def __init__(self, filename : list):
        self.filename = filename
        self.liste = [] 
        self.resultat = [] 
    def _open(self):
        contenu = [] 
        for i in range(len(self.filename)):  
            file = open(self.filename[i], "r") 
            contenu = contenu + file.readlines()
            file.close()
        for ligne in contenu:
            self.liste.append(ligne.strip())
        self.pile_dict()
        return self.resultat
      
        
    def pile_dict(self):
        a = []
        b = ["identifiant de l'appel", 'type call', ' date et heure','appelant', 'appelé', 'durée', 'taxe', 'total volume']
        for i in self.liste:
            
            a = i.split('|')
            #print(a)
            self.resultat.append(dict(zip(b, a)))
        
            
class facture:
    def __init__(self,liste_dict):
        self.liste_dict = liste_dict
        self.prix = {} 
    
    def definition(self):
        for i in self.liste_dict: 
            type_call = float(i['type call']) 
            num2 = i['appelé'] 
            if i['durée'] != '': 
            	dure = float(i['durée']) 
            else:
            	dure = 0 
            total_vol = float(i['total volume'])
            taxe = float(i['taxe'])
            prix = 0
            if type_call == 0: 
                if num2[0:5] == '24381' or num2[0:5] == '24382':
                    prix += 0.025*dure/60
                else:
                    prix += 0.05*dure/60
            elif type_call == 1:
                if num2[0:5] == '24381' or num2[0:5] == '24382':
                    prix  += 0.001  
                else:
                    prix += 0.002  
            else:
                prix += total_vol*0.03 
            if taxe == 1:  
                prix = prix + prix *10/100
            elif taxe == 2: 
                prix = prix + prix *16/100 
            if i['appelant'] in list(self.prix.keys()) :  
                self.prix[i['appelant']] += prix  
            else:
                self.prix[i['appelant']] = prix  
        return self.prix  
                 
                       
class statistique:
    def __init__(self, liste_dict):
        self.liste_dict = liste_dict
        
        self.statistique = {} 
        self.stat_dict = [] 
    def stat(self):
        for i in self.liste_dict: 
            
            nbr_appel = 0 
            nbr_sms = 0
            giga = 0 
            dure_appel = 0
            
            type_call = float(i['type call'])  
            
            if i['durée'] != '':
            	dure = float(i['durée']) 
            else:
            	dure = 0 
            total_vol = float(i['total volume']) 
            
            if type_call == 0: 
                nbr_appel += 1 
                dure_appel += dure 
                
            elif type_call == 1: 
                nbr_sms += 1
            else:
                giga += total_vol 
                
            
            if i['appelant'] in list(self.statistique.keys()) : 
                un = self.statistique[i['appelant']][0] + nbr_appel 
                deux = self.statistique[i['appelant']][1] + dure_appel
                trois = self.statistique[i['appelant']][2] + nbr_sms
                quatre = self.statistique[i['appelant']][3] + giga
                cinq = i['appelant'] 
                self.statistique[i['appelant']] = [un, deux, trois, quatre, cinq]
            else: 
                un =  nbr_appel
                deux =  dure_appel
                trois =  nbr_sms
                quatre =  giga
                cinq = i['appelant']
                self.statistique[i['appelant']] = [un, deux, trois, quatre, cinq]
        self.have_stat() 
        return self.stat_dict 
    def have_stat(self):
        a = ["Nombre d'appels", "Durée d'appel", "Nombre de sms", "Nombre de Gigabytes", "abonnés"]
        for i in self.statistique.keys(): 
            self.stat_dict.append(dict(zip(a, self.statistique[i]))) 
        


# Tests 

cdr = cdr(['cdr.txt', 'cdr2.txt'])
list_dict = cdr._open()
print (list_dict)

#facture = facture(list_dict)
#prix = facture.definition()
#print(prix)

#stat = statistique(list_dict)
#nos_stat = stat.stat()
#print(nos_stat)

#polytechnique = client('POLYTECHNIQUE', '20/01/2004', '243818140120', prix)
#print(polytechnique.facture)

#polytechnique = client('POLYTECHNIQUE', '20/01/2004', '243818140560', prix)
#print("La facture pour le client POLYTECHNIQUE est :{}".format(polytechnique.facture))


            
            


    
    
        
            

        
                
            
        
        
    
    

