pic 1



**Отчёт по лабораторной работе № 5**

Дискреционное разграничение прав в Linux. SetUID-, SetGID- и Sticky-биты





1\. Цель работы







2\. Формулировка задания



1. Подготовить лабораторный стенд: установить gcc, отключить SELinux.
2. Создать программу simpleid.c, скомпилировать и выполнить её.
3. Сравнить вывод программы с системной командой id.
4. Усложнить программу до simpleid2.c с выводом действительных и эффективных идентификаторов.
5. Установить SetUID- и SetGID-биты, проверить их действие.
6. Создать программу readfile.c, проверить её работу с SetUID-битом.
7. Исследовать Sticky-бит на директории /tmp.
8. Занести наблюдения в отчёт.







**3. Описание процесса выполнения задания**

3.1 Подготовка лабораторного стенда

Действие: Проверить наличие компилятора gcc и отключить SELinux.



Команды:



pic 2

Результат:



gcc -v выводит версию компилятора (если установлен).

3.2 Создание программы simpleid.c

Действие: Войти как guest, создать программу для вывода эффективных идентификаторов.

Содержимое simpleid.c:
pic 3
pic 4
uid=1001, gid=1001

3.3 Сравнение с системной командой id

Действие: Выполнить системную команду id и сравнить результаты.
Команда:
pic5

Результат:

Сравнение: Вывод simpleid совпадает с эффективными идентификаторами из id.



3.4 Усложнение программы до simpleid2.c

Действие: Добавить вывод действительных и эффективных идентификаторов.

Содержимое simpleid2.c:

pic 6

Компиляция и запуск:
bash
gcc simpleid2.c -o simpleid2
./simpleid2

Результат:
text
e\_uid=1001, e\_gid=1001
real\_uid=1001, real\_gid=1001
При обычном запуске действительные и эффективные идентификаторы совпадают.


3.5 Установка SetUID-бита

Действие: От имени суперпользователя сменить владельца файла simpleid2 на root и установить SetUID-бит.

Команды:
pic 7
 Бит s в правах владельца означает SetUID.







3.6 Проверка действия SetUID-бита

Действие: Запустить simpleid2 и id от имени guest.

Команды:
pic 8

При запуске simpleid2 эффективный UID стал 0 (root), так как установлен SetUID-бит и владелец файла — root. Это позволяет программе выполняться с правами суперпользователя.


3.7 Создание программы readfile.c

Действие: Создать программу для чтения файла.
Содержимое readfile.c:
pic 9

3.8 Подготовка файла для чтения

Действие: Сменить владельца файла readfile.c на root и установить права, запрещающие чтение для guest.
Команды:
pic 10


3.9 Установка SetUID-бита на readfile

Действие: Сменить владельца программы readfile на root и установить SetUID-бит.
pic 7

3.10 Проверка чтения файла readfile.c

Действие: Попробовать прочитать readfile.c с помощью readfile.



Команда:
pic 10
 Программа readfile имеет SetUID-бит и владельца root, поэтому выполняется с правами root и может читать файл, недоступный для guest.


3.11 Исследование Sticky-бита

3.11.1 Проверка Sticky-бита на /tmp
Действие: Выяснить, установлен ли Sticky-бит на /tmp.


Команда:
pic 10

 Бит t в правах означает Sticky-бит.



3.11.2 Создание файла в /tmp

Действие: От имени guest создать файл file01.txt со словом test.
Команды:
pic 10


3.11.3 Чтение файла от guest2

Действие: От имени guest2 прочитать файл.
Команда:
pic 11

Чтение разрешено, так как права o+r установлены.


3.11.4 Дозапись в файл от guest2
Действие: Попробовать дозаписать слово test2.
Команда:
pic 11

Дозапись разрешена, так как права o+w установлены.





3.11.5 Перезапись файла от guest2

Действие: Попробовать перезаписать файл словом test3.
Команда:
pic 12

Перезапись разрешена, так как права o+w установлены.


3.11.6 Удаление файла от guest2
pic 12

Sticky-бит на /tmp запрещает удаление файлов, владельцем которых не является текущий пользователь. guest2 не владелец файла, поэтому удаление запрещено.




3.11.7 Снятие Sticky-бита
Действие: От имени суперпользователя снять Sticky-бит с /tmp.
Команды:
pic 13

Бит t отсутствует.



3.11.8 Повторная попытка удаления

Действие: От имени guest2 попробовать удалить файл.
pic 14
Без Sticky-бита любой пользователь с правами на запись в директорию может удалять файлы, даже если он не является их владельцем.



3.11.9 Возврат Sticky-бита
Действие: Вернуть Sticky-бит на /tmp.

Команды:
pic 15

Sticky-бит восстановлен.



4\. Содержание отчёта

□ Титульный лист

□ Цель работы

□ Описание процесса выполнения с командами и снимками экрана

