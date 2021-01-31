# coding: utf-8
import math
import random
import matplotlib.pyplot as plt
import numpy as np


class algGenetico():
	def __init__(self,tam_pop,n,max,min,mut_tax,cru_tax):
		self.tam_pop = tam_pop
		self.n = n
		self.max = max
		self.min = min
		self.mut_tax = mut_tax
		self.cru_tax = cru_tax
		self.gerarPopulacao()

	def gerarPopulacao(self):
		#cria lista que vai armazenar as strings de bits

		self.populacao = []
		self.populacao.clear()
		for i in range(0,self.tam_pop):
		    sublist = []
		    for j in range(0,self.n):
		        sublist.append('')
		    self.populacao.append(sublist)
		#prenche a lista criada com valores aleatorios
		for i in range(0,self.tam_pop):
			for j in range (0,self.n):
				self.populacao[i][j] = random.uniform(self.min, self.max)
		#print(self.populacao)


	def fitnessCalc(self):
		self.fitness = [0]*self.tam_pop
		self.trueFitness = [0]*self.tam_pop
		aux=[0]*self.n
		for i in range (0,self.tam_pop):
			self.trueFitness[i]=self.func_obj(self.populacao[i])
			self.fitness[i]=1/self.trueFitness[i]

		self.prepRoleta()
		#print(self.fitness)

	def func_obj(self,x):
		t = 0
		for i in range(0, self.n):
			t += x[i]*x[i]
		f_exp = -0.2 * math.sqrt((1*t)/self.n)
		t = 0
		for i in range(0, self.n):
			t += math.cos(2 * math.pi * x[i])
		s_exp = 1/self.n * t
		f = -20 * math.exp(f_exp) - math.exp(s_exp) + 20 + math.exp(1)
		return f

	def prepRoleta(self):
		somaFitness=0

		for i in range(self.tam_pop):
			somaFitness+=self.fitness[i]

		for i in range(self.tam_pop):
			self.fitness[i]/=somaFitness


	def roleta(self):
		pais=[0]*2
		paisIndex=[0]*2
		for i  in range(0,2):
			rndvalue=random.uniform(0,1)
			soma=0
			for j in range(self.tam_pop):
				if(soma<rndvalue):
					soma+=self.fitness[j]
				else:
					break
			pais[i]=self.populacao[j]
			paisIndex[i]=j;

		return pais,paisIndex



	def cruzamento(self,pais):
		n=self.n;

		aux=[0]*n
		filhos = [[0 for x in range(n)] for y in range(2)]
		a=0.5
		if (random.randint(0,99)<self.cru_tax):
			for i in range(0,2):
				for j in range(n):
					aux[j]=abs(pais[0][j]-pais[1][j])
					u=random.uniform(min(pais[0][j],pais[1][j])-a*aux[j],max(pais[0][j],pais[1][j])+a*aux[j])
					if(u>self.max):
						u=self.max
					elif(u<self.min):
						u=self.min
					filhos[i][j]=u
		else:
			for i in range(0,2):
				for j in range(0,n):
					filhos[i][j] = pais[i][j]

		return filhos

	def cruzamento2(self,pais,index):
		n=self.n;

		diff=[0]*n
		filhos = [[0 for x in range(n)] for y in range(2)]
		a=0.75
		b=0.25
		if(self.fitness[index[0]]<self.fitness[index[1]]):
			aux=pais[0]
			pais[0]=pais[1]
			pais[1]=aux
		if (random.randint(0,99)<self.cru_tax):
			for i in range(0,2):
				for j in range(n):
					diff[j]=abs(pais[0][j]-pais[1][j])
					if pais[0][j]<=pais[1][j]:
						u=random.uniform(pais[0][j]-a*diff[j],pais[1][j]+b*diff[j])
					else:
						u=random.uniform(pais[1][j]-b*diff[j],pais[0][j]+a*diff[j])
					if(u>self.max):
						u=self.max
					elif(u<self.min):
						u=self.min
					filhos[i][j]=u
		else:
			for i in range(0,2):
				for j in range(0,n):
					filhos[i][j] = pais[i][j]

		return filhos


	def mutacao(self):
		aux=''

		for i in range (0,self.tam_pop):
				for j in range (0,self.n):
						if random.randint(0,99)<self.mut_tax:
							self.populacao[i][j] = random.uniform(self.min, self.max)








def valores():
	val1 = int(input("Numero de gerações: "))
	val2 = int(input("Tamanho da população(precisa ser par): "))
	val3 = int(input("Numero de valores no individuo : "))
	val4 = int(input("Intervalo max: "))
	val5 = int(input("Intervalo min: "))
	val6 = int(input("Numero de bits: "))
	val7 = int(input("Taxa de mutação: "))
	val8 = int(input("Taxa de cruzamento: "))
	return val1,val2,val3,val4,val5,val6,val7,val8



