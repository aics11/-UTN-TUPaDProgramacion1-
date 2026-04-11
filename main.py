
import mss
import numpy as np
import cv2

print("Poker Coach - Zonas (ESC para salir)")

with mss.mss() as sct:
    monitor = sct.monitors[1]

    # Región grande que ya ajustaste
    region = {
        "top": 200,
        "left": 200,
        "width": 1200,
        "height": 700
    }

    while True:
        screenshot = sct.grab(region)
        img = np.array(screenshot)

        # =========================
        # ZONAS (POSICIONES EJEMPLO)
        # =========================

        # Cartas del jugador
        carta1 = (490, 600, 80, 120)  # x, y, w, h
        carta2 = (580, 600, 80, 120)
        
        x, y, w, h = carta1
        carta1_img = img[y:y+h, x:x+w]

        cv2.imshow("Carta 1", carta1_img)


        # Cartas de la mesa
        flop1 = (350, 300, 80, 120)
        flop2 = (440, 300, 80, 120)
        flop3 = (530, 300, 80, 120)
        turn  = (620, 300, 80, 120)
        river = (710, 300, 80, 120)

        zonas = [carta1, carta2, flop1, flop2, flop3, turn, river]

        # Dibujar rectángulos
        for (x, y, w, h) in zonas:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Poker Coach - Zonas", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cv2.destroyAllWindows()

