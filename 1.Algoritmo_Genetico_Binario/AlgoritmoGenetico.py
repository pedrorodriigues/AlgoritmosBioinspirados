# coding: utf-8
import math
import random


class algGenetico():
	def __init__(self,tam_pop,n,max,min,n_bits,mut_tax,cru_tax):
		self.tam_pop = tam_pop
		self.n = n
		self.max = max
		self.min = min
		self.n_bits = n_bits
		self.mut_tax = mut_tax
		self.cru_tax = cru_tax
		self.gerarPopulacao()

	def gerarPopulacao(self):
		#cria lista que vai armazenar as strings de bits
		self.populacao = []
		for i in range(0,self.tam_pop):
		    sublist = []
		    for j in range(0,self.n):
		        sublist.append('')
		    self.populacao.append(sublist)
		#prenche a lista criada com valores aleatorios
		for i in range(0,self.tam_pop):
			for j in range (0,self.n):
				num = random.randint(0,(2**self.n_bits-1))
				self.populacao[i][j] = bin(num)[2:].zfill(self.n_bits)

	def fitnessCalc(self):
		#converte os valores para inteiro, para serem utilizados na transformacao
		min=int(self.min)
		max=int(self.max)
		bits = int(self.n_bits)
		self.fitness = [0]*self.tam_pop
		aux=[0]*self.n
		for i in range (0,self.tam_pop):
			for j in range(0,self.n):
				num = int(self.populacao[i][j],2);
				aux[j]=min+(((max-min)/(2**bits-1))*num)
			self.fitness[i]=self.func_obj(aux)


	def torneio(self):

		best=[0]*2
		n1=random.randint(0,self.tam_pop-1)
		n2=random.randint(0,self.tam_pop-1)
		for i in range(0,2):
			if self.fitness[n1]> self.fitness[n2]:
				best[i] = self.populacao[n2]
				bestn=n2
			else:
				best[i] = self.populacao[n1]
				bestn=n1
			while bestn == n1 or bestn == n2:
				n1=random.randint(0,self.tam_pop-1)
				n2=random.randint(0,self.tam_pop-1)

		return best

	def cruzamento(self,pais):
		corte = random.randint(1,self.n_bits-2)
		f1=[0]*self.n
		f2=[0]*self.n

		if random.randint(0,99)<self.cru_tax:
			for i in range(0,self.n):
				f1[i] = pais[0][i][:corte] + pais[1][i][corte:]
				f2[i] = pais[1][i][:corte] + pais[0][i][corte:]

		else:
			for i in range(0,self.n):
				f1[i] = pais[0][i][:]
				f2[i] = pais[1][i][:]

		return f1,f2

	#mutação por bit
	def mutacao(self):
		aux=''

		for i in range (0,self.tam_pop):
				for k in range (0,self.n):
					for j in range (0,self.n_bits):

						if random.randint(0,99)<self.mut_tax:
							if int(self.populacao[i][k][j],2)==1:
								aux = aux + "0"
							else:
								aux = aux + "1"
						else:
							aux=aux+self.populacao[i][k][j]
					self.populacao[i][k]=aux
					aux=''

	#mutação por individuo
	def mutacao2(self):
		aux=''

		for i in range (0,self.tam_pop):
			if random.randint(0,99)<self.mut_tax:

				for k in range (0,self.n):
					for j in range (0,self.n_bits):

						if int(self.populacao[i][k][j],2)==1:
							aux = aux + "0"
						else:
							aux = aux + "1"
					self.populacao[i][k]=aux
					aux=''



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
	#numero de gerações
	n_gerações=1000
	#tamanho da populacao
	n_populacao=86
	#elementos por individuo na populacao
	n=3
	#intervalo max
	n_max=10
	#intervalo max
	n_min=-10
	#numero de bits da representacao em binario
	n_bits=10
	#taxa de mutacao
	n_mutax=2
	#taxa de cruzamento
	n_crutax=90

	#verifica se o usuario quer setar os proprios valores ou rodar em preset
	val = int(input("1.Preset \n2.Setar valores proprios\n"))
	if val == 2:
		n_gerações,n_populacao,n,n_max,n_min,n_bits,n_mutax,n_crutax=valores()


	#instancia classe algGenetico
	AG = algGenetico(n_populacao,n,n_max,n_min,n_bits,n_mutax,n_crutax)

	#quantas vezes vai ser necessario rodar para gerar uma nova populacao

	max_r = int(n_populacao/2)

	fbest=9999
	aux = [0]
	#caclula o fitnes da geração inicial
	AG.fitnessCalc()
	#rodar até o numero definido de gerações

	for i in range (0,n_gerações):

		novaPopulacao = []
		#criar uma nova geração
		for j in range(0,max_r):
			#seleciona 2 indiduos da geração atual para serem pais de 2 individuos da proxima geração
			pais = AG.torneio()
			#realiza o cruzamento dos pais para gerar 2 novos filhos para a nova geração
			filhos=AG.cruzamento(pais)
			novaPopulacao.append(filhos[0])
			novaPopulacao.append(filhos[1])

		#seleciona melhor elemento da geracao anterior
		elite =AG.populacao[AG.fitness.index(min(AG.fitness))]
		aux[0]=-10+(((10+10)/(2**10-1))*int(elite[0],2))
		#print("elite",elite)
		#print("prova",AG.func_obj(aux))
		#ind= AG.fitness.index(min(AG.fitness))
		#print(ind)
		#print("min" , (min(AG.fitness)))


		#setar a nova população no lugar da anterior
		AG.populacao = novaPopulacao
		#realizar mutação

		muta = AG.mutacao()

		#seta o elite da geracao anterior no lugar de um individuo aleatorio da geracao atual
		#print("a", AG.populacao)
		z=0
		AG.populacao[z] = elite
		#print(z,AG.populacao)
		#calcula o fitness da geração atual
		AG.fitnessCalc()
		#seleciona o melhor da geração atual para printar
		best = AG.populacao[AG.fitness.index(min(AG.fitness))]
		#printa caso o melhor  fitness da geração atual seja melhor que o ja encontrado anteriormente ou seja a ultima geração
		#if min(AG.fitness)<fbest or i==n_gerações-1:
		fbest = min(AG.fitness)
		print("geração: %d, Melhor Individuo[ fitnes: %f, binario: %s, inteiro: " % (i+1,min(AG.fitness), best),end='')
		for i in range(0,n):
			print(int(best[i],2),end=' ' )
		print("]")

if __name__ == '__main__':
	main()
