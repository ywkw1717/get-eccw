#!/usr/bin/env python
# -*- coding: utf-8 -*-
# エラー訂正コード語を求めるスクリプト

import sympy as sy
import re

# symbolとして使う変数の宣言
x = sy.Symbol('x')
a = sy.Symbol('a')

# 正規表現パターン
pattern = "a\*+[0-9]+"
repatter = re.compile(pattern)

a_pattern = "a\*x"
a_repatter = re.compile(a_pattern)

# ガロア体 GF(2**8) α の指数と整数の対応
a_table = [1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38,
           76, 152, 45, 90, 180, 117, 234, 201, 143, 3, 6, 12, 24, 48, 96,
           192, 157, 39, 78, 156, 37, 74, 148, 53, 106, 212, 181, 119, 238,
           193, 159, 35, 70, 140, 5, 10, 20, 40, 80, 160, 93, 186, 105, 210,
           185, 111, 222, 161, 95, 190, 97, 194, 153, 47, 94, 188, 101, 202,
           137, 15, 30, 60, 120, 240, 253, 231, 211, 187, 107, 214, 177, 127,
           254, 225, 223, 163, 91, 182, 113, 226, 217, 175, 67, 134, 17, 34,
           68, 136, 13, 26, 52, 104, 208, 189, 103, 206, 129, 31, 62, 124, 248,
           237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204, 133, 23, 46,
           92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84, 168, 77,
           154, 41, 82, 164, 85, 170, 73, 146, 57, 114, 228, 213, 183, 115,
           230, 209, 191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246,
           241, 255, 227, 219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220,
           165, 87, 174, 65, 130, 25, 50, 100, 200, 141, 7, 14, 28, 56, 112,
           224, 221, 167, 83, 166, 81, 162, 89, 178, 121, 242, 249, 239, 195,
           155, 43, 86, 172, 69, 138, 9, 18, 36, 72, 144, 61, 122, 244, 245,
           247, 243, 251, 235, 203, 139, 11, 22, 44, 88, 176, 125, 250, 233,
           207, 131, 27, 54, 108, 216, 173, 71, 142, 1]


# 訂正コード語数より、gを求める関数
def G(ec_words):
    if ec_words == "7":
        return x**7 + (a**87 * x**6) + (a**229 * x**5) + (a**146 * x**4) + \
               (a**149 * x**3) + (a**238 * x**2) + (a**102 * x) + a**21
    elif ec_words == "10":
        return x**10 + (a**251 * x**9) + (a**67 * x**8) + (a**46 * x**7) + \
               (a**61 * x**6) + (a**118 * x**5) + (a**70 * x**4) + \
               (a**64 * x**3) + (a**94 * x**2) + (a**32 * x) + a**45
    elif ec_words == "13":
        return x**13 + (a**74 * x**12) + (a**152 * x**11) + \
               (a**176 * x**10) + (a**100 * x**9) + (a**86 * x**8) + \
               (a**100 * x**7) + (a**106 * x**6) + (a**104 * x**5) + \
               (a**130 * x**4) + (a**218 * x**3) + (a**206 * x**2) + \
               (a**140 * x) + a**78
    elif ec_words == "16":
        return x**16 + (a**120 * x**15) + (a**104 * x**14) + \
               (a**107 * x**13) + (a**109 * x**12) + (a**102 * x**11) + \
               (a**161 * x**10) + (a**76 * x**9) + (a**3 * x**8) + \
               (a**91 * x**7) + (a**191 * x**6) + (a**147 * x**5) + \
               (a**169 * x**4) + (a**182 * x**3) + (a**194 * x**2) + \
               (a**225 * x) + a**120
    elif ec_words == "17":
        return x**17 + (a**43 * x**16) + (a**139 * x**15) + \
               (a**206 * x**14) + (a**78 * x**13) + (a**43 * x**12) + \
               (a**239 * x**11) + (a**123 * x**10) + (a**206 * x**9) + \
               (a**214 * x**8) + (a**147 * x**7) + (a**24 * x**6) + \
               (a**99 * x**5) + (a**150 * x**4) + (a**39 * x**3) + \
               (a**243 * x**2) + (a**163 * x) + a**136
    elif ec_words == "18":
        return x**18 + (a**215 * x**17) + (a**234 * x**16) + \
               (a**158 * x**15) + (a**94 * x**14) + (a**184 * x**13) + \
               (a**97 * x**12) + (a**118 * x**11) + (a**170 * x**10) + \
               (a**79 * x**9) + (a**187 * x**8) + (a**152 * x**7) + \
               (a**148 * x**6) + (a**252 * x**5) + (a**179 * x**4) + \
               (a**5 * x**3) + (a**98 * x**2) + (a**96 * x) + a**153
    elif ec_words == "22":
        return x**22 + (a**210 * x**21) + (a**171 * x**20) + \
               (a**247 * x**19) + (a**242 * x**18) + (a**93 * x**17) + \
               (a**230 * x**16) + (a**14 * x**15) + (a**109 * x**14) + \
               (a**221 * x**13) + (a**53 * x**12) + (a**200 * x**11) + \
               (a**74 * x**10) + (a**8 * x**9) + (a**172 * x**8) + \
               (a**98 * x**7) + (a**80 * x**6) + (a**219 * x**5) + \
               (a**134 * x**4) + (a**160 * x**3) + (a**105 * x**2) + \
               (a**165 * x) + a**231
    elif ec_words == "24":
        return x**24 + (a**229 * x**23) + (a**121 * x**22) + \
               (a**135 * x**21) + (a**48 * x**20) + (a**211 * x**19) + \
               (a**117 * x**18) + (a**251 * x**17) + (a**126 * x**16) + \
               (a**159 * x**15) + (a**180 * x**14) + (a**169 * x**13) + \
               (a**152 * x**12) + (a**192 * x**11) + (a**226 * x**10) + \
               (a**228 * x**9) + (a**218 * x**8) + (a**111 * x**7) + \
               x**6 + (a**117 * x**5) + (a**232 * x**4) + (a**87 * x**3) + \
               (a**96 * x**2) + (a**227 * x) + a**21


