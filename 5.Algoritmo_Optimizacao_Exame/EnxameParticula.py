import random
import numpy as np
from operator import itemgetter
class algPSO():
    def __init__(self,dimensao,tam_populacao,min,max,w,c1,c2):
        self.tam_populacao=tam_populacao
        self.dimensao=dimensao
        self.min=min
        self.max=max
        self.bestGeral=[]
        self.bestIndividuo=[]
        self.velocidade=[]
        self.w=w
        self.c1=c1
        self.c2=c2
        self.gerarPopulacao()

    def gerarPopulacao(self):
        self.populacao = []
        self.populacao.clear()
        for i in range(0,self.tam_populacao):
            sublist = []
            sublistvelocidade = []
            sublistbest=[]
            for j in range(0,self.dimensao):
                if j==0:
                    sublistbest.append(99999)
                sublist.append(random.uniform(self.min, self.max))
                sublistvelocidade.append(sublist[j]*0.1)
                sublistbest.append(random.uniform(self.min, self.max))
            self.populacao.append(sublist)
            self.bestIndividuo.append(sublistbest)
            self.velocidade.append(sublistvelocidade)
        self.bestGeral.append(sublistbest)

    def funcObjetivo2(self,individuo):
        x=0
        for i in range(0,self.dimensao):
            x+=individuo[i]**4-16*individuo[i]**2+5*individuo[i]
        return x/2

    def funcObjetivo(self,individuo):
        x=0
        for i in range(0,self.dimensao):
            x+=individuo[i]**2
        return x**2

    def econtrarMelhorValor(self):
        for i  in range(self.tam_populacao):
            fitness=self.funcObjetivo(self.populacao[i])
            if(fitness<self.bestIndividuo[i][0]):
                for j in range(self.dimensao):
                    self.bestIndividuo[i][0]=fitness
                    self.bestIndividuo[i][j+1]=self.populacao[i][j]
                if(fitness<self.bestGeral[0][0]):
                    for j in range(self.dimensao):
                        self.bestGeral[0][0]=fitness
                        self.bestGeral[0][j+1]=self.populacao[i][j]

    def calcVelocidade(self):
        #print(self.velocidade)
        for i in range(0,self.tam_populacao):
            for j in range(0,self.dimensao):
                r1=random.random()
                r2=random.random()
                self.velocidade[i][j]=self.w*self.velocidade[i][j]+ self.c1*r1*(self.bestIndividuo[i][j+1]-self.populacao[i][j])+ self.c2*r2*(self.bestGeral[0][j+1]-self.populacao[i][j])
        #print(self.velocidade)

    def mover(self):
        for i in range(0,self.tam_populacao):
            for j in range(0,self.dimensao):
                novaPosition=self.populacao[i][j]+self.velocidade[i][j]
                if novaPosition>self.max:
                    self.populacao[i][j]=self.max
                elif novaPosition<self.min:
                    self.populacao[i][j]=self.min
                else:
                    self.populacao[i][j]=novaPosition
    def printarResult(self):
        print(self.bestGeral[0])

def main():
    numero_iteracoes=500
    dimensao=2
    tam_populacao=100
    min=-100
    max=100
    w=0.2
    c1=1
    c2=2

    pso=algPSO(dimensao,tam_populacao,min,max,w,c1,c2)
    for i in range(numero_iteracoes):
        pso.econtrarMelhorValor()
        pso.calcVelocidade()
        pso.mover()
        pso.printarResult()



if __name__ == '__main__':
	main()
