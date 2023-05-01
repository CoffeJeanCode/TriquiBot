import cv2

class Camera:
  def __init__(self):
    self.currentImage = None
    self.capture = None
    self.idxPhoto = 0

    self.capture = cv2.VideoCapture(0)

  def takePhoto(self, filename):

    if not self.capture.isOpened():
        raise IOError("No se pudo abrir la cámara")
    
    ret, frame = self.capture.read()
    

    if not ret:
        raise RuntimeError("No se pudo capturar una imagen")
    
    filenameWithId = f"plays/{filename}_{self.idxPhoto}.jpg"
    
    cv2.imwrite(filenameWithId, frame)


    self.currentImage = cv2.imread(filenameWithId)
    self.idxPhoto += 1

  def cropImage(self):
    height, width, channels = self.currentImage.shape

    h = int(height)
    w = int(width)

    return self.currentImage[int(h/2 - h/4) : int(h/2 + h/4), int(w/2 - h/4) : int(w/2 + h/4)]

  def generateCells(self):
    image = self.cropImage()
    height, width, channels = image.shape
    cells = []
    
    cv2.waitKey(0)

    widthToRect = int(width / 3)


    # Creamos una máscara rectangular y la mostramos.
    for i in range(0, width, widthToRect):
        for j in range(0, width, widthToRect):
          
          # Elegimos el umbral de rojo en HSV        
          # hacemos la mask y filtramos en la original
          masked = image[j + 10 : j + widthToRect - 10, i + 10 : i + widthToRect - 10]
          img_hsv = cv2.cvtColor(masked, cv2.COLOR_RGB2HSV)
          
          mask1 = cv2.inRange(img_hsv, (0, 0, 0), (255,255,100))

          cells.append(mask1)

    return cells