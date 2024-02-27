import cv2

def transfor_drawing(arquivo,qtd_filter):
    img = cv2.imread(f"img/{arquivo}")
    img_pb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_inverted = cv2.bitwise_not(img_pb)
    image_blur = cv2.GaussianBlur(image_inverted,(qtd_filter,qtd_filter), 0)
    image_blur_inverted = cv2.bitwise_not(image_blur)
    image_drawing = cv2.divide(img_pb,image_blur_inverted, scale=256.0)

    cv2.imwrite(f"img_tratado/{arquivo}",image_drawing)

transfor_drawing("totoro.jpg", 51)