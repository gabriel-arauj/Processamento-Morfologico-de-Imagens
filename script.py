from PIL import Image

def filtro_mediana(_img, janela_m=3, janela_n=3):
    img = _img.copy()
    M = img.width
    N = img.height
    m = janela_m//2
    n = janela_n//2
    for i in range(m,M-m):
        for j in range(n,N-n):
            lista = []
            # percorrer mascara
            for x in range(i-m, i+m+1):
                for y in range(j-n, j+n+1):
                    lista.append(_img.getpixel((x,y)))
            lista = sorted(lista)
            pixel = lista[len(lista)//2]
            img.putpixel((i,j), pixel)
                        
    return img


def filtro_minima(_img, janela_m=3, janela_n=3):
    img = _img.copy()
    M = img.width
    N = img.height
    m = janela_m//2
    n = janela_n//2
    for i in range(m,M-m):
        for j in range(n,N-n):
            lista = []
            # percorrer mascara
            for x in range(i-m, i+m+1):
                for y in range(j-n, j+n+1):
                    lista.append(_img.getpixel((x,y)))
            lista = sorted(lista)
            pixel_color = lista[0]
            img.putpixel((i,j), pixel_color)
                        
    return img

class ElementoEstruturante:
    def __init__(self, f, ancora=None): 
        '''
        f = matriz contendo o elemento estruturante 
        [
            [x,x,x],
            [x,x,x],
            [x,x,x],
        ]
        ancora = ponto de ancoragem do elemento estruturante. Se vazia o ponto de ancora será o ponto central
        (linha,coluna)
        '''
        self.f = f
        self.m = len(f[0])
        self.n = len(f)
        if ancora:
            self.ancora = {
                'x': ancora[0],
                'y': ancora[1],
            }
        else:
            self.ancora = {
                'x': self.n//2,
                'y': self.m//2,
            }
        self.f_ancora = f[self.ancora['x']][self.ancora['y']]



def hit(img, elemento_estruturante, ponto):
    es_m = elemento_estruturante.m # colunas
    es_n = elemento_estruturante.n # linhas
    M = img.width # colunas
    N = img.height # linhas
    x = ponto[1] - elemento_estruturante.ancora['x'] # linha
    for linhas in elemento_estruturante.f:
        y = ponto[0] - elemento_estruturante.ancora['y'] # coluna
        for el in linhas:
            if not el:
                y+=1
                continue
            if x < 0 or y < 0 or x >= N or y >= M:
                return False
            #print(img.getpixel((y,x)), end=",")
            if el != img.getpixel((y,x)):
                return False
            y+=1
        #print('')
        x+=1
    return True


def erosao(_img, elemento_estruturante, pixel):
    img = _img.copy()
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            #print(f"{i}{j}", end=",")
            if hit(_img, elemento_estruturante, (j,i)):
                img.putpixel((j,i), pixel)
            else:
                img.putpixel((j,i), (255,255,255))
            #print(img.getpixel((j,i)), end=",")
        #print('')
        
    return img




def find(img, elemento_estruturante, ponto):
    es_m = elemento_estruturante.m # colunas
    es_n = elemento_estruturante.n # linhas
    M = img.width # colunas
    N = img.height # linhas
    x = ponto[1] - elemento_estruturante.ancora['x'] # linha
    found = []
    for linhas in elemento_estruturante.f:
        y = ponto[0] - elemento_estruturante.ancora['y'] # coluna
        for el in linhas:
            if not el:
                y+=1
                continue
            if x < 0 or y < 0 or x >= N or y >= M:
                y+=1
                continue
            found.append((y,x))
            y+=1
        x+=1
    return found


def dilatacao(_img, elemento_estruturante, pixel):
    img = _img.copy()
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            if _img.getpixel((j,i)) == elemento_estruturante.f_ancora:
                for ponto in find(_img, elemento_estruturante, (j,i)):
                    img.putpixel(ponto, pixel)
        
    return img
    

def complemento(_img):
    img = _img.copy()
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            pixel = _img.getpixel((j,i))
            complement = tuple(map(int.__sub__, (255,255,255), pixel))
            img.putpixel((j,i), complement)
    return img

def uniao(_img1,_img2):
    img = _img1.copy()
    if _img1.width != _img2.width or _img1.height != _img2.height:
        raise Exception('As imagens devem ter o mesmo tamanho')
        return
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            pixel1 = _img1.getpixel((j,i))
            pixel2 = _img2.getpixel((j,i))
            img.putpixel((j,i), min(pixel1,pixel2))
    return img


def intersecao(_img1,_img2):
    img = _img1.copy()
    if _img1.width != _img2.width or _img1.height != _img2.height:
        raise Exception('As imagens devem ter o mesmo tamanho')
        return
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            pixel1 = _img1.getpixel((j,i))
            pixel2 = _img2.getpixel((j,i))
            img.putpixel((j,i), max(pixel1,pixel2))
    return img

def diferenca(_img1,_img2):
    img = _img1.copy()
    if _img1.width != _img2.width or _img1.height != _img2.height:
        raise Exception('As imagens devem ter o mesmo tamanho')
        return
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            pixel1 = _img1.getpixel((j,i))
            pixel2 = _img2.getpixel((j,i))
            if pixel2 < (255,255,255):
                img.putpixel((j,i), (255,255,255))
    return img


def hitRGB(img, elemento_estruturante, ponto):
    M = img.width # colunas
    N = img.height # linhas
    x = ponto[1] - elemento_estruturante.ancora['x'] # linha
    for linhas in elemento_estruturante.f:
        y = ponto[0] - elemento_estruturante.ancora['y'] # coluna
        for el in linhas:
            if not el:
                y+=1
                continue
            if x < 0 or y < 0 or x >= N or y >= M:
                return False
            if not el or img.getpixel((y,x)) == (255,255,255):
                return False
            y+=1
        x+=1
    return True


def erosaoRGB(_img, elemento_estruturante):
    img = _img.copy()
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            if hitRGB(_img, elemento_estruturante, (j,i)):
                img.putpixel((j,i), img.getpixel((j,i)))
            else:
                img.putpixel((j,i), (255,255,255))
    return img


def abertura(_img, elemento_estruturante, pixel):
    img = _img.copy()
    img = erosao(img, elemento_estruturante, pixel)
    img = dilatacao(img, elemento_estruturante, pixel)
    return img

def fechamento(_img, elemento_estruturante, pixel):
    img = _img.copy()
    img = dilatacao(img, elemento_estruturante, pixel)
    img = erosao(img, elemento_estruturante, pixel)
    return img

def preenche_buraco(_img, elemento_estruturante, pixel, ponto_inicial):
    img = _img.copy()
    new_img = Image.new('RGB',(img.width, img.height), (255,255,255))
    ponto = (ponto_inicial[1], ponto_inicial[0])
    new_img.putpixel(ponto, pixel)
    img_c = complemento(img)

    img = dilatacao(new_img, elemento_estruturante, pixel)
    img = intersecao(img, img_c)
    while img != new_img:
        new_img = img.copy()
        img = dilatacao(new_img, elemento_estruturante, pixel)
        img = intersecao(img, img_c)
    return uniao(img, _img)

def trocar_cor(_img, pixel_original, pixel_novo):
    img = _img.copy()
    M = img.width
    N = img.height
    for i in range(N):
        for j in range(M):
            if _img.getpixel((j,i)) == pixel_original:
                img.putpixel((j,i), pixel_novo)
            else:
                img.putpixel((j,i), (255,255,255))
    return img


def hit_or_miss(_img, D):
    img = _img.copy()
    m = (D.m+2)
    n = (D.n+2)
    W = [[(0,0,0)]*m for l in range(n)]

    for l in range(n-2)[::-1]:
        for c in range(m-2)[::-1]:
            if D.f[l][c] == None:
                W[l+1][c+1] = None
                continue
            W[l+1][c+1] = tuple(map(int.__sub__, (255,255,255),D.f[l][c]))
            if W[l+1][c+1] == (255,255,255):
                W[l+1][c+1] = None
    
    B1 = D
    B2 = ElementoEstruturante(W)
    img_c = complemento(_img)

    img1 = erosao(img, B1, (0,0,0))
    img2 = erosao(img_c, B2, (0,0,0))
    img = intersecao(img1, img2)
    return img

def rotaciona(elemento_estruturante):
    es = elemento_estruturante
    elemento = es.f[es.ancora['x']][es.ancora['y']]
    es.f[es.ancora['x']][es.ancora['y']] = 'a'
    new_es = []
    new_ancora = (es.ancora['x'], es.ancora['y'])
    for c in range(es.m):
        linha = []
        for l in range(es.n)[::-1]:
            linha.append(es.f[l][c])
        new_es.append(linha)
    for i in range(len(new_es)):
        for j in range(len(new_es[i])):
            if new_es[i][j] == 'a':
                new_ancora = (i,j)
                new_es[i][j] = elemento
        #print(new_es[i])
    #print(new_ancora)
    return ElementoEstruturante(new_es, new_ancora)

def fecho_convexo_aux(_img, elemento_estruturante):
    img = _img.copy()
    img = erosao(_img, elemento_estruturante, (0,0,0))
    new_img = uniao(_img, img)

    old_img = _img.copy()
    while old_img != new_img:
        old_img = new_img.copy()
        img = erosao(new_img, elemento_estruturante, (0,0,0))
        new_img = uniao(new_img, img)
    return new_img
    
def fecho_convexo(_img, es1):
    es2 = rotaciona(es1)
    es3 = rotaciona(es2)
    es4 = rotaciona(es3)

    img1 = fecho_convexo_aux(_img,es1)
    img2 = fecho_convexo_aux(_img,es2)
    img3 = fecho_convexo_aux(_img,es3)
    img4 = fecho_convexo_aux(_img,es4)
    img = uniao(uniao(img1, img2), uniao(img3, img4))
    return img
    
def esqueleto(_img, elemento_estruturante):
    img = _img.copy()
    esqueletos =[]
    img_vazio = intersecao(_img, complemento(_img))
    while img != img_vazio:
        img_kb = erosao(img, elemento_estruturante, (0,0,0))
        img_abrt = abertura(img, elemento_estruturante, (0,0,0))
        SkA = diferenca(img, img_abrt)
        esqueletos.append(SkA)
        img = img_kb.copy()
    
    img = img_vazio
    for img_esq in esqueletos:
        img = uniao(img, img_esq)
    return img




def questao_01():
    """
    Eliminar todos os pontos pretos
    """
    img = Image.open('morfologia.png')
    img = filtro_mediana(img,7,7)
    # img = filtro_mediana(img,3,3)
    # img = filtro_mediana(img,3,3)
    # img = filtro_mediana(img,3,3)
    # img = filtro_mediana(img,3,3)
    # img = filtro_mediana(img,3,3)
    img.save("questão_01/questao_01.png")

questao_01()

def questao_02():
    """
    Preencher os buracos dos objetos: magenta, vermelho e verde;
    """
    pixel = pixel_preto = (0,0,0)
    pixel_vermelho = (229,0,28)
    pixel_azul = (48,46,192)
    pixel_verde = (35,166,59)
    pixel_magenta = (144,48,147)
    pixel_vermelho = (229,0,28)
    elemento_estruturante = ElementoEstruturante(
            [
                [pixel,pixel,pixel],
                [pixel,pixel,pixel],
                [pixel,pixel,pixel],
            ],
            (1,1)
        )

    img = Image.open('morfologia.png').convert('RGB')

    img_vermelho = trocar_cor(img, pixel_vermelho, pixel_preto)
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (120,60))
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (138,38))
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (146,61))
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (160,93))
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (100,110))
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (115,130))
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (122,117))
    img_vermelho = preenche_buraco(img_vermelho, elemento_estruturante, pixel, (140,51))
    img_vermelho = trocar_cor(img_vermelho, pixel_preto, pixel_vermelho)
    img_vermelho.save("questão_02/vermelho.png")

    img_verde = trocar_cor(img, pixel_verde, pixel_preto)
    img_verde = preenche_buraco(img_verde, elemento_estruturante, pixel, (20,40))
    img_verde = preenche_buraco(img_verde, elemento_estruturante, pixel, (50,45))
    img_verde = trocar_cor(img_verde, pixel_preto, pixel_verde)    
    img_verde.save("questão_02/verde.png")

    img_magenta = trocar_cor(img, pixel_magenta, pixel_preto)
    img_magenta = preenche_buraco(img_magenta, elemento_estruturante, pixel, (55,118))
    img_magenta = preenche_buraco(img_magenta, elemento_estruturante, pixel, (72,145))
    img_magenta = trocar_cor(img_magenta, pixel_preto, pixel_magenta)    
    img_magenta.save("questão_02/magenta.png")

    img = uniao(img, img_verde)
    img = uniao(img, img_vermelho)
    img = uniao(img, img_magenta)
    img.save("questão_02/questao_02.png")

