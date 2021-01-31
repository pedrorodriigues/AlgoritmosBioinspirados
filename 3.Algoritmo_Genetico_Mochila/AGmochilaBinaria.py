# coding: utf-8
import math
import random
from operator import itemgetter


class algGenetico():

	def __init__(self,tam_pop,mut_tax,cru_tax):
		self.tam_pop = tam_pop
		self.n = 0
		self.mut_tax = mut_tax
		self.cru_tax = cru_tax
		self.baseValue=[]
		self.capacidade=0
		self.fitness=[0]*tam_pop
		self.readFile()

	def readFile(self):
		filename=[]
		filename.append("valor.txt")
		filename.append("peso.txt")
		count=0
		for i in range(0,2):
			with open(filename[i], 'r') as file:
				lines = [int(line) for line in file]
			self.baseValue.append(lines)
		with open(filename[0], 'r') as file:
			self.n = sum(1 for line in file)

		with open("capacidade.txt", 'r') as file:
			self.capacidade = [int(line) for line in file]
		self.baseValue=list(zip(self.baseValue[0],self.baseValue[1]))
		self.capacidade=self.capacidade[0]
		#print(type(self.capacidade[0]))
		self.gerarPopulacao()




	def gerarPopulacao(self):
		#cria lista que vai armazenar as strings de bits
		self.populacao = []
		for i in range(0,self.tam_pop):
			sublist = []
			for j in range(0,self.n):
				sublist.append(random.randint(0,1))
			if all(x == 0  for x in sublist):
				sublist[random.randint(0,self.n-1)]=1
			self.populacao.append(sublist)

		#print(self.populacao)

	def fitnessCalc(self):
		for i,individuo in enumerate(self.populacao):
			self.fitness[i]=[tuple(self.baseValue[j]) for j,objeto in enumerate(individuo) if objeto]
			self.fitness[i]=[sum(x) for x in zip(*self.fitness[i])]
			if not self.fitness[i]:
				self.fitness[i]=[0,0]

			if(self.fitness[i]!=[] and self.fitness[i][1]>self.capacidade):
				#print(self.fitness[i][0])
				self.fitness[i][0]*=(1-(self.fitness[i][1]-self.capacidade)/self.capacidade)
	def torneio(self):

		best=[0]*2
		n1=random.randint(0,self.tam_pop-1)
		n2=random.randint(0,self.tam_pop-1)
		for i in range(0,2):
			if self.fitness[n1][0]> self.fitness[n2][0]:
				best[i] = self.populacao[n1]
				bestn=n2
			else:
				best[i] = self.populacao[n2]
				bestn=n2
			while bestn == n1 or bestn == n2:
				n1=random.randint(0,self.tam_pop-1)
				n2=random.randint(0,self.tam_pop-1)

		return best

	def cruzamento(self,pais):
		corte = random.randint(1,self.n-2)

		#print(pais)
		#print(corte)
		if random.randint(0,99)<self.cru_tax:
			f1 = pais[0][:corte] + pais[1][corte:]
			f2 = pais[1][:corte] + pais[0][corte:]

		else:
			f1 = pais[0][:]
			f2 = pais[1][:]
		#print(f1,f2)
		return f1,f2

	#mutação por bit
	def mutacao(self):
		aux=''

		for i in range (0,self.tam_pop):
			for k in range (0,self.n):
				if random.randint(0,99)<self.mut_tax:
					if self.populacao[i][k]==1:
						self.populacao[i][k]=0
					else:
						self.populacao[i][k]=1
	def listaValida(self):
		validos=[]
		for i,tupla in enumerate(self.fitness):
			if(tupla[1]<=self.capacidade):
				validos.append(tupla)
		return validos

	def selecionaMelhor(self):
		validos=self.listaValida()
		if validos:
			return max(validos,key=itemgetter(0))
		else:
			return max(self.fitness,key=itemgetter(0))



	def elite(self):
		candidato = self.selecionaMelhor()
		elite =self.populacao[self.fitness.index(candidato)]
		index=random.randint(0,self.tam_pop-1)
		self.populacao[index] = elite

	def estatisticas(self):
		fitnessValidos=self.listaValida()
		media=sum(fitness[0] for fitness in fitnessValidos)
		if len(fitnessValidos)!=0:
			media/=len(fitnessValidos)
		else:
			media=0
		print(fitnessValidos)
		print(media)



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

	#numero de gerações
	n_gerações=25
	#tamanho da populacao
	n_populacao=26
	#taxa de mutacao
	n_mutax=10
	#taxa de cruzamento
	n_crutax=100
	melhor=99
	execuções=20
	file = open( 'Resultado_Testes_Execuções2.txt', 'w' )
	for t in range(0,81):
		n_mutax=parametrosParaTestes[t][0]
		n_crutax=parametrosParaTestes[t][1]
		n_populacao=parametrosParaTestes[t][2]
		n_gerações=parametrosParaTestes[t][3]
		max_r = int(n_populacao/2)
		print(n_mutax,n_crutax,n_populacao,n_gerações)

		for m in range(0,execuções):

			AG = algGenetico(n_populacao,n_mutax,n_crutax)
			for i in range (0,n_gerações):
				AG.fitnessCalc()
				novaPopulacao = []
				for j in range(0,max_r):
					#seleciona 2 indiduos da geração atual para serem pais de 2 individuos da proxima geração
					pais = AG.torneio()
					#realiza o cruzamento dos pais para gerar 2 novos filhos para a nova geração
					filhos=AG.cruzamento(pais)
					novaPopulacao.append(filhos[0])
					novaPopulacao.append(filhos[1])
				AG.elite()


				AG.populacao = novaPopulacao

				muta = AG.mutacao()
			melhor=AG.selecionaMelhor()
			file.write(repr(t)+ "," + repr(m)+","+ repr(melhor[0])+","+repr(melhor[1])+"\n")




	#print(melhor)
	#print(mediaexec/20)
if __name__ == '__main__':
	main()
