# -*- coding: utf-8 -*-
"""TRABALHO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CkxCixsbgZ1l3bko4WoFGTVIiEWrQEgk
"""



print("Esse é um quiz sobre conhecimentos gerais","\n","Seja bem vindo")
Player=input("Escreva seu nome:"  )
print("")#foi usado para pular uma linha.
pontos=0#aqui definimos a variável pontos.
print(Player," ao jogar você precisa de no mínimo 12.5 pontos para avançar para a próxima rodada","\n","ou seja em cada rodada você precisa acertar no mínimo 2 perguntas","\n"," Cada rodada vale 25 pontos e possui 4 perguntas a soma total de pontos caso acerte todas e igual a 100 pontos")
print("")#1RODADA
print("Início 1 rodada (⁠＾⁠∇⁠＾⁠)⁠ﾉ⁠♪Boa sorte")
while pontos == 0<12.5:#o bloco de 4 perguntas se repete enquanto a pessoa não acertar no mínimo 2 respostas.
 print('')# Acima iniciamos o laço de repetição, para sair dele tem que acertar 2 perguntas, e repetido a cada rodada.
 print("1\Quem foi Arquimedes?","\n","A\matemático" ,"B\professor de natação","\n","C\programador" ,"D\Cozinheiro")#\n e usado para não ficar tudo na mesma linha.
 Resposta=input("resposta:")
 if Resposta == "A" or Resposta == "a":# or foi utilizado para se aceitar a resposta tanto em letra maiúscula e minúscula.
   print("resposta correta")# if(se) a resposta estiver correta a variável pontos recebe +6.25 pontos.
   pontos=pontos+6.25
 else:# else(senao) não recebe nada(⁠゜⁠o⁠゜⁠;.
   print("resposta errada")
 print("")
 print("2\Ada Lovelance foi a primeira:","\n","A\programadora","B\matematica","\n","C\Fisica","D\professora")
 Resposta2=input("resposta:")
 if Resposta2 == "A" or Resposta2 == "a":
   print("resposta correta")
   pontos=pontos+6.25
 else:
   print("resposta errada ಠ⁠ ⁠೧⁠ ⁠ಠ")
 print("")
 print("3\Quais o menor e o maior países do mundo?","\n","A\Vaticano e Russia","B)Nauru e China","\n","C)Mônaco e Canadá","D)Índia e Brasil")
 Resposta3=input("resposta:")
 if Resposta3 == "A" or Resposta3 == "a":
  print("resposta correta｡⁠.ﾟ⁠+⁠ ⁠⟵⁠(⁠｡⁠･⁠ω⁠･⁠)")
  pontos=pontos+6.25
 else:
  print("resposta errada")
 print("")
 print("4)Qual o maior animal terrestre?","\n","A)Baleia Azul"," B)Dinossauro","\n","C)Elefante Africano"," D)Tubarão Branco")
 Resposta4=input("resposta:")
 if Resposta4 == "C" or Resposta4 == "c":
  print("resposta correta ←⁠(⁠>⁠▽⁠<⁠)⁠ﾉ")
  pontos=pontos+6.25
 else:
  print("resposta errada•́⁠ ⁠ ⁠‿⁠ ⁠,⁠•̀")
 print('')
 print("Fim da 1 rodada",Player,pontos,"pontos")
print("")#FIM 1 RODADA/ INÍCIO 2 RODADA.
pontos2=0
print("Início 2 rodada ლ⁠(⁠^⁠o⁠^⁠ლ⁠) vá na fé você consegue!")
while pontos2==0<12.5:
 print('')
 print("5)Em que oceano fica Madagascar?","\n","A)Oceano índico","B)Oceano Pacífico","\n","C)Oceano Ártico"," D)Oceano Antártico")
 Resposta5=input("resposta:")
 if Resposta5 == "A" or Resposta5 == "a":
   print("resposta certa♪⁠～⁠(⁠´⁠ε⁠｀⁠ ⁠)")
   pontos2=pontos2+6.25
 else:
  print("resposta errada")
 print("")
 print("6)Complete o provérbio'A cavalo dado ...:'","\n","A)Sai caro","B)bonito lhe parece","\n","C)não se olha os dentes"," D) não se olha o rabo")
 Resposta6=input("Resposta:")
 if Resposta6 == "C" or Resposta6 == "c":
   print("resposta correta")
   pontos2=pontos2+6.25
 else:
   print('resposta errada')
 print('')
 print("7)Quem foi discípulo de Sócrates?","\n","A)Platão","B)Descartes","\n","C)Heráclito"," D)Parmênides")
 Resposta7=input("resposta:")
 if Resposta7 == "A" or Resposta7 == "a":
   print("resposta correta")
   pontos2=pontos2+6.25
 else:
   print("resposta errada")
 print("")
 print("8)Quantos dias tem um ano bissexto?","\n","A)366","B)365","\n","C)345","D)367")
 Resposta8=input("resposta:")
 if Resposta8 == "A" or Resposta8 == "a":
   print("resposta correta")
   pontos2=pontos2+6.25
 else:
   print("resposta errada")
 print("pontos da 2 rodada",pontos2)
 print("")
 print(Player,"Seus pontos até aqui são iguais a:",pontos+pontos2)