questao_02()

def questao_03():
    """
    Encontrar o fecho convexo dos objetos: azul, vermelho e verde;
    """
    pixel = pixel_preto = (0,0,0)
    pixel_vermelho = (229,0,28)
    pixel_azul = (48,46,192)
    pixel_verde = (35,166,59)
    pixel_magenta = (144,48,147)
    pixel_vermelho = (229,0,28)
    elemento_estruturante = ElementoEstruturante(
        [
            [pixel,None,None],
            [pixel,(255,255,255),None],
            [pixel,None,None],
        ],
        (1,1)
    )

    img = Image.open('morfologia.png').convert('RGB')

    img_vermelho = trocar_cor(img, pixel_vermelho, pixel_preto)
    img_vermelho = fecho_convexo(img_vermelho, elemento_estruturante)
    img_vermelho = trocar_cor(img_vermelho, pixel_preto, pixel_vermelho)
    img_vermelho.save("questão_03/vermelha.png")
   
    img_azul = trocar_cor(img, pixel_azul, pixel_preto) 
    img_azul = fecho_convexo(img_azul, elemento_estruturante)
    img_azul = trocar_cor(img_azul, pixel_preto, pixel_azul)
    img_azul.save("questão_03/azul.png")
    
    img_verde = trocar_cor(img, pixel_verde, pixel_preto)
    img_verde = fecho_convexo(img_verde, elemento_estruturante)
    img_verde = trocar_cor(img_verde, pixel_preto, pixel_verde)
    img_verde.save("questão_03/verde.png")

    img_magenta = trocar_cor(img, pixel_magenta, pixel_preto)
    img_magenta = fecho_convexo(img_magenta, elemento_estruturante)
    img_magenta = trocar_cor(img_magenta, pixel_preto, pixel_magenta)
    img_magenta.save("questão_03/magenta.png")

    img = uniao(img, img_verde)
    img = uniao(img, img_vermelho)
    img_azul = uniao(img, img_azul)
    img_azul.save("questão_03/juntas_azul.png")
    
    img_magenta = uniao(img, img_magenta)
    img_magenta.save("questão_03/juntas_magenta.png")


