import cv2
import os,time

camera = cv2.VideoCapture(0)

while True:
    ret , image=camera.read()
    
    
    if ret:
        cv2.imshow("camera",image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # convertir de RGGB vers gray
        cv2.imshow("grayimage", gray)
        #convertir de RGB vers YUV
        gr=cv2.cvtColor(image,cv2.COLOR_RGB2YUV)
        cv2.imshow("autre", gr)
        # appliquer un filtre median
        blur = cv2.medianBlur(image,15)
        # applique un filtre gaussien 
        #Flou d'image (lissage d'image) est Le flou de l'image est obtenu en convoluant l'image avec un noyau de filtre passe-bas.
        #C'est utile pour supprimer le bruit. Il supprime en fait le contenu haute fréquence (par exemple: bruit, contours) de l'image.
        # Ainsi, les bords sont un peu flous dans cette opération (il existe également des techniques de flou qui ne brouillent pas les bords)
        
        gauss = cv2.GaussianBlur(image,(5,5),0)
        flou = cv2.bilateralFilter(image, 9,75,75)
        cv2.imshow("camera blur", blur)
        #cv2.imshow("gaussian blur", gauss)
        cv2.imshow("flou",flou)
        # modifier la dimensionde l'image hauteur/laegeur
        im1 = cv2.resize(image, (200,300))
        im2 = cv2.resize(gray,(240,240))
        im3 =cv2.resize(gauss,(240,240))
        #cv2.imshow("dimension1",im1)
        #cv2.imshow("dimension2",im2)
        #cv2.imshow("dimension3",im3)
        print(im1.shape)
        #cv2.imwrite('image' + time.strftime("%Y-%m-%d") + '.png', image)
    if cv2.waitKey(1) & 0xff ==ord('a'):
        break
    
    
camera.release()

cv2.destroyAllWindows()