def main():
	parametrosParaTestes=[[1,60,26,25],[1,60,26,50],[1,60,26,100],[1,60,50,25],[1,60,50,50],[1,60,50,100],[1,60,100,25],[1,60,100,50],[1,60,100,100],
						  [1,80,26,25],[1,80,26,50],[1,80,26,100],[1,80,50,25],[1,80,50,50],[1,80,50,100],[1,80,100,25],[1,80,100,50],[1,80,100,100],
						  [1,100,26,25],[1,100,26,50],[1,100,26,100],[1,100,50,25],[1,100,50,50],[1,100,50,100],[1,100,100,25],[1,100,100,50],[1,100,100,100],
						  [5,60,26,25],[5,60,26,50],[5,60,26,100],[5,60,50,25],[5,60,50,50],[5,60,50,100],[5,60,100,25],[5,60,100,50],[5,60,100,100],
  						  [5,80,26,25],[5,80,26,50],[5,80,26,100],[5,80,50,25],[5,80,50,50],[5,80,50,100],[5,80,100,25],[5,80,100,50],[5,80,100,100],
  						  [5,100,26,25],[5,100,26,50],[5,100,26,100],[5,100,50,25],[5,100,50,50],[5,100,50,100],[5,100,100,25],[5,100,100,50],[5,100,100,100],
						  [10,60,26,25],[10,60,26,50],[10,60,26,100],[10,60,50,25],[10,60,50,50],[10,60,50,100],[10,60,100,25],[10,60,100,50],[10,60,100,100],
  						  [10,80,26,25],[10,80,26,50],[10,80,26,100],[10,80,50,25],[10,80,50,50],[10,80,50,100],[10,80,100,25],[10,80,100,50],[10,80,100,100],
  						  [10,100,26,25],[10,100,26,50],[10,100,26,100],[10,100,50,25],[10,100,50,50],[10,100,50,100],[10,100,100,25],[10,100,100,50],[10,100,100,100]]

	#caracterustucas por individuo na populacao
	n=2
	#intervalo max
	n_max=10
	#intervalo max
	n_min=-10
	#taxa de mutacao


	#verifica se o usuario quer setar os proprios valores ou rodar em preset
	#val = int(input("1.Preset \n2.Setar valores proprios\n"))
	#if val == 2:
	#	n_gerações,n_populacao,n,n_max,n_min,n_mutax,n_crutax=valores()


	#instancia classe algGenetico


	#quantas vezes vai ser necessario rodar para gerar uma nova populacao



	#caclula o fitnes da geração inicial
	#rodar até o numero definido de gerações

	file = open( 'Resultado_Testes.txt', 'w' )
	for t in range(0,81):
		print(t)
		n_mutax=parametrosParaTestes[t][0]
		n_crutax=parametrosParaTestes[t][1]
		n_populacao=parametrosParaTestes[t][2]
		n_gerações=parametrosParaTestes[t][3]

		#file.write("Parametros do teste " + repr(t)+ " mutação " +repr(n_mutax) +" cruzamento "+ repr(n_crutax) +" população "+ repr(n_populacao)+" geração "+repr(n_gerações)+"\n")





		max_r = int(n_populacao/2)

		for l in range(0,20):
			AG = algGenetico(n_populacao,n,n_max,n_min,n_mutax,n_crutax)
			for i in range (0,n_gerações):

				novaPopulacao = []
				#criar uma nova geração
				AG.fitnessCalc()
				for j in range(0,max_r):

					#seleciona 2 indiduos da geração atual para serem pais de 2 individuos da proxima geração
					#pais = AG.roleta()
					pais,index = AG.roleta()
					#realiza o cruzamento dos pais para gerar 2 novos filhos para a nova geração
					#filhos=AG.cruzamento(pais)
					filhos=AG.cruzamento2(pais,index)
					novaPopulacao.append(filhos[0])
					novaPopulacao.append(filhos[1])

				#seleciona melhor elemento da geracao anterior
				#print(AG.fitness)
				#print(AG.tempFitness)
				elite =AG.populacao[AG.fitness.index(max(AG.fitness))]
				#print("heehxd" + str(elite))
				#setar a nova população no lugar da anterior
				AG.populacao = novaPopulacao
				#realizar mutação

				muta = AG.mutacao()

				#seta o elite da geracao anterior no lugar de um individuo aleatorio da geracao atual

				AG.populacao[random.randint(0,n_populacao-1)] = elite

				#calcula o fitness da nova geração

			media=0
			for k in range(n_populacao):
				media+=AG.trueFitness[k]
			melhorFitness= min(AG.trueFitness)
			mediaFitness=media/n_populacao
			file.write(repr(t)+ " " + repr(l)+" "+repr(i)+" "+repr(melhorFitness)+" "+ repr(mediaFitness)+"\n")



	file.close()

if __name__ == '__main__':
	main()
