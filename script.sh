 #1 laba
#!/bin/bash
authorize_users() {
    openvt -c 1 -- su - username1 &
}
create_user_info_file() {
    who = >> user_info.txt
    date = >> user_info.txt
}
create_user_info_file
                                                                                                                            #2 laba
#!/bin/bash

mkdir -p ~/cat1/cat2/cat3/cat6
mkdir -p ~/cat1/cat2/cat3/cat7
mkdir -p ~/cat1/cat2/cat5
mkdir -p ~/cat1/cat3/cat4
mkdir -p ~/cat1/cat8
ln -s ~/cat1/cat2/cat3/cat6 ~/cat1/cat8/symlink_to_cat6

rm -r ~/cat1/cat2/cat3
rm -r ~/cat1/cat2/cat3/cat6
rm -r ~/cat1/cat2/cat3/cat7

rm ~/cat1/cat8/symlink_to_cat6

mkdir ~/dir
date > ~/dir/date


ln -s ~/dir/date ~/link1

mv ~/dir/date ~/dir/current_date

cp ~/dir/current_date ~/

tree ~/cat1
                                                                                                                              #3 laba
#!/bin/bash

cut -d: -f1 passwd_example | sort -r > cut_result

diff cut_result cut_result2

cat cut_result2 >> cut_result

uniq cut_result > cut_result_temp && mv cut_result_temp cut_result

user="username"
grep "^$user:" passwd_example | cut -d: -f6

printenv

echo $TERM

export PS1="\[\033[0;41m\]<\u@\h \W>\$\[\033[0m\]"

PS1="\[\033[0;41m\]<\u@\h \W>\$\[\033[0m\] "
                                                                                                                            #4 laba
                                                                                                                            #5 laba
#!/bin/bash

ps -u root --sort=ppid > proc1

ps -u $USER -o pid,ppid,stat | grep ' R ' > user_running_processes.txt

ps aux --sort=-%cpu | head -n 2 >> proc1

top

pstree -p | grep firefox

firefox &
gedit &
gedit &


jobs

# fg - Перемещение задачи на передний план
# bg - Запуск задачи в фоновом режиме
# Ctrl + z - Остановка текущего процесса
# Ctrl + c - Отмена выполнения текущей задачи

man kill

kill PID

killall -u $USER
                                                                                                                          #6 laba
                                                                                                                          #7 laba
if [ $# -eq 2 ]; then
    sum=$(( $1 + $2 ))

    echo "Сумма $1 и $2 равна $sum"

    if [ $sum -lt 0 ]; then
        echo "Результат меньше нуля"
    elif [ $sum -gt 0 ]; then
        echo "Результат больше нуля"
    else
        echo "Результат равен нулю"
    fi
else
    echo "Скрипт принимает два аргумента"
fi

#!/bin/bash

if [ $# -eq 1 ]; then
    current_time=$(date +"%Y%m%d_%H%M%S")
    archive_name="$1_$current_time.tar.gz"

    find ~/ -name "*.txt" -exec tar -czf "$archive_name" {} +

    echo "Архив $archive_name создан"
else
    echo "Скрипт принимает один аргумент (имя архива)"
fi

