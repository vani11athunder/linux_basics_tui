#!/usr/bin/env python3
from textual.app import App
from textual.widgets import Static, Button, Input
from textual.containers import Vertical, Horizontal, Grid

pwd_text = 'Показывает, где ты сейчас находишься. \n pwd -> Пример вывода: /home/user'
ls_text = 'Показывает содержимое папки. \n ls -l -> подробный список (права, владелец, размер) \n ls -a -> включая скрытые файлы \n ls -la -> комбинация двух флагов (подробно + скрытые)'
cd_text = 'Переход между папками. \n cd /home/user/Documents -> переход в указанную папку \n cd .. -> на уровень вверх \n cd ~ -> в домашнюю папку пользователя'
mkdir_text = 'Создает новую папку. \n mkdir test_folder -> создаёт папку с именем test_folder \n Можно создавать вложенные папки: mkdir -p a/b/c'
touch_text = 'Создает пустой файл или обновляет время изменения файла. \n touch file.txt -> создаёт пустой файл file.txt'
cp_text = 'Копирование файлов и папок. \n cp file.txt copy.txt -> копирует файл \n cp -r folder1 folder2 -> копирует папку целиком (рекурсивно)'
mv_text = 'Перемещение или переименование. \n mv file.txt /home/user/ -> переместить файл \n mv old.txt new.txt -> переименовать файл'
rm_text = 'Удаление файлов и папок. \n rm file.txt -> удалить файл \n rm -r folder -> удалить папку и всё содержимое \n rm -rf folder -> принудительное удаление без вопросов (опасно)'
cat_text = 'Просмотр содержимого файла. \n cat file.txt -> выводит весь файл в терминал'
man_text = 'Открывает справку по команде. \n man ls -> документация по команде ls \n Выход: клавиша q'


cd_tasks = [
    'Перейди в домашнюю директорию',
    'Поднимись на уровень выше через cd ..',
    'Перейди в папку Downloads',
    'Зайди в директорию /var/log',
    'Перейди в папку, используя абсолютный путь'
]
pwd_tasks = [
    'Узнай, в какой директории ты сейчас находишься',
    'Перейди в папку Documents и проверь путь через pwd',
    'Открой терминал и определи домашнюю директорию',
    'Перейди в /tmp и выведи текущий путь',
    'После нескольких переходов между папками проверь своё местоположение'
]
ls_tasks = [
    'Выведи список файлов в текущей папке',
    'Покажи скрытые файлы через ls -a',
    'Выведи подробную информацию о файлах через ls -l',
    'Скомбинируй флаги и выполни ls -la',
    'Посмотри содержимое папки /etc'
]
mkdir_tasks = [
    'Создай папку test_folder',
    'Создай папку projects',
    'Создай вложенные папки через mkdir -p dir1/dir2/dir3',
    'Создай папку в домашней директории',
    'Создай сразу несколько папок одной командой'
]
touch_tasks = [
    'Создай пустой файл file.txt',
    'Создай файл notes.md',
    'Создай несколько файлов одной командой',
    'Создай файл внутри другой папки',
    'Проверь, что файл появился через ls'
]
cp_tasks = [
    'Скопируй file.txt в copy.txt',
    'Скопируй файл в другую директорию',
    'Скопируй папку через cp -r',
    'Создай резервную копию файла',
    'Скопируй несколько файлов в одну папку'
]
mv_tasks = [
    'Переименуй file.txt в new_file.txt',
    'Перемести файл в другую папку',
    'Перемести папку projects в /tmp',
    'Переименуй директорию',
    'Перемести несколько файлов в одну директорию'
]
rm_tasks = [
    'Удалить файл file.txt',
    'Удалить папку через rm -r',
    'Попробовать удалить папку без -r и посмотреть ошибку',
    'Удалить несколько файлов одной командой',
    'Удалить временные файлы из папки'
]
cat_tasks = [
    'Посмотреть содержимое файла file.txt',
    'Создать текстовый файл и прочитать его через cat',
    'Вывести содержимое нескольких файлов',
    'Перенаправить вывод cat в другой файл',
    'Проверить содержимое конфигурационного файла'
]
man_tasks = [
    'Открыть документацию по ls',
    'Найти справку по команде rm',
    'Открыть man для mkdir',
    'Прочитать описание команды cp',
    'Открыть справку и выйти через q']
