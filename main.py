#!/usr/bin/python3

dic = {'Name': 'Turtle', 'Age': 7}

print ("Nome : {: >14}".format(dic.get('Name', "Never")))
print ("Idade : {: >8}".format(dic.get('Age')))
print ("Escolaridade : {}".format(dic.get('Education', "Never")))