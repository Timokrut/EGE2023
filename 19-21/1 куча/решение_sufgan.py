# программа для заданий 19-21

# Ты это сам писал или с сайта скопировал, я для тик тока комменты устаю писать а ты все вообще написал

# Пример - https://inf-ege.sdamgia.ru/test?id=13325843
# Правила:
#
# Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят 
# по очереди, первый ход делает Петя. За один ход игрок может
#
# добавить в кучу один камень или
# добавить в кучу два камня или
# увеличить колочество камней в куче в два раза.
#
# Например, имея кучу из 10 камней, за один ход можно получить кучу из 11, 12 или 20 камней. 
# У каждого игрока, чтобы делать ходы, есть неограниченное количество камней.
#
# Игра завершается в тот момент, когда количество камней в куче превышает 41. Победителем считается 
# игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 42 или больше камней.
#
# В начальный момент в куче было S камней, 1 ≤ S ≤ 41.

# ВАЖНАЯ ИНФОРМАЦИЯ
# ходы: +1; +2; *2
# первый ходит Петя
# 1 ≤ S ≤ 41
# если S > 41, то победитель - тот кто положил последний камень


def f(x, s, n=0): # x - это тот, чей ход мы ищем(первый Васин, ...); s - сумма; n - номер итерации(или хода(как 'x'))
    if s >= 42: # зависит от правил
        return n%2 == x%2 # при s вышедшем за значения, мы проверяем, ходил ли последним тот, чей ход мы ждем(сравниваем четность)
    if n >= x: return False # убирает итерации, в которых номер хода вышел за пределы ожидаемого

    ls = [f(x, s+1, n+1), f(x, s+2, n+1), f(x, s*2, n+1)] # здесь мы пишеем все возможные ходы
    return any(ls) if (n+1)%2 == x%2 else all(ls)# если следующий ходит тот, кого мы ожидаем, то если любой из его ходов будет выигрышным, то он так и поступит, значит используем any, если же ходит противник, то у нас есть шанс успеха, только в случае, если все его ходы не могут быть выигрышными, поэтому используем all


for s in range(1, 41+1): # рамки зависят от ограничения S
    for x in range(1, 4+1): # это номер хода: 1 - первый Пети; 2 - первый Васи; 3 - второй Пети и тд, больше 4 не берем, так как максимально нас спрашивают о 2 ходе Васи
        if f(x, s): # дословно: может ли Вася/Петя за первый/второй ход(зависит от х) с вероятностью 100% выиграть при таком S
            print(x, ' --> ', s)
            break

# ниже приложен результат работы программы

# ЗАДАНИЯ
# Задание 19:
# Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах 
# противника. Описать стратегию игрока  — значит, описать, какой ход он должен сделать в любой 
# ситуации, которая ему может встретиться при различной игре противника. В описание выигрышной 
# стратегии не следует включать ходы следующего стратегии игрока, которые не являются для него 
# безусловно выигрышными.
# Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите 
# минимальное значение S, когда такая ситуация возможна.
# 
# Такое задание к сожалению с помощью программы решить нельзя
# поэтому рассуждаем логически
# максмальный прирост в сумме получится при двойном умножении на 2(*2)
# минимальное выигышное значение s = 42, значит допустим, что до хода васи после пети получилось 21, значит у пети было или 19 или 20 камней
# если пробовать двойное умножение(попробовать разделить конечную сумму на 2*2(4)), то можем получить цепочку 44 <-- 22 <-- 11, 11 и является нашим ответом
# Ответ: 11

# Задание 20
# Найдите три таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно 
# выполняются два условия:
# — Петя не может выиграть за один ход;
# — Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
# Найденные значения запишите в ответе в порядке возрастания без разделительных знаков
# 
# Такую задачу мы решить уже можем
# Для ее решения нам нужно найти х = 3, так как это соответствует второму ходу Пети
# эти х возникают только при значениях суммы [10, 18, 19]
# Ответ: 101819

# Задание 21
# Найдите минимальное значение S, при котором одновременно выполняются два условия:
# — у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# — у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
# 
# Для решения, нам необходимо лишь найти х = 4, соответствующий второму ходу Васи
# При этом х сумма = 17
# Ответ: 17


# output:
# 3  -->  10 (20)
# 4  -->  17 (21)
# 3  -->  18 (20)
# 3  -->  19 (20)
# 2  -->  20 
# 1  -->  21
# 1  -->  22
# 1  -->  23
# 1  -->  24
# 1  -->  25
# 1  -->  26
# 1  -->  27
# 1  -->  28
# 1  -->  29
# 1  -->  30
# 1  -->  31
# 1  -->  32
# 1  -->  33
# 1  -->  34
# 1  -->  35
# 1  -->  36
# 1  -->  37
# 1  -->  38
# 1  -->  39
# 1  -->  40
# 1  -->  41

