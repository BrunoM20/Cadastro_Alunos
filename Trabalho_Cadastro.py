# Bruno Vieira Martins RGM: 29885949
# Gabriel Costa Valin RGM: 29069815


class aluno:
    
    def __init__(self,rgm,nome,endereco,curso):
        self.rgm = rgm
        self.nome = nome 
        self.endereco = endereco
        self.curso = curso
        
class disciplina:
    
    def __init__(self,codigo,nome,nota,frequencia):
        self.codigo = codigo
        self.nome = nome
        self.nota = nota
        self.frequencia = frequencia
        
        
class ListaNoDisciplina:
    
    def __init__(self,disciplina):
        self.disciplina = disciplina 
        self.proximo = None 
        
class ListaLigadaDisciplina:
    
    def __init__(self):
        self.inicio = None 
        
    def InsereDisciplina(self,disciplina):
        no = ListaNoDisciplina(disciplina)
        no.proximo = self.inicio
        self.inicio = no 
        
    def alteraDisciplina(self,disciplina):
        noAtual = self.inicio
        while noAtual:
            if noAtual.disciplina.codigo == disciplina.codigo:
                noAtual.disciplina = disciplina
            noAtual = noAtual.proximo
    
    def excluiDisciplina(self,codigo):
        if self.inicio is None:
            return False
        
        if self.inicio.disciplina.codigo == codigo:
            self.inicio = self.inicio.proximo
            return True
            
        anterior = self.inicio
        atual = self.inicio.proximo
        
        while atual:
            if atual.disciplina.codigo == codigo:
                anterior.proximo = atual.proximo
                return True
        return False
            
    def mostraDisciplina(self):
        noAtual = self.inicio
        while noAtual is not None:
            print(f"\nDisciplina \nCodigo: {noAtual.disciplina.codigo} \nNome: {noAtual.disciplina.nome} \nNota: {noAtual.disciplina.nota} \nFrequencia: {noAtual.disciplina.frequencia}%")
            print("-" * 100)
            noAtual = noAtual.proximo
        
class ListaNoAluno:
    
    def __init__(self, aluno):
        self.aluno = aluno
        self.proximo = None
        self.lista = ListaLigadaDisciplina()
    
