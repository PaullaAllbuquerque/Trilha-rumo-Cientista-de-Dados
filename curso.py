class CursoBase:
    def __init__(self, curso, descricao, escola, duracao):
        self.curso = curso
        self.descricao = descricao
        self.escola = escola
        self.duracao = duracao
        self.concluido = False

    def iniciar_curso(self):
        print(f"Iniciando o curso de {self.curso}!")

    def concluir_curso(self):
        self.concluido = True
        print(f"Parabéns! Você concluiu o curso de {self.curso}.")

    def __str__(self):
        status_conclusao = 'Sim' if self.concluido else 'Não'
        info_curso = (f"Curso: {self.curso}\n"
                      f"Descrição: {self.descricao}\n"
                      f"Escola: {self.escola}\n"
                      f"Duracao: {self.duracao} horas\n"
                      f"Concluído: {status_conclusao}")
        return info_curso
class Resumo:
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def __str__(self):
        return  f"Conteúdo: {self.conteudo}"

class Curso(CursoBase):
    def __init__(self, curso, descricao, escola, duracao, resumo=None):
        super().__init__(curso, descricao, escola, duracao)
        self.resumo = resumo

    def __str__(self):
        info_curso_base = super().__str__()
        if self.resumo:
            info_curso_base += f"\nResumo: \n{self.resumo}"
            return info_curso_base

curso3 = Curso("Python", "Entendendo a Orientação a Objetos", 'Alura', 12)
curso4 = Curso("Python", "Avançando na Orientação a Objetos", 'Alura', 10)
curso5 = Curso("IA Generativa", "ChatGPT: Desvendando a IA em conversas e suas aplicaçòes", 'Alura', 8)
curso6 = Curso("IA Generativa", "ChatGPT: Otimizando a qualidade dos resultados", 'Alura', 8)
curso7 = Curso("IA Generativa", "ChatGPT e programação: aumente sua produtividade", 'Alura', 8)
curso8 = Curso("Data Science", "Python para Data science: primeiros passos", 'Alura', 10)


resumo1 = Resumo("Instalação do Python 3; Lidando com a entrada do usuário; Testando valores; "
                 "A sequência do jogo; Iterando de maneira diferente; Gerando números aleatórios; "
                 "Nível e Pontuação; Organizando ainda melhor o nosso código; Comparando Python com C")

resumo2 = Resumo("Preparando o jogo da forca; Manipulando strings; conhecendo e trabalhando com listas;"
                 "Conhecendo e trabalhando com tuplas;Implementando o encerramento do jogo;"
                 "Escrita e leitura de arquivos; Melhorando o código e a apresentação")

curso1 = Curso("Python", "Começando com a Linguagem", 'Alura', 12, resumo1)
curso2 = Curso("Python", "Avançando na Linguagem", 'Alura', 12, resumo2)

curso2.iniciar_curso()
curso2.concluir_curso()
print(curso2)