questao_03()

def questao_04():
    """
    Utilizando a transformada hit-or-miss, localize cada um dos objetos de cor azul;
    """
    pixel = pixel_preto = (0,0,0)
    pixel_vermelho = (229,0,28)
    pixel_azul = (48,46,192)
    pixel_verde = (35,166,59)
    pixel_magenta = (144,48,147)
    pixel_vermelho = (229,0,28)
    
    img = Image.open('morfologia.png').convert('RGB')
    
    matriz = [ [pixel]*29 for i in range(27)]
    elemento_estruturante = ElementoEstruturante(matriz)
    img_azul1 = trocar_cor(img, pixel_azul, pixel_preto) 
    img_azul1 = hit_or_miss(img_azul1, elemento_estruturante)
    img_azul1.save("questão_04/hit_or_miss1.png")

    matriz = [ [pixel]*19 for i in range(20)]
    elemento_estruturante = ElementoEstruturante(matriz)
    img_azul2 = trocar_cor(img, pixel_azul, pixel_preto) 
    img_azul2 = hit_or_miss(img_azul2, elemento_estruturante)
    img_azul2.save("questão_04/hit_or_miss2.png")

    matriz = [ [pixel]*13 for i in range(14)]
    elemento_estruturante = ElementoEstruturante(matriz)
    img_azul3 = trocar_cor(img, pixel_azul, pixel_preto) 
    img_azul3 = hit_or_miss(img_azul3, elemento_estruturante)
    img_azul3.save("questão_04/hit_or_miss3.png")


    img = uniao(img, img_azul1)
    img = uniao(img, img_azul2)
    img = uniao(img, img_azul3)
    img.save("questão_04/juntas.png")