# 係数より、実際にfを求める関数
def F(coefficient, section):
    f = 0
    for i in range(len(coefficient)):
        f += coefficient[i] * x**section
        section -= 1
    return f

# fの項の数を求める関数(総コード語数)
# def F_section(ec_words):
#     if ec_words == "7" or ec_words == "10" or ec_words == "13" or ec_words == "17":
#         return 25
#     elif ec_words == "16" or ec_words == "22":
#         return 34
#     elif ec_words == "18":
#         return 32


# 指数から整数へ変換
def convert_exponent_into_integer(func):
    # a_match = a_repatter.findall(str(func))
    # if a_match:
        # func = re.sub(a_pattern, "a**1*x", str(func))
        # func = func.replace(a+"*"+x, a+"**1*"+x)
        # for i in range(len(a_match)):
        #     func = func.replace(a_match[i], a**1*x)
        # print type(func)
        # print func
        # print a_match

    match = repatter.findall(str(func))
    if match:
        exponent = "".join(match).split("a**")
        exponent = exponent[1:]
        for i in range(len(match)):
            if int(exponent[i]) > 255:
                exponent[i] = int(exponent[i]) % 255
            # replaceするので式の順番はめちゃくちゃでも良い
            func = func.replace(match[i], a_table[int(exponent[i])])
        return func


# 引数に与えた関数の最初の項に対応するaの値を返す
def get_a_exponent(func):
    first_coefficient = str(func).split(' ')
    first_coefficient = first_coefficient[0].split('*')

    # 最初の項が1だと、first_coefficient[0]にxが入ってしまい、invalid literalを返されてしまうため
    if first_coefficient[0] == 'x':
        exponent = a_table.index(1)
    else:
        if int(first_coefficient[0] == 1000):
            exponent = a_table.index(1)
        else:
            exponent = a_table.index(int(first_coefficient[0]))

    return exponent