□ Листинги программ (simpleid.c, simpleid2.c, readfile.c)

□ Наблюдения по SetUID-, SetGID- и Sticky-битам

□ Выводы, согласованные с целью работы







**5. Выводы**

В ходе лабораторной работы я:



Подготовил лабораторный стенд: установил gcc, отключил SELinux.



Создал и скомпилировал программы simpleid.c, simpleid2.c, readfile.c.



Изучил разницу между действительными и эффективными идентификаторами.



Установил SetUID- и SetGID-биты и убедился, что:



SetUID позволяет программе выполняться с правами владельца файла (root).



SetGID позволяет программе выполняться с правами группы владельца файла.



Продемонстрировал, что SetUID-программа может читать файлы, недоступные обычному пользователю (включая /etc/shadow).



Исследовал Sticky-бит на /tmp:



При установленном Sticky-бите удалять файлы может только их владелец (или root).



Без Sticky-бита любой пользователь с правами на запись в директорию может удалять чужие файлы.



Убедился в потенциальной опасности SetUID-программ и важности Sticky-бита для общих директорий.



Цель работы достигнута: получены практические навыки работы с SetUID-, SetGID- и Sticky-битами, изучены механизмы смены идентификаторов процессов.



**6. Краткая сводка команд**

bash

\# Подготовка стенда

gcc -v

yum install gcc

setenforce 0

getenforce



\# Создание и компиляция программ

gcc simpleid.c -o simpleid

./simpleid

id



gcc simpleid2.c -o simpleid2

./simpleid2



\# Установка SetUID-бита

su -

chown root:guest /home/guest/simpleid2

chmod u+s /home/guest/simpleid2

ls -l /home/guest/simpleid2

exit



\# Проверка

./simpleid2

id



\# Установка SetGID-бита

su -

chmod g+s /home/guest/simpleid2

ls -l /home/guest/simpleid2

exit

./simpleid2



\# Программа readfile

gcc readfile.c -o readfile



\# Подготовка файла

su -

chown root:root /home/guest/readfile.c

chmod 600 /home/guest/readfile.c

exit

cat /home/guest/readfile.c



\# SetUID на readfile

su -

chown root:root /home/guest/readfile

chmod u+s /home/guest/readfile

ls -l /home/guest/readfile

exit



\# Проверка чтения

./readfile /home/guest/readfile.c

./readfile /etc/shadow



\# Исследование Sticky-бита

ls -l / | grep tmp

echo "test" > /tmp/file01.txt

ls -l /tmp/file01.txt

chmod o+rw /tmp/file01.txt

ls -l /tmp/file01.txt



\# От guest2

cat /tmp/file01.txt

echo "test2" >> /tmp/file01.txt

cat /tmp/file01.txt

echo "test3" > /tmp/file01.txt

cat /tmp/file01.txt

rm /tmp/file01.txt



\# Снятие Sticky-бита

su -

chmod -t /tmp

exit

ls -l / | grep tmp



\# Повторное удаление

rm /tmp/file01.txt



\# Возврат Sticky-бита

su -

chmod +t /tmp

exit

ls -l / | grep tmp







**7. Листинги программ**

simpleid.c

c

\#include <sys/types.h>

\#include <unistd.h>

\#include <stdio.h>



int main() {

&#x20;   uid\_t uid = geteuid();

&#x20;   gid\_t gid = getegid();

&#x20;   printf("uid=%d, gid=%d\\n", uid, gid);

&#x20;   return 0;

}

simpleid2.c

c

\#include <sys/types.h>

\#include <unistd.h>

\#include <stdio.h>



int main() {

&#x20;   uid\_t real\_uid = getuid();

&#x20;   uid\_t e\_uid = geteuid();

&#x20;   gid\_t real\_gid = getgid();

&#x20;   gid\_t e\_gid = getegid();



&#x20;   printf("e\_uid=%d, e\_gid=%d\\n", e\_uid, e\_gid);

&#x20;   printf("real\_uid=%d, real\_gid=%d\\n", real\_uid, real\_gid);

&#x20;   return 0;

}

readfile.c

c

\#include <fcntl.h>

\#include <stdio.h>

\#include <sys/stat.h>

\#include <sys/types.h>

\#include <unistd.h>



int main(int argc, char\* argv\[]) {

&#x20;   unsigned char buffer\[16];

&#x20;   size\_t bytes\_read;

&#x20;   int i;

&#x20;   int fd = open(argv\[1], O\_RDONLY);

&#x20;   do {

&#x20;       bytes\_read = read(fd, buffer, sizeof(buffer));

&#x20;       for (i = 0; i < bytes\_read; ++i)

&#x20;           printf("%c", buffer\[i]);

&#x20;   } while (bytes\_read == sizeof(buffer));

&#x20;   close(fd);

&#x20;   return 0;

}

