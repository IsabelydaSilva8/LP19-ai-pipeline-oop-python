#AI Pipeline Orchestrator (POO em Python)

Projeto prático desenvolvido para consolidar os pilares da **Programação Orientada a Objetos (POO)** em Python aplicados a um cenário de Engenharia de IA.

##Conceitos Aplicados
* **Classes e Objetos:** Estruturação de modelos de Inteligência Artificial e do orquestrador.
* **Encapsulamento:** Proteção do atributo privado `__custo_por_requisicao` com leitura controlada via método público.
* **Herança:** Reaproveitamento da classe base `ModeloIA` nas especializações `ModeloLLM` e `ModeloVisao`.
* **Polimorfismo:** Sobrescrita do método `executar(prompt)` para que cada tipo de modelo processe a entrada à sua maneira.
* **Composição e Dunder Methods:** Orquestração de múltiplos modelos na classe `PipelineIA` e formatação amigável com `__str__`.

##Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/IsabelydaSilva8/LP19-ai-pipeline-oop-python
   ```
2. Acesse a pasta e execute o script:
   ```bash
   cd ai-pipeline-oop-python
   python main.py
   ```
