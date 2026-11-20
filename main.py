
class ModeloIA:
    def __init__(self, nome, custo_por_requisicao):
        self.nome = nome
        self.__custo_por_requisicao = custo_por_requisicao
        
    def executar(self, prompt):
        pass
    
    def obter_custo(self):
        return self.__custo_por_requisicao
        
    def __str__(self):
        return f"Modelo: {self.nome} | Custo/req: ${self.__custo_por_requisicao:.2f}"
    
    
class ModeloLLM(ModeloIA):
    def __init__(self, nome, custo_por_requisicao, temperatura):
        super().__init__(nome, custo_por_requisicao)
        self.temperatura = temperatura
    
    def executar(self, prompt):
        print(f"{self.nome} gerando texto para '{prompt}' (Temperatura: {self.temperatura:.2f})")
        
        
class ModeloVisao(ModeloIA):
    def __init__(self, nome, custo_por_requisicao, resolucao):
        super().__init__(nome, custo_por_requisicao)
        self.resolucao = resolucao
        
    def executar(self, prompt):
        print(f"{self.nome} gerando imagem para '{prompt}' (Resolução: {self.resolucao})")
        
class PipelineIA:
    def __init__(self):
        self.modelos = []
        
    def adicionar_modelo(self, modelo):
        self.modelos.append(modelo) 
        
    def rodar_todos(self, prompt):
        custo_total = 0.0
        
        for modelo in self.modelos:
            modelo.executar(prompt)
            custo_total += modelo.obter_custo()
            
        print(f"Custo total da execução: $ {custo_total:.2f}")
        
        
        
# Testando

gpt = ModeloLLM("GPT-4o", 0.05, 0.7)
dall_e = ModeloVisao("DALL-E 3", 0.12, "1024x1024")

print(gpt)
print(dall_e)
print("-" * 40)

pipeline = PipelineIA()
pipeline.adicionar_modelo(gpt)
pipeline.adicionar_modelo(dall_e)
pipeline.rodar_todos("Um robô programando em Python")
