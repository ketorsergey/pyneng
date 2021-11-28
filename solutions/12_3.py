"""
Функция ожидает как аргументы два списка:

список доступных IP-адресов
список недоступных IP-адресов
Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.,jughjjh
"""
from tabulate import tabulate

reachable = ['8.8.4.4', '1.1.1.1', '172.21.41.128', '172.21.41.132']
unreachable = ['5.5.5.5', '2.2.2.2', '7.7.7.7', '192.168.1.1']
 
def print_ip_table(reachable, unreachable):
    dictip = {"Reachable:" : reachable, "Unreachcable:" : unreachable}
    print(tabulate(dictip, headers = "keys"))
    return

if __name__ == "__main__":
    print_ip_table(reachable, unreachable)
