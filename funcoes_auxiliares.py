def teletransporte_cobra(x, y, largura, altura, tamanho):
    if x > largura:
        x = 0
        return x
    elif x < 0:
        x = largura-tamanho
        return x
    if y > altura:
        y = 0
        return y
    elif y < 0:
        y = altura - tamanho
        return y