class ListaLigadaAluno():
    
    def __init__(self):
        self.inicio = None 
        
    def InsereAluno(self,aluno):
        no = ListaNoAluno(aluno)
        if self.inicio is None or aluno.rgm < self.inicio.aluno.rgm:
            no.proximo = self.inicio 
            self.inicio = no 
        else:
            noAtual = self.inicio
            while noAtual.proximo is not None and aluno.rgm >= noAtual.proximo.aluno.rgm:
                noAtual = noAtual.proximo
            no.proximo = noAtual.proximo 
            noAtual.proximo = no 
    
    def obtemListaDisciplina(self,rgm):
        p = self.inicio
        while p:
            if p.aluno.rgm == rgm:
                return p.lista  
            p = p.proximo 
            
        return None 
    
    def cadastraDisciplina(self,rgm,disciplina):
        l = self.obtemListaDisciplina(rgm)
        if l:
            l.InsereDisciplina(disciplina)
        else:
            print("Aluno não cadastrado")
            
    def alteraDisciplinaAluno(self,rgm,disciplina):
        d = self.obtemListaDisciplina(rgm)
        if d:
            d.alteraDisciplina(disciplina)
            print(f"Disciplina do RGM {rgm} alterada com sucesso")  
        else:
            print("Disciplina não alterada")
            
    def excluiDisciplinaAluno(self,rgm,codigo):
        e = self.obtemListaDisciplina(rgm)
        if e.excluiDisciplina(codigo):
            print(f"A disciplina de codigo {codigo} foi excluida do RGM {rgm}")
        else:
            print("Disciplina ou aluno não encontrados")

    
    def verificaDisciplinaCadastrada(self,rgm):
        lista_disciplinas = self.obtemListaDisciplina(rgm)
        if lista_disciplinas is not None and lista_disciplinas.inicio is not None:
            return True
        else:
            return False
              
    def alteraAluno(self,aluno):
        a = self.inicio
        while a:
            if a.aluno.rgm == aluno.rgm:
                a.aluno = aluno
            a = a.proximo
 
                
    def excluiAluno(self,rgm):
        if self.inicio is None:
            print("Lista de alunos vazia")
            return
        
        if self.inicio.aluno.rgm == rgm and not self.verificaDisciplinaCadastrada(rgm):
            self.inicio = self.inicio.proximo
            print(f"Aluno com RGM {rgm} foi removido")
            return
        
        anterior = self.inicio
        atual = self.inicio.proximo
        
        while atual:
            if atual.aluno.rgm == rgm and not self.verificaDisciplinaCadastrada(rgm):
                anterior.proximo = atual.proximo
                print(f"Aluno com RGM {rgm} foi removido")
                return 
            anterior = atual
            atual = atual.proximo
        print(f"Aluno com o RGM {rgm} não foi removido")
                
                          
    def mostraLista(self):
        noAtual = self.inicio
        while noAtual:
            print(f"\nAluno \nRGM: {noAtual.aluno.rgm} \nNome: {noAtual.aluno.nome} \nEndereço: {noAtual.aluno.endereco} \nCurso: {noAtual.aluno.curso}")
            noAtual.lista.mostraDisciplina()
            noAtual = noAtual.proximo
            
    def alunosReprovados(self):
        noAtual = self.inicio
        print("\nAlunos Reprovados:")
        while noAtual:
            lista_disciplina = noAtual.lista
            no_disciplina = lista_disciplina.inicio
            while no_disciplina:
                if no_disciplina.disciplina.nota < 6:
                    print(f"{noAtual.aluno.nome}")
                    break
                no_disciplina = no_disciplina.proximo
            noAtual = noAtual.proximo 
            
    def alunosAprovados(self):
        noAtual = self.inicio
        print("\nAlunos Aprovados:")
        while noAtual:
            lista_disciplina = noAtual.lista
            no_disciplina = lista_disciplina.inicio
            while no_disciplina:
                if no_disciplina.disciplina.nota >= 6:
                    print(f"{noAtual.aluno.nome}")
                    break
                no_disciplina = no_disciplina.proximo
            noAtual = noAtual.proximo                
        
            
la = ListaLigadaAluno()

la.InsereAluno(aluno(1529, "Matheus", "Travessa Lemos, 25", "Direito"))
la.InsereAluno(aluno(1296, "Rodrigo", "Travessa Nossa Senhora, 75", "Engenharia Civil"))
la.InsereAluno(aluno(1876, "Fernanda", "Rua Tiradentes, 96", "Psicologia"))
la.InsereAluno(aluno(1356, "Gabriel", "Rua da Saudade, 63", "Arquitetura"))
la.InsereAluno(aluno(2036, "Alexa", "Travessa Silicio, 15", "Direito"))
la.InsereAluno(aluno(3652, "Fabricio", "Avenida da Saudade, 221", "Gastronomia"))
la.InsereAluno(aluno(1458, "Paula", "Rua Padre Antonio, 322", "Artes Cenicas"))

la.cadastraDisciplina(1529, disciplina(150, "Direito Penal", 9.5, 80))
la.cadastraDisciplina(1876, disciplina(233, "Psicanalise", 8, 90))
la.cadastraDisciplina(1356, disciplina(980, "Design de Interior", 2, 50))
la.cadastraDisciplina(2036, disciplina(150, "Direito Penal", 4.5, 60))
la.cadastraDisciplina(1296, disciplina(500, "Estruturas", 7.5, 65))

la.alteraDisciplinaAluno(1296, disciplina(500, "Ciencia de Dados", 5, 80))

la.alteraAluno(aluno(3652, "Alice", "Travessa Teresinha, 55", "Medicina"))

la.cadastraDisciplina(3652, disciplina(369, "Anatomia Humana", 2.5, 80))

la.excluiAluno(1458)

la.excluiDisciplinaAluno(3652,369)

la.mostraLista()

la.alunosReprovados()

la.alunosAprovados()
