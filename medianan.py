def filtro_mediana(_img, janela=3):
    img = _img.copy()
    M = img.width
    N = img.height
    borda = janela/2
    for i in range(borda,M-borda):
        for j in range(borda,N-borda):
            try:
                img.getpixel((i,j))
                img.putpixel((i,j), (0,0,0))
            except:
                pass
    return img


img = Image.open('morfologia.png')
filtro_mediana(img)
img.show()