print("")#FIM 2 RODADA/ INÍCIO 3 RODADA.
pontos3=0
print("Início 3 rodada good Lucky(⁠☞ﾟ⁠∀ﾟ⁠)⁠☞")
print("")
while pontos3==0<12.5:
 print("9)O Estado Novo foi o período da ditadura varguista em que toda oposição foi silenciada e perseguida por agentes do governo.","\n","Em maio de 1938, um grupo que apoiou o golpe do Estado Novo decidiu atacar o palácio presidencial.","\n","Esse ataque foi realizado pelos:","\n","a) comunistas","b) liberais","c) tenentistas","d) integralistas","e) nenhuma das alternativas")
 Resposta9=input("resposta:")
 if Resposta9=="d" or Resposta9=="D":
   print("resposta certa")
   pontos3=pontos3+6.25
 else:
   print("resposta errada")
 print("")
 print("10)Quais são os três maiores países do mundo?","\n","a)Rússia,Canadá e China","b)Brasil,Japão e EUA","c)Índia ,China e Brasil","d)África, Argentina e Canadá.")
 Resposta10=input("resposta:")
 if Resposta10=="a" or Resposta10=="A":
   print("você acertou")
   pontos3=pontos3+6.25
 else:
   print("Você errou")
 print("")
 print("11)Qual o ponto de ebulição da água?","\n","a)100°","b)373,2°K","c)212°F","d)Todas as opcões")
 Resposta11=input("resposta:")
 if Resposta11=="d" or Resposta11=="D":
   print("Voce acertou")
   pontos3=pontos3+6.25
 else:
   print("Você errou")
 print("")
 print("12)A mãe da Karen tem cinco filhas: Dadá, Dedé, Didi, Dodó e …?")
 Resposta12=input("resposta:")
 if Resposta12=="karen" or Resposta12=="Karen":
   print("Voce acertou")
   pontos3=pontos3+6.25
 else:
   print("Você errou")
print("Fim 3 rodada seus pontos são iguais a:",pontos3)
print("")
print("Seus pontos até aqui são iguais a:",pontos+pontos2+pontos3)
print("")#4RODADA
print("Início 4 rodada (⁠๑⁠•⁠﹏⁠•⁠) Você chegou a última rodada boa sorte")
print('')
pontos4=0
while pontos4==0<12.5:
 print("13)Em uma sala quadrada, temos uma calopsita em cada canto. Cada calopsita vê outras três. Quantas calopsitas há no total?")
 Resposta13=input("resposta:")
 if Resposta13=="4" or Resposta13=="quatro" or Resposta13=="Quatro":
   print("Voce acertou")
   pontos4=pontos4+6.25
 else:
   print("Você errou")
 print("")
 print("14)O valor da pressão atmosférica é:")
 print("a) 1atm","b) 3atm","c) não existe valor para a pressão atmosférica")
 Resposta14=input("resposta:")
 if Resposta14=="a" or Resposta14=="A":
   print("resposta certa")
   pontos4=pontos4+6.25
 else:
   print("resposta errada")
 print("")
 print("15)Qual foi a primeira rainha da Inglaterra ")
 print("a) Vitória","b) Elizabeth I","c) Isabel I","d) Elizabeth II")
 Resposta15=input("resposta:")
 if Resposta15=="c" or Resposta15=="C":
   print("você acertou")
   pontos4=pontos4+6.25
 else:
   print("Você errou")
 print("")
 print("16) Qual o animal possui o maior pescoço乁⁠[⁠ᓀ ?")
 print ("a)elefante","b)girafa","c)Cameroceras, a lula gigante","d) nenhuma das alternativas")
 Resposta16=input("resposta:")
 if Resposta16=="b" or Resposta16=="B":
   print("Voce acertou")
   pontos4=pontos4+6.25
 else:
   print("Você errou")
print("Fim da 4 rodada,seus pontos:",pontos4)
print("")#Fim 4 RODADA/ Soma final de pontos das rodadas 1,2,3,4.
print(Player,"<⁠(⁠￣⁠︶⁠￣⁠)⁠>parabéns você chegou no final. O total de pontos são:",pontos+pontos2+pontos3+pontos4)