import numpy as np
import sys
import random
from operator import itemgetter
np.set_printoptions(threshold=sys.maxsize)



class algFormiga():
    def __init__(self,num_formigas,num_cidade,A,B,P):
        self.num_formigas = num_formigas
        self.num_cidade = num_cidade
        self.A = A
        self.B = B
        self.P=P
        self.preparacao()

    def preparacao(self):
        self.distancia = []
        with open('dist.txt') as f:
            for line in f:
                temp_list = [int(x) for x in line.strip().split()]
                if len(temp_list) > 0:  # don't append an empty list (blank line)
                    self.distancia.append(temp_list)

        self.formigas = np.zeros((self.num_cidade,self.num_cidade),dtype=int)
        self.feromonios = np.full((self.num_formigas,self.num_cidade),1/10**16)
        np.fill_diagonal(self.feromonios,0)

        for index,i in enumerate(self.formigas):
            i[0]=index




    def funcaoProb(self,cidadeAtualFormiga,cidadesnaovisitadas):
        soma=0
        A=self.A
        B=self.B
        roleta=[]
        for i in cidadesnaovisitadas:

            soma+=(self.feromonios[cidadeAtualFormiga][i]**A) *(1/(self.distancia[cidadeAtualFormiga][i]**B))

        for i in cidadesnaovisitadas:
            roleta.append(((self.feromonios[cidadeAtualFormiga][i]**A) *((1/self.distancia[cidadeAtualFormiga][i])**B))/soma)

        rndvalue=random.uniform(0,1)
        soma=0
        for j in range(0,len(cidadesnaovisitadas)):
            soma+=roleta[j]
            if(soma>=rndvalue):
                break
        return cidadesnaovisitadas[j]
    


    def funcobj(self,formigas):
        soma=0
        for i in range(0,self.num_formigas-1):
            soma+=self.distancia[formigas[i]][formigas[i+1]]
        soma+=self.distancia[formigas[i+1]][formigas[0]]
        return soma

    def somaferm(self,v1,v2,caminhoFormigas,distMelhoresCominhos):

        q=100
        feromonioAdicional=0
        for i in range(0,self.num_formigas):
            for j in range(0,self.num_cidade-1):
                if(caminhoFormigas[i][j]==v1 and caminhoFormigas[i][j+1]==v2):
                    feromonioAdicional+=q/distMelhoresCominhos[i]
                    break
        return feromonioAdicional

    def calcFeromonios(self,caminhoFormigas,distMelhoresCominhos):
        p=self.P

        for i in range(0,self.num_cidade):
            for j in range(0,self.num_cidade):
                self.feromonios[i][j]=(1-p)*self.feromonios[i][j]+self.somaferm(i,j,caminhoFormigas,distMelhoresCominhos)



def main():
    num_cidade=15
    num_formigas=15
    A=1
    B=5
    P=0.2
    valoresA=[1,5,10]
    valoresB=[1,5,10]
    valoresP=[0.2,0.5,0.9]
    combinacoes=[]
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                preset=[]
                preset.append(valoresA[i])
                preset.append(valoresB[j])
                preset.append(valoresP[k])
                combinacoes.append(preset)

    limite_iterações=25
    execucoes=20
    resultCombinacoes=[]
    num_combinacoes=27
    for m in range(0,num_combinacoes):
        A=combinacoes[m][0]
        B=combinacoes[m][1]
        P=combinacoes[m][2]
        somaExecs=0
        for l in range(0,execucoes):
            AG_Formiga = algFormiga(num_formigas,num_cidade,A,B,P)
            for i in range(0,limite_iterações):
            #percorre por todas as formigas
                melhorCaminhoValor=999999999
                melhorCaminhoCidades=[]
                melhores=[]
                melhoresCidades=[]
                for j in range(0,num_formigas):

                    cidadesnaovisitadas=np.arange(num_cidade).tolist()
                    cidadesnaovisitadas.remove(AG_Formiga.formigas[j][0])
                    for k in range(0,num_cidade-1):
                        AG_Formiga.formigas[j][k+1]=AG_Formiga.funcaoProb(int(AG_Formiga.formigas[j][k]),cidadesnaovisitadas)
                        cidadesnaovisitadas.remove(int(AG_Formiga.formigas[j][k+1]))
                    melhores.append(AG_Formiga.funcobj(AG_Formiga.formigas[j]))
                    melhoresCidades.append(AG_Formiga.formigas[j].tolist())
                    if(melhores[j]<melhorCaminhoValor):
                       melhorCaminhoValor=melhores[j]
                       melhorCaminhoCidades=AG_Formiga.formigas[j].tolist()
                AG_Formiga.calcFeromonios(melhoresCidades,melhores)



            somaExecs+=melhorCaminhoValor
            if(l==19):
                resultCombinacoes.append(somaExecs/20)
    list_b=np.arange(num_combinacoes).tolist()
    resultCombinacoes= list(zip(resultCombinacoes, list_b))
    resultCombinacoes.sort(key=itemgetter(0))
    for i in range(0,num_combinacoes):
        print("Media das 20 execs ", resultCombinacoes[i][0])
        print("Parametros usados " , combinacoes[resultCombinacoes[i][1]])




if __name__ == '__main__':
	main()
