from time import sleep
import pyautogui as py
import random
from sys import exit

def open_browsers():
    py.PAUSE_TIME = 5
    py.press("win")
    py.write("edge")
    sleep(2)
    py.press("enter")
    sleep(5)
    py.hotkey("win", "left")
    sleep(2)
    py.press("win")
    sleep(1)
    py.write("Fire Fox")
    py.press("enter")
    sleep(5)
    py.hotkey("win", "right")
    sleep(7)
    py.write("https://www.bing.com/")
    sleep(3)
    py.press("enter")
def init_serch():
    py.PAUSE_TIME = 5
    py.click(x=367, y=370)
    x = random.randint(1, 100)
    py.write(str(x))
    py.press("enter")
    sleep(2.5)
    py.click(x=1394, y=364)
    sleep(1)
    x = random.randint(1, 100)
    py.write(str(x))
    py.press("enter")

    pesquisas = [
    "abacaxi", "abelha", "abóbora", "abraço", "abrigo", "acampamento", "açúcar", "água",
    "agulha", "avião", "azul", "banana", "barco", "bicicleta", "biblioteca", "bola",
    "borboleta", "brinquedo", "cachoeira", "caderno", "cadeira", "café", "caminho", "camisa",
    "caneta", "carro", "casa", "castelo", "cavalo", "celular", "chave", "chuva",
    "cidade", "cinema", "coelho", "computador", "coração", "corda", "copo", "coruja",
    "criança", "dança", "deserto", "diamante", "dinheiro", "disco", "dragão", "elefante",
    "escola", "espelho", "estrela", "faca", "fazenda", "feijão", "festa", "flor",
    "floresta", "foguete", "formiga", "fotografia", "fruta", "futebol", "garrafa", "gato",
    "girafa", "globo", "golfinho", "grama", "guitarra", "helicóptero", "história", "hotel",
    "igreja", "ilha", "imagem", "janela", "jardim", "joaninha", "jornal", "jogo",
    "lago", "laranja", "leão", "livro", "lua", "macaco", "maçã", "madeira",
    "mar", "martelo", "mesa", "montanha", "moto", "música", "navio", "neve",
    "noite", "nuvem", "oceano", "olho", "ônibus", "ovelha", "palácio", "papagaio",
    "papel", "parque", "passarinho", "peixe", "piano", "planeta", "praia", "prédio",
    "presente", "professor", "quadro", "queijo", "raposa", "relógio", "rio", "robô",
    "rosa", "sapo", "satélite", "selva", "sorvete", "tartaruga", "telefone", "televisão",
    "tempestade", "tesouro", "tigre", "tomate", "torre", "trator", "trem", "universo",
    "urso", "vaca", "vale", "vento", "viagem", "violão", "vulcão", "adolescente",
    "adulto", "amigo", "amor", "alegria", "amizade", "aventura", "beleza", "bondade",
    "bravura", "calma", "carinho", "coragem", "curiosidade", "desejo", "esperança", "felicidade",
    "força", "generosidade", "honestidade", "humildade", "imaginação", "inteligência", "justiça", "liberdade",
    "memória", "mistério", "orgulho", "paciência", "paz", "perigo", "prazer", "respeito",
    "saudade", "segurança", "silêncio", "sinceridade", "talento", "verdade", "vitória", "vontade",
    "sabedoria", "responsabilidade", "criatividade", "determinação", "disciplina", "energia", "equilíbrio", "experiência",
    "confiança", "conhecimento", "sucesso", "futuro", "passado", "momento", "tempo", "destino",
    "sorte", "azar", "segredo", "arco", "armário", "âncora", "antena", "apito",
    "aquecedor", "aquário", "areia", "arroz", "azeitona", "balão", "banco", "bandeira",
    "baú", "berço", "bilhete", "binóculo", "blusa", "botão", "brinco", "broto",
    "bule", "cabide", "cachorro", "caixa", "calendário", "câmera", "campainha", "caneca",
    "canoa", "capacete", "carteira", "cartaz", "cartão", "casaco", "cesta", "chapéu",
    "chaveiro", "chocolate", "chuveiro", "cobertor", "colchão", "colher", "concha", "controle",
    "cortina", "cristal", "dado", "diário", "dicionário", "escada", "escova", "espada",
    "estojo", "etiqueta", "filtro", "fone", "forno", "frigideira", "garfo", "guarda",
    "isqueiro", "lápis", "lanterna", "lata", "liquidificador", "maleta", "mapa", "mochila",
    "molde", "panela", "pente", "pergaminho", "pincel", "porta", "prato", "rádio",
    "rede", "sacola", "sapato", "serrote", "sofá", "tapete", "tesoura", "toalha",
    "travesseiro", "vaso", "vassoura", "vela", "ventilador", "xícara", "zíper", "amarelo",
    "amargo", "alto", "antigo", "apertado", "ardente", "baixo", "barulhento", "bonito",
    "branco", "brilhante", "caloroso", "claro", "colorido", "comprido", "confortável", "corajoso",
    "curto", "delicado", "difícil", "doce", "duro", "elegante", "enorme", "escuro",
    "especial", "estranho", "fácil", "famoso", "feliz", "forte", "fraco", "frio",
    "gelado", "gigante", "gracioso", "horrível", "jovem", "leve", "limpo", "lento",
    "louco", "macio", "maravilhoso", "moderno", "molhado", "novo", "pequeno", "pesado",
    "rápido", "raro", "redondo", "rico", "seco", "simples", "suave", "sujo",
    "tranquilo", "triste", "velho", "verde", "vermelho", "vivo", "vazio", "andar",
    "aprender", "amar", "aparecer", "aproveitar", "arriscar", "assistir", "atacar", "beber",
    "brincar", "buscar", "cair", "cantar", "cavar", "celebrar", "chegar", "cozinhar",
    "correr", "criar", "dançar", "decidir", "deixar", "descobrir", "desenhar", "dormir",
    "encontrar", "ensinar", "entrar", "escrever", "escutar", "escolher", "esperar", "estudar",
    "evitar", "existir", "falar", "fazer", "fechar", "ganhar", "gostar", "guardar",
    "imaginar", "jogar", "lavar", "ler", "levantar", "ligar", "limpar", "mandar",
    "marchar", "medir", "morar", "mostrar", "nadar", "nascer", "observar", "ouvir",
    "pagar", "parar", "partir", "passar", "pensar", "perder", "perguntar", "pesquisar",
    "pintar", "plantar", "pular", "receber", "recordar", "rir", "saber", "sair",
    "sentar", "sentir", "sonhar", "subir", "ter", "terminar", "tocar", "trabalhar",
    "trazer", "viajar", "viver", "voltar", "votar", "voar", "abandonar", "aceitar",
    "acordar", "admirar", "adicionar", "ajudar", "alcançar", "alegrar", "alugar", "analisar",
    "anunciar", "apagar", "apresentar", "aprovar", "arrumar", "assinar", "aumentar", "avisar",
    "bater", "bloquear", "caminhar", "cancelar", "carregar", "casar", "causar", "chamar",
    "comparar", "completar", "comprar", "concordar", "construir", "contar", "continuar", "controlar",
    "conversar", "convidar", "copiar", "corrigir", "cortar", "cuidar", "deitar", "demonstrar",
    "depender", "descrever", "desenvolver", "desligar", "destruir", "detalhar", "devolver", "dirigir",
    "discutir", "dividir", "dobrar", "dominar", "economizar", "eliminar", "empurrar", "encostar",
    "entender", "entregar", "enviar", "errar", "escapar", "esconder", "esquecer", "estabelecer",
    "executar", "explicar", "explorar", "expressar", "fabricar", "ferver", "formar", "funcionar",
    "gerar", "gritar", "identificar", "ignorar", "iniciar", "inspirar", "instalar", "inventar",
    "investigar", "juntar", "lembrar", "liberar", "localizar", "manter", "melhorar", "misturar",
    "modificar", "necessitar", "notar", "organizar", "participar", "perceber", "permitir", "preparar",
    "produzir", "proteger", "publicar", "realizar", "reconhecer", "reduzir", "repetir", "resolver",
    "responder", "retirar", "reunir", "salvar", "separar", "significar", "solucionar", "suportar",
    "transformar", "transportar", "utilizar", "verificar", "visitar", "academia", "aeroporto",
    "aldeia", "avenida", "bairro", "cafeteria", "capital", "catedral", "centro", "clube",
    "colégio", "comércio", "continente", "corredor", "estação", "estádio", "faculdade", "farmácia",
    "galeria", "garagem", "hospital", "laboratório", "loja", "mercado", "museu", "oficina",
    "padaria", "piscina", "praça", "porto", "restaurante", "rodovia", "salão", "shopping",
    "teatro", "universidade", "zoológico", "astronomia", "biologia", "química", "física", "matemática",
    "geografia", "filosofia", "literatura", "gramática", "ciência", "tecnologia", "engenharia", "medicina",
    "economia", "política", "cultura", "sociedade", "educação", "ambiente", "natureza", "galáxia",
    "átomo", "molécula", "célula", "matéria", "gravidade", "espaço", "cometa", "asteroide",
    "dinossauro", "evolução", "genética", "ecologia", "clima", "relevo", "território", "população",
    "latitude", "longitude", "democracia", "república", "governo", "constituição", "cidadania", "direito",
    "lei", "estado", "computação", "programação", "algoritmo", "código", "servidor", "internet",
    "site", "aplicativo", "programa", "sistema", "arquivo", "pasta", "teclado", "monitor",
    "mouse", "processador", "bateria", "navegador", "usuário", "dados", "tabela", "função",
    "variável", "classe", "objeto", "python", "javascript", "html", "css", "backend",
    "frontend", "software", "hardware", "robótica", "máquina", "automação", "digital", "virtual",
    "conexão", "metal", "ouro", "prata", "cobre", "ferro", "alumínio", "borracha",
    "tecido", "algodão", "seda", "cimento", "concreto", "petróleo", "gás", "carvão",
    "minério", "sal", "esmeralda", "pantera", "onça", "lobo", "rinoceronte", "hipopótamo",
    "gorila", "chimpanzé", "canguru", "coala", "panda", "preguiça", "tamanduá", "tatu",
    "capivara", "veado", "javali", "burro", "boi", "cabra", "galinha", "galo",
    "pato", "ganso", "águia", "falcão", "tucano", "pinguim", "avestruz", "flamingo",
    "gaivota", "baleia", "tubarão", "arraia", "polvo", "lula", "caranguejo", "lagosta",
    "camarão", "jacaré", "crocodilo", "cobra", "lagarto", "iguana", "rã", "salamandra",
    "aranha", "besouro", "mosquito", "grilo", "gafanhoto", "lírio", "margarida", "girassol",
    "orquídea", "tulipa", "violeta", "lavanda", "alecrim", "manjericão", "hortelã", "sálvia",
    "tomilho", "coentro", "salsa", "cebolinha", "alface", "couve", "espinafre", "brócolis",
    "cenoura", "batata", "mandioca", "beterraba", "cebola", "alho", "pepino", "pimentão",
    "berinjela", "abobrinha", "milho", "trigo", "aveia", "ervilha", "lentilha", "soja",
    "amendoim", "limão", "manga", "mamão", "melancia", "melão", "morango", "uva",
    "pêssego", "pera", "ameixa", "cereja", "kiwi", "coco", "abacate", "maracujá",
    "goiaba", "jabuticaba", "acerola", "caju", "figo", "romã", "manhã", "tarde",
    "madrugada", "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo",
    "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
    "setembro", "outubro", "novembro", "dezembro", "primavera", "verão", "outono", "inverno",
    "milênio", "ontem", "hoje", "amanhã", "cedo", "agora", "depois", "norte",
    "sul", "leste", "oeste", "direita", "esquerda", "frente", "trás", "cima",
    "baixo", "dentro", "fora", "perto", "longe", "acima", "abaixo", "borda",
    "entrada", "saída", "primeiro", "terceiro", "quarto", "quinto", "sexto", "sétimo",
    "oitavo", "nono", "décimo", "único", "duplo", "triplo", "metade", "dobro",
    "parte", "grupo", "conjunto", "par", "trio", "equipe", "multidão", "basquete",
    "vôlei", "tênis", "natação", "atletismo", "ciclismo", "ginástica", "boxe", "judô",
    "karatê", "surfe", "skate", "xadrez", "corrida", "escalada", "gol", "time",
    "jogador", "técnico", "árbitro", "torcida", "campeonato", "medalha", "troféu", "competição",
    "partida", "quadra", "campo", "pista", "ponto", "flauta", "violino", "saxofone",
    "trompete", "clarinete", "harpa", "teclado", "tambor", "melodia", "ritmo", "canção",
    "artista", "pintura", "escultura", "poesia", "romance", "conto", "filme", "série",
    "personagem", "fantasia", "ficção", "comédia", "drama", "terror", "ação", "exploração",
    "descoberta", "expedição", "missão", "desafio", "problema", "solução", "enigma", "pista",
    "pirata", "herói", "vilão", "princesa", "príncipe", "cavaleiro", "mago", "monstro",
    "cérebro", "cabeça", "rosto", "orelha", "nariz", "boca", "dente", "língua",
    "pescoço", "ombro", "braço", "mão", "dedo", "peito", "costas", "perna",
    "joelho", "pé", "cabelo", "pele", "osso", "músculo", "sangue", "pulmão",
    "estômago", "fígado", "rim", "corpo", "voz", "chá", "leite", "suco",
    "refrigerante", "sopa", "carne", "frango", "ovo", "pão", "manteiga", "iogurte",
    "pizza", "hambúrguer", "sanduíche", "macarrão", "lasanha", "salada", "bolo", "biscoito",
    "pipoca", "brigadeiro", "pudim", "torta", "gelatina", "marrom", "preto", "cinza",
    "dourado", "prateado", "transparente", "nublado", "chuvoso", "ensolarado", "ventoso", "úmido",
    "semanal", "mensal", "anual", "diário", "noturno", "matinal", "central", "regional",
    "nacional", "mundial", "local", "global", "natural", "artificial", "social", "cultural",
    "histórico", "moderno", "urbano", "rural", "industrial", "comercial", "público", "privado",
    "familiar", "pessoal", "principal", "secundário", "inicial", "final", "normal", "comum",
    "diferente", "possível", "impossível", "necessário", "importante", "interessante", "útil", "inútil",
    "rápido", "vagaroso", "profundo", "raso", "largo", "estreito", "grosso", "fino",
    "redondo", "quadrado", "triangular", "vertical", "horizontal", "reto", "curvo", "aberto",
    "fechado", "cheio", "vazio", "inteiro", "quebrado", "novo", "usado", "seguro",
    "perigoso", "famoso", "desconhecido", "popular", "secreto", "poderoso", "frágil", "resistente",
    "flexível", "elástico", "rígido", "quente", "morno", "fresco", "gelado", "seco",
    "molhado", "doce", "salgado", "azedo", "picante", "amargo", "saboroso", "delicioso",
    "comida", "bebida", "refeição", "cozinha", "receita", "ingrediente", "prateleira", "geladeira",
    "freezer", "fogão", "microondas", "forno", "pia", "torneira", "prateleira", "gaveta",
    "quarto", "sala", "cozinha", "banheiro", "varanda", "telhado", "parede", "chão",
    "teto", "escada", "corredor", "janelas", "cortina", "lâmpada", "tapete", "quadro",
    "espelho", "cama", "armário", "mesa", "cadeira", "estante", "sofá", "poltrona",
    "televisão", "computador", "impressora", "carregador", "fones", "controle", "console", "videogame",
    "internet", "senha", "perfil", "conta", "mensagem", "notícia", "revista", "documento",
    "texto", "palavra", "frase", "pergunta", "resposta", "exemplo", "ideia", "opinião",
    "argumento", "explicação", "informação", "pesquisa", "estudo", "prova", "questão", "resumo",
    "trabalho", "tarefa", "aula", "aluno", "colega", "diretor", "escritor", "autor",
    "leitor", "capítulo", "página", "parágrafo", "título", "tema", "assunto", "história",
    "personagem", "narrador", "cenário", "enredo", "aventura", "mistério", "final", "começo",
    "meio", "resultado", "causa", "efeito", "motivo", "razão", "objetivo", "plano",
    "projeto", "meta", "regra", "ordem", "sinal", "símbolo", "número", "forma",
    "linha", "círculo", "ângulo", "ponto", "distância", "medida", "peso", "altura",
    "largura", "volume", "velocidade", "temperatura", "pressão", "força", "energia", "potência",
    "movimento", "repouso", "luz", "sombra", "som", "eco", "onda", "frequência",
    "espaço", "tempo", "matemática", "número", "cálculo", "conta", "soma", "subtração",
    "multiplicação", "divisão", "fração", "decimal", "porcentagem", "equação", "gráfico", "ângulo",
    "triângulo", "quadrado", "retângulo", "círculo", "esfera", "cubo", "cilindro", "cone",
    "volume", "área", "perímetro", "raiz", "potência", "média", "probabilidade", "estatística",
    "experimento", "laboratório", "microscópio", "telescópio", "planeta", "estrela", "universo", "galáxia",
    "sol", "terra", "marte", "júpiter", "saturno", "urano", "netuno", "mercúrio",
    "vênus", "plutão", "lua", "cometa", "meteorito", "espaçonave", "foguete", "astronauta",
    "órbita", "gravidade", "atmosfera", "oceano", "montanha", "vulcão", "rio", "lago",
    "floresta", "deserto", "geleira", "ilha", "praia", "caverna", "vale", "planície",
    "platô", "colina", "penhasco", "costa", "fronteira", "país", "cidade", "região",
    "estado", "província", "capital", "território", "continente", "população", "mapa", "globo",
    "bússola", "direção", "localização", "coordenada", "latitude", "longitude", "clima", "tempo",
    "temperatura", "chuva", "neve", "vento", "tempestade", "furacão", "tornado", "nuvem",
    "sol", "calor", "frio", "estação", "primavera", "verão", "outono", "inverno",
]
    def pesquisa():
        py.write(str(random.choice(pesquisas)))
        py.press("enter")
        sleep(3.5)

    def pontos():
        py.click(x=342, y=113)
        sleep(0.25)
        py.hotkey("ctrl", "a")
        py.press("backspace")
        sleep(0.25)
        pesquisa()
        py.click(x=1553, y=106)
        sleep(0.25)
        py.hotkey("ctrl", "a")
        py.press("backspace")
        pesquisa()
        sleep(5)
    

    pontos()

    for n in range(20):
        pontos()
def Definido_diariamente():
    sleep(3)
    py.click(x=1349, y=21)
    py.click(x=1349, y=21)
    py.hotkey("ctrl", "a")
    py.press("backspace")
    py.write("https://www.bing.com/rewards/dashboard")
    py.press("enter")
    sleep(1)
    py.moveTo(x=1470, y=376)
    sleep
    for n in range(11):
        py.scroll(-100)
    sleep(2)     
    with py.hold("ctrl"):
        py.click(x=1371, y=499)
        sleep(0.25)
        py.click(x=1371, y=673)
        sleep(0.25)
        py.click(x=1371, y=877)
        sleep(0.25)    
def browsers():
      py.click(x=1897, y=34)
      sleep(0.5)
      py.click(x=916, y=43)
def code():
    open_browsers()
    init_serch()
    Definido_diariamente()
    browsers()
    exit()

code()