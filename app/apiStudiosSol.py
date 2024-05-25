from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)


#Realiza o cálculo de possibilidades para cada pontuação inteira entre 0 e a maior pontuação obtida 
#
#   Cria um vetor do tamanho do maior placar +1, que é iniciado com 0, menos para o valor da posição 0, pois assume se que se tem uma e somente uma possibilidade (não pontuar).
#  À partir disso itera sobre cada pontuação que pode se ser somada, adicionando a contagem de possibilidades aos próximos numeros, espaçados pela "distância" das pontuações
#  
#   EX: Na iteração sobre a pontuação 3, o valor de 1, contido na posição 0 é somado ao 3,6,9 e assim por diante, sempre espaçado pelo tamanho do ponto.
# Quando é feita a iteração pelos próximos pontos, por exemplo o 6, o valor de 1 é somado nas posições 6,12,18... Porém temos valores de 1 agora nas posições 3,6,9... 
# Então estes valores também são somados as posições do 9,12,15... Sendo assim possível cobrir todas possibilidades de combinações de 0 até o score do vencedor.
#

def calcula_possibilidades(score1,score2): #O(n)
    possible_points= [3,6,7,8]           
    score_vencedor=max(score1,score2)
    vetor_todos= [0] *(score_vencedor+1) 
    vetor_todos[0]=1                     
    for ponto in possible_points:
        for i in range(ponto,score_vencedor+1):
            vetor_todos[i]+=vetor_todos[i-ponto]
    possibilidades=vetor_todos[score1]*vetor_todos[score2]
    return possibilidades
    #print("O total de possíbilidades possíveis para este placar é: {}".format(possibilidades))

#Retira do Json do placar a quantidade de pontos de cada time e chama a função que calcula as possibilidades para cada pontuação
def extrai_pontos(placar):
    score1,score2 = map(int,placar.split('x'))
    #print("os placares obtidos pelos times foram:", score1,score2)
    possibilidades=calcula_possibilidades(score1,score2)
    return{
             "combinations":possibilidades 
          }
    
class VerifyScore(graphene.Mutation):
    class Arguments:
        score = graphene.String(required = True)
    
    combinations = graphene.Int()

    def mutate(self,info,score):
        resposta= extrai_pontos(score)
        return VerifyScore(combinations=resposta["combinations"])
    

class Mutation(graphene.ObjectType):
    verify = VerifyScore.Field()

schema = graphene.Schema(mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
    
)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    
    
    
    #entrada = '{"score": "6x15"}'
    #data=json.loads(entrada)
    #placar=data['score']
    #print("O placar extraido do json foi:{}".format(placar))
    #extrai_pontos(placar)