# 多項式の割り算
def div_func(f, g, div_num, section, ec_words):
    count = 1
    for i in range(div_num + 1):
        next_coefficient = []
        section -= 1

        g = G(ec_words)
        g *= a**get_a_exponent(f) * x**(div_num - i)
        g = sy.expand(g)  # 多項式の展開
        g = convert_exponent_into_integer(g)
        print "[ " + str(count) + " ]"
        print "g(x) = ", g

        # 係数のみを取り出す
        f_coefficient = "".join(str(f)).split(" + ")
        for i in range(len(f_coefficient)):
            word_1 = f_coefficient[i].find("*x**")
            word_2 = f_coefficient[i].find("*x")
            word_3 = f_coefficient[i].find("x**")
            if word_1 != -1:
                f_coefficient[i] = f_coefficient[i][:word_1]
            elif word_2 != -1:
                f_coefficient[i] = f_coefficient[i][:word_2]
            elif word_3 != -1:
                f_coefficient[i] = "1"
            elif f_coefficient[i] == "x":
                f_coefficient[i] = "1"

        g_coefficient = "".join(str(g)).split(" + ")
        for i in range(len(g_coefficient)):
            word_1 = g_coefficient[i].find("*x**")
            word_2 = g_coefficient[i].find("*x")
            word_3 = g_coefficient[i].find("x**")
            if word_1 != -1:
                g_coefficient[i] = g_coefficient[i][:word_1]
            elif word_2 != -1:
                g_coefficient[i] = g_coefficient[i][:word_2]
            elif word_3 != -1:
                g_coefficient[i] = "1"
            elif g_coefficient[i] == "x":
                g_coefficient[i] = "1"

        # print "f_coefficient = ", f_coefficient
        # print "g_coefficient = ", g_coefficient
        # for i in range(len(g_coefficient)):
        #     print g_coefficient[i],
        if (len(f_coefficient) > len(g_coefficient)):
            for i in range(len(g_coefficient)):
                if int(f_coefficient[i]) == 1000:
                    xor = 0 ^ 2 if g_coefficient[i] == "a" else 0 ^ int(g_coefficient[i])
                else:
                    xor = int(f_coefficient[i]) ^ 2 if g_coefficient[i] == "a" else int(f_coefficient[i]) ^ int(g_coefficient[i])
                next_coefficient.append(xor)
        else:
            for i in range(len(f_coefficient)):
                if int(f_coefficient[i]) == 1000:
                    xor = 0 ^ 2 if g_coefficient[i] == "a" else 0 ^ int(g_coefficient[i])
                else:
                    xor = int(f_coefficient[i]) ^ 2 if g_coefficient[i] == "a" else int(f_coefficient[i]) ^ int(g_coefficient[i])
                next_coefficient.append(xor)

        next_coefficient = next_coefficient[1:]
        add = len(f_coefficient)
        del g_coefficient[0:add]
        for i in range(len(g_coefficient)):
            next_coefficient.append(int(g_coefficient[i]))

        # print next_coefficient
        f = 0
        for i in range(len(next_coefficient)):
            # 係数が０の時は項と掛け算されて消えてしまう 係数０として後々のxorをさせたいので条件分岐
            if next_coefficient[i] == 0:
                f += 1000 * x**(section - i)
            else:
                f += next_coefficient[i] * x**(section - i)

        print "f(x) = ", f
        print "-------------------------------------------------------"
        count += 1

    answer = "".join(str(f)).split(" + ")
    for i in range(len(answer)):
        word_1 = answer[i].find("*x**")
        word_2 = answer[i].find("*x")
        word_3 = answer[i].find("x**")
        if word_1 != -1:
            answer[i] = answer[i][:word_1]
        elif word_2 != -1:
            answer[i] = answer[i][:word_2]
        elif word_3 != -1:
            answer[i] = "1"
        elif answer[i] == "x":
            answer[i] = "1"

    return answer


if __name__ == "__main__":
    ec_words_list = []  # エラー訂正コード語数
    all_code_words_list = []  # 総コード語数
    coefficient_list = []  # データコードを係数とした多項式f(x)を求めるための係数
    ans_list = []

    rs_block = input('rs_block > ')  # RSブロック数

    for i in range(rs_block):
        print "[ " + str(i + 1) + " ]"

        ec_words_list.append(raw_input('ec_code_words > '))
        while ec_words_list[i] == '':
            ec_words_list.pop(i)
            ec_words_list.append(raw_input('ec_code_words > '))

        all_code_words_list.append(input('all_code_words > '))
        while all_code_words_list[i] == '':
            all_code_words_list.pop(i)
            all_code_words_list.append(input('all_code_words > '))

        coefficient_list.append(raw_input('coefficient > '))
        while coefficient_list[i] == '':
            coefficient_list.pop(i)
            coefficient_list.append(raw_input('coefficient > '))

        all_code_words_list[i] -= 1  # 一時的な処置

    for i in range(rs_block):
        coefficient = str(coefficient_list[i]).split(' ')
        coefficient = map(int, coefficient)  # リストの要素を全てint型に変換
        section = all_code_words_list[i]
        f = F(coefficient, section)
        g = G(ec_words_list[i])

        print "\n\n-------------------------------------------------------"
        print "f(x) = " + str(f)
        print "g(x) = " + str(convert_exponent_into_integer(g))
        print "-------------------------------------------------------"

        div_num = section - int(ec_words_list[i])  # 除算を行う回数
        ans_list.append(div_func(f, g, div_num, section, ec_words_list[i]))

    for i in range(rs_block):
        print "\n\n\nR" + str(i + 1) + "(x) Coefficient =",
        for j in range(len(ans_list[i])):
            print ans_list[i][j],

    if rs_block == 2:
        print "\n\n\nanswer = ",
        ans_bin = []
        tmp1 = ans_list[0]
        tmp2 = ans_list[1]

        for i in range(len(tmp1)):
            ans_bin.append(tmp1[i])
            ans_bin.append(tmp2[i])
            print tmp1[i], tmp2[i],

        ans_bin = map(int, ans_bin)
        ans_bin = map(bin, ans_bin)
        print "\n\n\nanswer_binary_version = ",

        for i in range(len(ans_bin)):
            print ans_bin[i][2:].zfill(8),  # 8桁で統一
