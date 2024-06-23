import cv2
from cvzone.HandTrackingModule import HandDetector

#Inicialização da Webcam
#Somente a Inicialização não irá abrir a tela de POP-UP dela
webcam = cv2.VideoCapture(0)

#Inicialização do Rastreador de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

#Verificação se conseguiu abrir a Webcam
while True:
    #Captura da Imagem da WebCam
    sucesso, imagem = webcam.read()

    #Detecção de Mão
    hands, imagem_maos = rastreador.findHands(imagem)

    #Consideração importante, acentos no titulo da tela trava o sistema
    #Mostar a tela tipo "POP-UP" com video da webcam e marcação das mãos
    cv2.imshow("Projeto - IA", imagem_maos)

    #Finalização da tela da câmera ao apertar qualquer tecla do teclado
    if cv2.waitKey(1) != -1:
        break
    
#Libera a câmera e fecha a janela
webcam.release()
cv2.destroyAllWindows()