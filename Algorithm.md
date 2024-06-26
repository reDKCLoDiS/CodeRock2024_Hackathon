# Алгоритм от склада до пункта выдачи
Тут будет представлен алгоритм нахождения пути(любого, кратчайшего или от склада на котором есть товар)
0. Пункт выдачи пользователь выбирает сам в самом начале(это будет сделано так, потому-что кому-то удобно забрать после работы).
1. Выстраивается прямой путь ото всех складов до выбранного пользователем пункта выдачи.
2. Пути приспосабливаются к дорогам, то есть для этого мы на каждом повороте создаём отдельную вершину и у нас получается множество графов.
При каком-то фиксированном отклонении от x или y создаётся вершина графа и расчитывается расстояние между предыдущей вершиной и нашей и так до пункта выдачи.
3. Каждое ребро графа хранит информацию о расстояние между вершинами в километрах(как его можно расчитать):

$AB = \sqrt{(x_{b}-x_{a})^2 + (y_{b}-y{a})^2}$
1. Пользователю предоставляется возможность выбирать между маршрутами наидудобнейший для него.
2. Затем пользователь может выбрать доставить к дому или на пункт выдачи, если до дома, то начисляется дополнительная плата за курьера.(За каждый километр уже больший коэффицент, но из-за того, что в городе много дорог мы просто считаем дорогу по прямой, в минус не уйдём из-за повышенного коэффицента на доставку от пункта выдачи до города)
## Формулы
Расстояние от вершины до вершины:

$Расстояние = \sqrt{(x_{b}-x_{a})^2 + (y_{b}-y{a})^2}$

Стоимость доставки от склада до пункта выдачи:

$C1 = (k_1+k_2+k_3...)*n$

C1 - цена за доставку от склада до пункта выдачи.
$k_1+k_2+k_3...$ - коэффиценты в зависимости от разных факторов, например:
$k_1$ - стоимость бензина
$k_2$ - наценка за доставку и зарплата водителя фуры.
$k_3$ - Количество нужного товара на складе, то есть достаточно ли его или мало(Чем меньше товара тем больше наценка)
И так далее
n - это весь путь от склада до пункта выдачи в километрах.

Как расчитать весь путь(из алгоритма):

$n = (A_1B_1+A_2B2+A3B3+...+A_nB_n)$

$A_1B_1+...$ - это рёбра графа пути, которые хранят в себе расстояние между всеми этими точками(из алгоритма)

# Чтобы расчитать расстояние между пунктом выдачи и домом
Просто напрямую этой формулой прямым вектором расчитываем расстояние даже не подгоняя под дороги но будет увеличенный коэффицент уже только доставки.
А так просто расстояние между пунктом выдачи и домом:

$Расстояние = \sqrt{(x_{b}-x_{a})^2 + (y_{b}-y{a})^2}$

А затем цена доставки к дому:
$C2 = Расстояние * k_{Progressive}$
# Финал
## Если человек выбрал доставку до пункта выдачи:
$$
C_{Final} = C_1
$$
## Если человек выбрал доставку до дома, то цена:
$$
C_{Final} = C_1+C_2
$$

Визуальное представление алгоритма
![GraphAlgorithm](Images/Artboard%201.png)

## Вершины и сам граф
Сам граф со всеми вершинами будет задан заранее, как и вся карта. Вершины графа повторяюсь будут на повороте, нам это нужно, чтобы удобно можно было расчитывать расстояние, визуальным созданием графа и алгоритмом хранением его в коде займусь я.(Сразу говорю визуальное представление будет сразу в виде карты со всеми точками и представлением). Ещё в самом центре карты 0 координаты по x и y, а каждый следующая целая точка на любой из осей равна +1км.