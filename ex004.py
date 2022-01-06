#Faça um programa que leia algo e diga o seu tipo primitivo e todos as informações sobre ele.

termo = input('Escreva aqui qualquer coisa: ')
print('O tipo do termo é: ', type(termo))
print('O termo é espaços? ', termo.isspace())
print('O termo é alfabético? ', termo.isalpha())
print('O termo é numérico?', termo.isnumeric())
print('O termo é uma mistura de letras e números? ', termo.isalnum())
print('O termo está todo maiúsculo? ', termo.isupper())
print('O termo está todo em minúsculo? ', termo.islower())
print('O termo tem capitalizações? ', termo.istitle())

