from flask import Flask, jsonify

app = Flask(__name__)

businessman = [
    {
        "name": "Luiz Barsi",
        "historic": "Considerado o maior investidor individual do Brasil, Luiz Barsi, agora com 80 anos, já foi engraxate. Começou sua carreira de investidor na década de 1960, comprando ações da Cesp. Segundo reportagem do jornal O Estado de S. Paulo de agosto de 2019, seu patrimônio chega a quase R$ 2 bilhões. Mesmo assim, mantém hábitos simples e anda de metrô pela cidade. Sua estratégia de investimento na bolsa de valores consiste em comprar ações que pagam bons dividendos e ficar com elas, independentemente da variação no preço dos papéis. Segundo ele, a ideia não é investir em ações da bolsa, mas comprar participações em boas empresas."
    },
    {
        'name': 'Victor Adler',
        'historic': 'Victor Adler divide com Luiz Barsi e outro integrante desta lista, Lírio Parisotto, o posto de um dos maiores acionistas da Eternit, conhecida por ser uma boa pagadora de dividendos. Em 2019, o investidor anunciou que seu fundo alcançou neste ano 5,3% de participação acionária na empresa de telefonia Oi. Mais discreto do que a maioria dos seus pares, comunga com Barsi o desapreço pela renda fixa e a preferência pelo mercado acionário. Para o portal Exame, deixou claro também que o mercado imobiliário não era a sua praia. Considera altos os custos com advogados e corretores e prefere fugir da baixa liquidez do setor.'
    },
    {
        'name': 'Eufrásia Teixeira Leite',
        'historic': 'Nascida em 1850, Eufrásia Teixeira Leite foi uma mulher à frente de seu tempo. Perdeu os pais em 1872 e passou, junto com a sua irmã Francisca Bernardina, a administrar a herança recebida. Conseguiu multiplicar sua fortuna e deixou, em testamento, um valor que poderia comprar 1.850 quilos de ouro, ao preço da época. Morreu em 1930 e hoje seria considerada bilionária. Deixou a maior parte da herança a instituições assistenciais e educacionais da cidade de Vassouras, no Rio de Janeiro. A riqueza também lhe garantiu independência para viver de acordo com as suas escolhas, sem prestar contas a ninguém. Foi assim que concedeu a própria mão em casamento ao abolicionista Joaquim Nabuco. Foram 14 anos de idas e vindas, mas o casamento jamais ocorreu.'
    },
    {
        'name': 'Guilherme Affonso Ferreira',
        'historic': 'Outro grande investidor, Guilherme Affonso Ferreira é filho de um colaborador da Caterpillar, de quem herdou o apreço pelo trabalho árduo. Fez a graduação em engenharia de produção pela Escola Politécnica da USP (Universidade de São Paulo) e depois passou um ano fazendo estágios em diversos países. Sua história está bastante ligada à da Caterpillar, uma fabricante de máquinas, motores e veículos pesados. Com as sobras de capital da empresa, ele começou a fazer investimentos em outros negócios, que tivessem um ciclo diferente do negócio principal. Assim, aproveitou para comprar outras empresas com dinheiro novo por meio do fundo que administra, o Teorema.'
    }
]

@app.route('/businessman', methods=['GET'])#desnecessário, já que o get é método padrão
def home():
    app.config['JSON_AS_ASCII'] = False#evitando problemas com caracteres especiais
    app.config['JSON_SORT_KEYS'] = False#ignorando a ordem alfabética de posicionamento
    return jsonify(businessman), 200

if __name__ == '__main__':
    app.run(debug=True)