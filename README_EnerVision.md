
# 💡 EnerVision – Reconhecimento de Gestos para Acionamento de Luzes de Emergência

EnerVision é uma solução de visão computacional para condomínios residenciais, que utiliza **Python + MediaPipe** para detectar o gesto de **cruzar os braços** e ativar/desativar luzes de emergência em caso de quedas de energia.

## 🚨 Problema
Durante apagões causados por eventos climáticos, moradores de condomínios ficam expostos a riscos em áreas comuns escuras, como escadas, corredores e garagens. Nessas situações, a comunicação e segurança ficam comprometidas.

## 🎯 Objetivo
Criar uma forma prática, offline e acessível para **ativar luzes de emergência por meio de um gesto** reconhecido pelas câmeras de segurança do condomínio, que funcionam com **bateria auxiliar mesmo durante falhas de energia**.

## 🧠 Como funciona
- A câmera capta o gesto de **cruzar os braços em "X"**.
- O sistema identifica o movimento usando a biblioteca `MediaPipe`.
- O status de emergência é alternado: `LIGADA` 🔋 ou `DESLIGADA` 💡.
- O texto é exibido com a fonte **Montserrat Bold** via `Pillow`, com destaque de cor.

## 🖥️ Tecnologias Utilizadas
- Python 3
- OpenCV
- MediaPipe
- Pillow (PIL)
- Fonte personalizada: Montserrat-Bold.ttf

## ▶️ Demonstração em vídeo
📺 [Assista ao vídeo do projeto (YouTube)](https://youtu.be/jFLPrRHiGgI)

## 📦 Repositório:

https://github.com/brunoventuri01/GS-PYSHICAL-COMPUTING.git


> ⚠️ Certifique-se de ter o arquivo `Montserrat-Bold.ttf` na mesma pasta do código.

## 👥 Integrantes

- **Bruno Venturi Lopes Vieira** – RM99431  
- **Leonardo de Oliveira Ruiz** – RM98901

---

Desenvolvido para a disciplina de **Physical Computing IOT** – Global Solution 2025 | FIAP
