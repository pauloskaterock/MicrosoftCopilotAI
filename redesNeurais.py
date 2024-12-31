# Explicação de Redes Neurais
# Redes neurais são sistemas computacionais inspirados na estrutura do cérebro humano. Elas consistem em camadas de nós (neurônios) interconectados que podem aprender a realizar tarefas específicas, como reconhecimento de padrões, classificação, e predição, através de um processo de treinamento.

# Estrutura Básica
# Camada de Entrada: Recebe os dados de entrada.
# Camadas Ocultas: Processam as entradas, realizando cálculos para extrair características mais complexas dos dados.
# Camada de Saída: Produz o resultado final da rede neural.
# Cada conexão entre os nós tem um peso associado, que é ajustado durante o treinamento para minimizar o erro da rede.

# Processo de Treinamento
# Forward Propagation: Os dados de entrada são passados através das camadas da rede, produzindo uma saída.
# Cálculo do Erro: A saída da rede é comparada com o valor real para calcular o erro.
# Backward Propagation: O erro é propagado de volta pela rede para ajustar os pesos das conexões, reduzindo o erro nas próximas iterações.
# Tutorial Prático
# Vamos criar uma rede neural simples usando o Keras, uma biblioteca popular de aprendizado de máquina em Python, para resolver um problema de classificação básico: o famoso dataset de dígitos manuscritos (MNIST).

# Passo 1: Instalação das Bibliotecas
# Primeiro, instale as bibliotecas necessárias:


# pip install numpy tensorflow keras matplotlib
# Passo 2: Importar as Bibliotecas

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical


# Passo 3: Carregar e Preparar os Dados

# Carregar o dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar os dados
x_train = x_train / 255.0
x_test = x_test / 255.0

# Converter os rótulos para categóricos (one-hot encoding)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# Passo 4: Construir o Modelo

# Inicializar o modelo
model = Sequential()

# Adicionar a camada de entrada (flatten da imagem 28x28 para um vetor de 784)
model.add(Flatten(input_shape=(28, 28)))

# Adicionar uma camada oculta com 128 neurônios e função de ativação ReLU
model.add(Dense(128, activation='relu'))

# Adicionar a camada de saída com 10 neurônios (um para cada dígito) e função de ativação softmax
model.add(Dense(10, activation='softmax'))

# Passo 5: Compilar o Modelo

# Compilar o modelo com o otimizador Adam e a função de perda categorical crossentropy
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Passo 6: Treinar o Modelo

# Treinar o modelo com os dados de treinamento
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Passo 7: Avaliar o Modelo

# Avaliar o modelo com os dados de teste
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

# Passo 8: Fazer Previsões

# Fazer previsões com o modelo treinado
predictions = model.predict(x_test)

# Visualizar uma previsão
index = 0  # Escolha um índice para visualizar
plt.imshow(x_test[index], cmap='gray')
plt.title(f'Previsão: {np.argmax(predictions[index])}, Real: {np.argmax(y_test[index])}')
plt.show()


# Conclusão
# Neste tutorial, criamos uma rede neural simples usando o Keras para classificar dígitos manuscritos. 
# Passamos pelo processo de carregar e preparar os dados, construir, compilar, treinar, avaliar o modelo, e 
# fazer previsões. Este é um exemplo básico, mas pode ser expandido para problemas mais complexos 
# adicionando mais camadas e ajustando hiperparâmetros.