pwd_answers = [
    'pwd',
    'cd Documents && pwd',
    'cd ~ && pwd',
    'cd /tmp && pwd',
    'pwd'
]
ls_answers = [
    'ls',
    'ls -a',
    'ls -l',
    'ls -la',
    'ls /etc'
]
cd_answers = [
    'cd ~',
    'cd ..',
    'cd Downloads',
    'cd /var/log',
    'cd /home/user/Documents'
]
mkdir_answers = [
    'mkdir test_folder',
    'mkdir projects',
    'mkdir -p dir1/dir2/dir3',
    'mkdir ~/new_folder',
    'mkdir dir1 dir2 dir3'
]
touch_answers = [
    'touch file.txt',
    'touch notes.md',
    'touch file1.txt file2.txt file3.txt',
    'touch folder/file.txt',
    'ls'
]
cp_answers = [
    'cp file.txt copy.txt',
    'cp file.txt /home/user/Documents',
    'cp -r folder1 folder2',
    'cp file.txt backup_file.txt',
    'cp file1.txt file2.txt folder/'
]
mv_answers = [
    'mv file.txt new_file.txt',
    'mv file.txt /home/user/Documents',
    'mv projects /tmp',
    'mv old_folder new_folder',
    'mv file1.txt file2.txt folder/'
]
rm_answers = [
    'rm file.txt',
    'rm -r folder',
    'rm folder',
    'rm file1.txt file2.txt',
    'rm *.tmp'
]
cat_answers = [
    'cat file.txt',
    'cat notes.txt',
    'cat file1.txt file2.txt',
    'cat file.txt > new_file.txt',
    'cat /etc/hosts'
]
man_answers = [
    'man ls',
    'man rm',
    'man mkdir',
    'man cp',
    'man ls'
]


