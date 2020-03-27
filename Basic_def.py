# 함수를 만들어 보자

# def grees(lang):              # def로 정의하여 grees() 함수를 만든 것
#     if lang == 'es' :
#         print('hola')
#     elif lang =='fr' :
#         print('Bonjour')
#     else:
#         print('hello')


   #.grees() 함수를 만들어 실행한 것
# grees('es')
# grees('en')
# grees('fr')
#


#
# print('==============================')
#
# print(grees('es'), 'bob')
# print(grees('en'), 'bodfb')
# print(grees('fr'), 'dsjfkls')


def grees(lang):             #. grees() 함수 값을 고정값으로 할당
    if lang == 'es' :
        return 'hola'
    elif lang =='fr' :
        return 'Bonjour'
    else:
        return 'hello'

grees('es')
grees('en')
grees('fr')