questao_04()


def questao_05():
    """
    Encontre o esqueleto da imagem de cor vermelha;
    """
    pixel = pixel_preto = (0,0,0)
    pixel_vermelho = (229,0,28)
    pixel_azul = (48,46,192)
    pixel_verde = (35,166,59)
    pixel_magenta = (144,48,147)
    pixel_vermelho = (229,0,28)
    elemento_estruturante = ElementoEstruturante([
                [None,pixel,None],
                [pixel,pixel,pixel],
                [None,pixel,None],
        ])


    img = Image.open('morfologia.png').convert('RGB')

    img_vermelho = trocar_cor(img, pixel_vermelho, pixel_preto)
    img_vermelho = esqueleto(img_vermelho, elemento_estruturante)
    img_vermelho = trocar_cor(img_vermelho, pixel_preto, pixel_vermelho)
    img_vermelho.save("questão_05/vermelha.png")
   

    img = uniao(img, img_vermelho)
    img.save("questão_05/juntas.png")
    


questao_05()

def questao_06():
    """
    Encontre o esqueleto da imagem de cor vermelha;
    """
    pixel = pixel_preto = (0,0,0)
    pixel_vermelho = (229,0,28)
    pixel_azul = (48,46,192)
    pixel_verde = (35,166,59)
    pixel_magenta = (144,48,147)
    pixel_vermelho = (229,0,28)
    
    elemento_estruturante = ElementoEstruturante(
        [
            [pixel,None,None],
            [pixel,(255,255,255),None],
            [pixel,None,None],
        ],
        (1,1)
    )


    img = Image.open('morfologia.png').convert('RGB')

    img_vermelho = trocar_cor(img, pixel_vermelho, pixel_preto)
    img_vermelho_fecho = fecho_convexo(img_vermelho, elemento_estruturante)
    elemento_estruturante = ElementoEstruturante([
                [None,pixel,None],
                [pixel,pixel,pixel],
                [None,pixel,None],
        ])
    img_vermelho = esqueleto(img_vermelho_fecho, elemento_estruturante)
    img_vermelho_fecho = trocar_cor(img_vermelho_fecho, pixel_preto, pixel_vermelho)
   

    img = uniao(img, img_vermelho)
    img = uniao(img, img_vermelho_fecho)
    img.save("questão_06/juntas.png")
    


questao_06()