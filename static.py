
class A():
  variavel = 10

  def __init__(self):
    self.variavel = 15

if __name__ == '__main__':
    print(A.variavel) #resultado 10 - variável da classe
    print(A().variavel) #resultado 15 - variável do objeto