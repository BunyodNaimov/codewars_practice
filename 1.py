"""
Джеку очень нравится его число пять: хитрость здесь в том, что вам нужно умножить каждое число на 5,
возведенное в число цифр каждого числа, так, например:

  3 -->    15  (  3 * 5¹)
 10 -->   250  ( 10 * 5²)
200 --> 25000  (200 * 5³)
  0 -->     0  (  0 * 5¹)
 -3 -->   -15  ( -3 * 5¹)

"""


def multiply(n):
    """
    1:num = len(str(abs(n))): В этой строке вычисляется количество цифр в абсолютном значении n.
    Сначала функция abs() используется для получения абсолютного значения n,
    затем оно преобразуется в строку с помощью функции str(), и, наконец, с помощью функции len()
    определяется количество символов в этой строке.

    2: return n * 5**num: Эта строка возвращает результат умножения n на 5 в степени num.
    Здесь ** обозначает возведение в степень. Таким образом, результатом функции будет произведение
    n на 5 в степени, равной количеству цифр в абсолютном значении n.
    """
    num = len(str(abs(n)))

    return n * 5 ** num


print(multiply(-3))
