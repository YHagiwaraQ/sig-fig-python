#xの少数部分の桁を取り出す
def strf(x):
    return str(abs(x)).split('.')[1]
#xの整数部分の桁を取り出す
def stri(x):
    return str(float(x)).split('.')[0]

#xの有効桁数を計算する（正確には返り値は有効数字−１）
def sd(x):
    if x < 1:
        lsx = list(strf(x))
        for i in range(len(lsx)):
            if lsx[i] != "0":
                return len(lsx)-i
                break
    else:
        return sum(i.isdigit() for i in str(x))

#有効数字を考慮して掛け算を行う
def mul(a,b):
    s = a*b
    sd_ab = min(sd(a),sd(b))
    if s < 1:
        
        lss = list(strf(s))
        for i in range(len(lss)):
            if lss[i] != "0":
                re =round(s*(10**(i+sd_ab)))/(10**(i+sd_ab))
                return re
    else:
        re =round(s*(10**(sd_ab-len(stri(s)))))/(10**(sd_ab-len(stri(s))))
        return re
    
#有効数字を考慮して割り算を行う
def div(a,b):
    s = a/b
    sd_ab = min(sd(a),sd(b))
    if s < 1:
        
        lss = list(strf(s))
        for i in range(len(lss)):
            if lss[i] != "0":
                re =round(s*(10**(i+sd_ab)))/(10**(i+sd_ab))
                return re
    else:
        re =round(s*(10**(sd_ab-len(stri(s)))))/(10**(sd_ab-len(stri(s))))
        return re
    
#xの有効桁位を計算する
def ed(x):
        return len(strf(x))
#有効数字を考慮して引き算を行う
def add(a,b):
    s = a + b
    ed_ab = min(ed(a),ed(b))
    re = round(s*(10**ed_ab))/(10**ed_ab)
    return re
#有効数字を考慮して足し算を行う
def sub(a,b):
    s = a - b
    ed_ab = min(ed(a),ed(b))
    re = round(s*(10**ed_ab))/(10**ed_ab)
    return re
#指定した有効数字で数字を丸める
def deci(n,x):
    if n < 1:
            ls = list(strf(n))
            for i in range(len(ls)):
                if ls[i] != "0":
                    re =round(n*(10**(i+x)))/(10**(i+x))
                    return re
    else:
        re =round(n*(10**(x-len(stri(n)))))/(10**(x-len(stri(n))))
        return re