class MyApp(App):
    CSS_PATH = 'style.tcss'
    now = ''
    cd_sol = 0
    pwd_sol = 0
    ls_sol = 0
    mkdir_sol = 0
    rm_sol = 0
    mv_sol = 0
    cp_sol = 0
    cat_sol = 0
    man_sol = 0
    touch_sol = 0
    def compose(self):
        self.now = ''
        self.cd_n = 0
        self.cp_n = 0
        self.mkdir_n = 0
        self.rm_n = 0
        self.ls_n = 0
        self.cat_n = 0
        self.man_n = 0
        self.mv_n = 0
        self.touch_n = 0
        self.pwd_n = 0
        with Vertical():
            with Horizontal(id='first_row'):
                yield Button("cd", id = "cd")
                yield Button("pwd", id = "pwd")
                yield Button('ls', id='ls')
            with Horizontal(id='second_row'):
                yield Button('mkdir', id='mkdir')
                yield Button('rm', id='rm')
                yield Button('cp', id='cp')
            with Horizontal(id='third_row'):
                yield Button('mv', id='mv')
                yield Button('touch', id='touch')
                yield Button('cat', id='cat')
            with Horizontal(id='fourth_row'):
                yield Button('man', id='man')
        yield Static('', id='task')
        yield Input(placeholder='Решение(нажми Enter)', id='input')
        yield Static('', id='info')


    def on_mount(self):
        self.query_one("#task", Static).update("Выбери инструмент для изучения")
        self.query_one("#info", Static).update("Начнем изучение")
    def on_button_pressed(self, event):
        
        output_info_widget = self.query_one("#info", Static)
        output_task_widget = self.query_one("#task", Static)
        if event.button.id == 'cd':
            output_info_widget.update(cd_text)
            output_task_widget.update("\n".join(cd_tasks))
            self.now = 'cd'

        elif event.button.id == 'pwd':
            output_info_widget.update(pwd_text)
            output_task_widget.update("\n".join(pwd_tasks))
            self.now = 'pwd'
        elif event.button.id == 'ls':
            output_info_widget.update(ls_text)
            output_task_widget.update("\n".join(ls_tasks))
            self.now = 'ls'
        elif event.button.id == 'mkdir':
            output_info_widget.update(mkdir_text)
            output_task_widget.update("\n".join(mkdir_tasks))
            self.now = 'mkdir'
        elif event.button.id == 'rm':
            output_info_widget.update(rm_text)
            output_task_widget.update("\n".join(rm_tasks))
            self.now = 'rm'
        elif event.button.id == 'cp':
            output_info_widget.update(cp_text)
            output_task_widget.update("\n".join(cp_tasks))
            self.now = 'cp'
        elif event.button.id == 'mv':
            output_info_widget.update(mv_text)
            output_task_widget.update("\n".join(mv_tasks))
            self.now = 'mv'
        elif event.button.id == 'touch':
            output_info_widget.update(touch_text)
            output_task_widget.update("\n".join(touch_tasks))
            self.now = 'touch'
        elif event.button.id == 'cat':
            output_info_widget.update(cat_text)
            output_task_widget.update("\n".join(cat_tasks))
            self.now = 'cat'
        elif event.button.id == 'man':
            output_info_widget.update(man_text)
            output_task_widget.update("\n".join(cd_tasks))
            self.now = 'man'



    def on_input_submitted(self, event):
        output_task_widget = self.query_one("#task", Static)
        if self.now == 'cd':
            if event.value == cd_answers[self.cd_n]:
                cd_tasks[self.cd_n] = cd_tasks[self.cd_n] + ' -> Верно'
                output_task_widget.update("\n".join(cd_tasks))
                self.cd_n+=1
            else:
                cd_tasks[self.cd_n] = cd_tasks[self.cd_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(cd_tasks))
        elif self.now == 'pwd':
            if event.value == pwd_answers[self.pwd_n]:
                pwd_tasks[self.pwd_n] = pwd_tasks[self.pwd_n] + ' -> Верно'
                output_task_widget.update("\n".join(pwd_tasks))
                self.pwd_n+=1
            else:
                pwd_tasks[self.pwd_n] = pwd_tasks[self.pwd_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(pwd_tasks))       
        elif self.now == 'mkdir':
            if event.value == mkdir_answers[self.mkdir_n]:
                mkdir_tasks[self.mkdir_n] = mkdir_tasks[self.mkdir_n] + ' -> Верно'
                output_task_widget.update("\n".join(mkdir_tasks))
                self.mkdir_n+=1
            else:
                mkdir_tasks[self.mkdir_n] = mkdir_tasks[self.mkdir_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(mkdir_tasks))
        elif self.now == 'ls':
            if event.value == ls_answers[self.ls_n]:
                ls_tasks[self.ls_n] = ls_tasks[self.ls_n] + ' -> Верно'
                output_task_widget.update("\n".join(ls_tasks))
                self.ls_n+=1
            else:
                ls_tasks[self.ls_n] = ls_tasks[self.ls_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(ls_tasks))
        elif self.now == 'rm':
            if event.value == rm_answers[self.rm_n]:
                rm_tasks[self.rm_n] = rm_tasks[self.rm_n] + ' -> Верно'
                output_task_widget.update("\n".join(rm_tasks))
                self.rm_n+=1
            else:
                rm_tasks[self.rm_n] = rm_tasks[self.rm_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(rm_tasks))
        elif self.now == 'cp':
            if event.value == cp_answers[self.cp_n]:
                cp_tasks[self.cp_n] = cp_tasks[self.cp_n] + ' -> Верно'
                output_task_widget.update("\n".join(cp_tasks))
                self.cp_n+=1
            else:
                cp_tasks[self.cp_n] = cp_tasks[self.cp_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(cp_tasks))
        elif self.now == 'mv':
            if event.value == mv_answers[self.mv_n]:
                mv_tasks[self.mv_n] = mv_tasks[self.mv_n] + ' -> Верно'
                output_task_widget.update("\n".join(mv_tasks))
                self.mv_n+=1
            else:
                mv_tasks[self.mv_n] = mv_tasks[self.mv_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(mv_tasks))
        elif self.now == 'touch':
            if event.value == touch_answers[self.touch_n]:
                touch_tasks[self.touch_n] = touch_tasks[self.touch_n] + ' -> Верно'
                output_task_widget.update("\n".join(touch_tasks))
                self.touch_n+=1
            else:
                touch_tasks[self.touch_n] = touch_tasks[self.touch_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(touch_tasks))
        elif self.now == 'cat':
            if event.value == cat_answers[self.cat_n]:
                cat_tasks[self.cat_n] = cat_tasks[self.cat_n] + ' -> Верно'
                output_task_widget.update("\n".join(cat_tasks))
                self.cat_n+=1
            else:
                cat_tasks[self.cat_n] = cat_tasks[self.cat_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(cat_tasks))
        elif self.now == 'man':
            if event.value == man_answers[self.man_n]:
                man_tasks[self.man_n] = man_tasks[self.man_n] + ' -> Верно'
                output_task_widget.update("\n".join(man_tasks))
                self.man_n+=1
            else:
                man_tasks[self.man_n] = man_tasks[self.man_n] + ' -> Пробуй еще'
                output_task_widget.update("\n".join(man_tasks))

# 1) проверить задания
# 2) возможность сохранения результатов(сейчас при переходе на другое задание результат сохраняется, но решать приходиться заново)
# 3) выгрузка на гитхаб + установочный файл для винды и линукса


app = MyApp()
app.run()
