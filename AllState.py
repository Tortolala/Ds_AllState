import pandas as pd
import numpy as np
from __future__ import division
import matplotlib.pyplot as plt
import seaborn as sns
​csv = pd.read_csv('allstate.csv')

csv['shopping_pt'].head(100)
​
csv.describe()
​
csv[(csv.shopping_pt == 1) and (csv.record_type==1)].sum()
csv[csv.record_type==1].count()
​
bystate=csv.groupby("state")
bystate.shopping_pt[bystate.record_type==1]
bystate.shopping_pt
bystate.shopping_pt.min()
bystate=csv[csv.record_type==1].groupby("state")
​
​
# 7.¿Cuántas cotizaciones, previo la compra, realizan los consumidores del estado de Florida?
bystate=csv[csv.record_type==1].groupby("state")
bystate.shopping_pt.mean()
# 7.277439//
​
csv[csv.record_type==1].sum()
# 97009
​
​
#2. ¿Qué tan probable es que se compre un seguro después de la k-ésima cotización?
​
    
n = csv.shopping_pt[csv.shopping_pt == 5].count()
d = csv.shopping_pt[csv.shopping_pt == 1].count()
    
x = 100 - ((n/d) * 100)
    
y = "La probabilidad de compra en la cotizacion no. 5 o antes es de " + str(x)
    
print y
    
#La probabilidad de compra en la cotizacion no. 5 o antes es de 13.9873619973    
   
​
#6. ¿Que estado, en promedio, necesita menos cotizaciones?
​
bystate=csv[csv.record_type==1].groupby("state")
bystate.shopping_pt.mean().min()
​
#South Dakota con 6.1951219512195124
​
#9. ¿Del total de carros que porcentaje tiene menos de k años?
csv.car_age.describe()
​
​
​
for i in range (0, 86):
    
    n = csv.car_age[csv.car_age == i].count()
    d = csv.car_age.count()
    
    x = (n/d) * 100 
    
    y = "El porcentaje de carros con edad  " + str(i) + " es de " + str(x)
    
    print y
​
​
​
​
    n = csv.car_age[csv.car_age == 1].count() + csv.car_age[csv.car_age == 2].count() + csv.car_age[csv.car_age == 3].count() + csv.car_age[csv.car_age == 4].count()
    d = csv.car_age.count()
    
    x = (n/d) * 100
    
    print "El porcentaje de carro con menos de 5 años es de " + str(x) + "%"
    
    
    
    n = csv.car_age[csv.car_age < 5].count()
    d = csv.car_age.count()
    
    x = (n/d) * 100
    
    print "El porcentaje de carro con menos de 5 años es de " + str(x) + "%"
    
#4. ¿Que edad promedio tienen las personas dueñas de carros viejos y carros nuevos?    
    
edad = csv[['car_age','age_oldest']]  
e1 = edad[edad.car_age == edad.car_age.max()] 
edades = e1.age_oldest.mean()
print edades 
edad = csv[['car_age','age_youngest']]  
e1 = edad[edad.car_age == edad.car_age.max()] 
edades = e1.age_youngest.mean()
print edades 
​
edad = csv[['car_age','age_oldest']]  
e1 = edad[edad.car_age == edad.car_age.min()] 
edades= e1.age_oldest.mean()
print edades 
    
edad = csv[['car_age','age_youngest']]  
e1 = edad[edad.car_age == edad.car_age.min()] 
edades = e1.age_youngest.mean()
print edades
​
​
#Promedio de edad que tienen carros nuevos es de 38.66
#Promedio de edad que tinen carros viejos es de 64
​
​
​
#10. ¿Que edad necesita menos cotizaciones para comprar un seguro?
datos = csv[['record_type','shopping_pt','age_youngest']]
cotizacion = datos[datos.record_type == 1]
pequenacot = min(cotizacion.shopping_pt)
cantidad = cotizacion[cotizacion.shopping_pt == pequenacot]
m = cantidad.mode()
print 'Las personas que menos cotizaciones necsitan para comprar tienen edad de: ' + str(int(m.age_youngest))
# 75 años
    
    
​
#1. ¿Qué características tienen los grupos a los que se les cotiza los seguros más baratos?
​
​
​
​
​
​
# se escogio el valor 605 porque es el primer cuartil.
​
q = csv[(csv.cost<605)]
​
q.state.mode()
​
# Estado que más se repite = Florida
​
​
q.car_value.mode()
​
# El value que más se repite en los carros asegurados por debajo de  la media es E (menor valor)
​
q.risk_factor.mode()
​
#El factor de riesgo que más se repite es 1 (el menor)
​
sns.distplot(q.age_oldest)
​
sns.distplot(csv.age_oldest)
​
q.age_oldest.describe()
​
#La edad que más se repite en los seguros más baratos  por mucho es 75 años.¿Es relevante?
​
​
menor = q[(q.age_oldest<75)]
​
print menor
​
sns.distplot(menor.age_oldest)
​
menor.age_oldest.mode()
​
# De igual manera se repite que las personas mayores son más baratas de asegurar.
​
​
sns.distplot(q.group_size)
​
q.group_size.describe()
​
#comparar con toda la base de datos para ver si afecta el grupo
​
df1 =csv[(csv.group_size > 1)]
​
df1.cost.describe()
​
sns.distplot(df1.cost)
​
​
df2 =csv[(csv.group_size > 2)]
​
df2.cost.describe()
​
sns.distplot(df2.cost)
​
#El tamaño del grupo no afecta signigicativamente el costo
​
​
q.car_age.describe()
​
q.car_age.mode()
​
sns.distplot(q.car_age)
​
sns.distplot(csv.car_age)
​
​
q.homeowner.describe()
​
q.homeowner.mode()
​
​
#los carros de las personas que le cotizan con menos precio están entre 8 y 12 años son dueños de casas y la mayoría vive en Florida.    
​
​
​
# 5.¿Probabilidad de que alguien de edad k compre un seguro?
​
edad=35
info=csv[csv['age_oldest']==edad]
totales=sum(csv['record_type']==1)
compra=sum(info['record_type']==1)
probabilidad=((compra/1.0)/(totales/1.0))*100
df=csv[csv['age_youngest']==edad]
compra2=sum(df['record_type']==1)
probabilidad2=((compra2/1.0)/(totales/1.0))*100
final=probabilidad+probabilidad2
print("probabilidad de que alguien tenga  "+ str(edad) +" de años y compre un seguro es de "+ str(final)[0:4] + "%")
​
#probabilidad de que alguien de edad 35 años compre un seguro es de 3.27%
​
#pregunta 3
​
young=csv['age_youngest'].min()
youngin=csv[(csv.age_youngest==young)&(csv.record_type==1)]
youngin.car_age.mean()
youngin.group_size.mean()
print("basados en la edad del mas joven, carro de "+str(youngin.car_age.mean())[0:4]+" años tiene mas probabilidad de comprar un seguro")
print("basados en la edad del mas joven, el tamaño del grupo "+str(youngin.group_size.mean())[0:4]+" tiene mas probabilidad de comprar un seguro")
​
#basados en la edad del mas joven, carro de 9.43 años tiene mas probabilidad de comprar un seguro
#basados en la edad del mas joven, el tamaño del grupo 1.95 tiene mas probabilidad de comprar un seguro
​
​
​
#8
​
tmp = csv[(csv.record_type == 1)]
tmp.count()
tmp.time.mode()
​
#14:35
​
