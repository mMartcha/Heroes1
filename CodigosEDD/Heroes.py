class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.proximo = None

class AgendaHeroes:
    def __init__(self):
        self.tamanho = 26
        self.tabela = [None] * self.tamanho

    def calcular_indice(self, letra):
        indice = ord(letra.upper()) - ord('A')
        return indice

    def adicionar_contato(self, nome, telefone):
        letra_inicial = nome[0]
        indice = self.calcular_indice(letra_inicial)

        novo_contato = Contato(nome, telefone)

        if self.tabela[indice] is None:
            self.tabela[indice] = novo_contato
        else:
            atual = self.tabela[indice]
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_contato

    def buscar_contato(self, nome):
        letra_inicial = nome[0]
        indice = self.calcular_indice(letra_inicial)

        atual = self.tabela[indice]
        while atual:
            if atual.nome == nome:
                return atual.telefone
            atual = atual.proximo
        return None

    def listar_contatos_por_letra(self, letra):
        indice = self.calcular_indice(letra)
        contatos = []

        atual = self.tabela[indice]
        while atual:
            contatos.append((atual.nome, atual.telefone))
            atual = atual.proximo

        return contatos

    def remover_contato(self, nome):
        letra_inicial = nome[0]
        indice = self.calcular_indice(letra_inicial)

        atual = self.tabela[indice]
        anterior = None

        while atual:
            if atual.nome == nome:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.tabela[indice] = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def importar_contatos(self, arquivo):
        with open(arquivo, 'r') as f:
            for linha in f:
                nome, telefone = linha.strip().split(',')
                self.adicionar_contato(nome, telefone)

if __name__ == "__main__":
    agenda = AgendaHeroes()
    arquivo_contatos = 'agenda.csv'
    
    agenda.importar_contatos(arquivo_contatos)

    while True:
        print("\nOpções:")
        print("1. Adicionar Super-Herói")
        print("2. Buscar Super-Heróis")
        print("3. Mostrar todos os Super-Heróis pela primeira letra")
        print("4. Remover Super-Herói")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do Super-Herói: ")
            telefone = input("Telefone do Super-Herói: ")
            agenda.adicionar_contato(nome, telefone)
            print("Super-Herói adicionado com sucesso!")

        elif escolha == '2':
            nome = input("Nome do Super-Herói a ser buscado: ")
            telefone = agenda.buscar_contato(nome)
            if telefone:
                print(f"Telefone do Super-Herói: {telefone}")
            else:
                print("Super-Herói não encontrado!")

        elif escolha == '3':
            letra = input("Digite a letra inicial: ")
            contatos = agenda.listar_contatos_por_letra(letra)
            if contatos:
                print(f"Super-Heróis com a letra {letra}:")
                for nome, telefone in contatos:
                    print(f"Nome: {nome}, Telefone: {telefone}")
            else:
                print("Nenhum Super-Herói encontrado com essa letra inicial!")

        elif escolha == '4':
            nome = input("Nome do Super-Herói a ser removido: ")
            if agenda.remover_contato(nome):
                print("Super-Herói removido com sucesso!")
            else:
                print("Super-Herói não encontrado!")

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
