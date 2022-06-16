# Урок 7. Работа с файловой системой. Исключения в Python.


# Задание №1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

#
# import os
#
# folder_struct = {
#     "my_project": [
#         {
#             "settings": [],
#             "mainapp": [],
#             "adminapp": [],
#             "authapp": []
#         }]
# }
#
#
# def project_starter(pth, struct):
#
#     for fold_node, ch_node in struct.items():
#
#         test_path = os.path.join(pth, fold_node)
#
#         if not os.path.exists(test_path):
#             os.mkdir(test_path)
#
#         if len(ch_node) > 0:
#             for node in ch_node:
#                 project_starter(test_path, node)
#
#
# if __name__ == "__main__":
#
#     project_starter(os.getcwd(), struct=folder_struct)


#  Задание №3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
#  Написать скрипт, который собирает все шаблоны в одну папку templates, например:

# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html

# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

""" task 2 """

def make_project(glb_tab, stryct, root):

    if glb_tab != -1 and not os.path.exists(root):
        os.mkdir(root)
    #print(f"make folder {root}")
    os.chdir(root)
    n_stryct = []
    inside_dir = None
    for i, (node_name, line_tab, is_dir) in enumerate(stryct):

        if inside_dir:
            if inside_dir[1] < line_tab:
                #print(f"in {inside_dir[0]} {node_name}")
                n_stryct.append((node_name, line_tab, is_dir))
                if i == len(stryct) - 1:
                    make_project(inside_dir[1], n_stryct,
                                 os.path.join(root, inside_dir[0]))
            elif inside_dir[1] == line_tab and is_dir:
                #print(f"put stack in {inside_dir[0]} in {root}")
                make_project(inside_dir[1], n_stryct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab)
                n_stryct = []

            else:
                #print(f"make folder {inside_dir[0]}")

                if not is_dir:
                    n_stryct.append((node_name, line_tab, is_dir))

                make_project(inside_dir[1], n_stryct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab) if is_dir else None

        elif is_dir:
            #print(f"find dir {node_name}")
            inside_dir = (node_name, line_tab)
        else:
            open(node_name, "a").close()
            #print(f"create file {node_name} in {root}")


if __name__ == "__main__":

    import sys
    import os

    # image if file not big
    with open("./config.yaml", "r", encoding="utf-8") as conf_text:
        conf = map(lambda x: (
            x.strip().replace("\t", "  ").replace(":", ""),
            x.rstrip().count(" "),
            x.find(":") > 0
        ), conf_text.readlines())

    make_project(-1, list(conf), os.getcwd())

    exit(0)




""" task 3 """

if __name__ == "__main__":

    import os
    import sys
    import shutil

    glb_path = sys.argv[1]
    files = [os.path.relpath(os.path.join(root, file), glb_path) for root, _, files in os.walk(
        glb_path) for file in files if file.endswith(".html")]
    for rel_path in files:
        path, file = os.path.split(rel_path)
        test_path = os.path.join(glb_path, "template", path)
        if not os.path.exists(test_path):
            os.makedirs(test_path)
        shutil.copyfile(os.path.join(glb_path,rel_path), os.path.join(test_path, file))


#  Задание №4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт;
# 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


#
# import os
# import sys
# import time
#
# size = {}
#
#
# def scan_mem(pth):
#
#     for root, _, files in os.walk(pth):
#         for file in files:
#             correct_file = os.path.join(root, file)
#             mem = 10 ** len(str(os.stat(correct_file).st_size))
#             size[mem] = size.get(mem, 0) + 1
#
#
# def scan_mem_recursion(pth):
#
#     if not os.path.exists(pth):
#         return
#     with os.scandir(pth) as files:
#
#         for node in files:
#
#             if os.path.isfile(node):
#
#                 mem = 10 ** (len(str(os.stat(node).st_size)) - 1)
#                 size[mem] = size.get(mem, 0) + 1
#             elif os.path.isdir(node):
#                 scan_mem(os.path.join(pth, node))
#
#
# if __name__ == "__main__":
#
#     if len(sys.argv) == 2:
#         pth = sys.argv[1]
#     else:
#         pth = os.getcwd()
#     print(f"{'soution with os.walk':^39}")
#     time_now = time.perf_counter()
#     scan_mem(pth)
#     print(size, f"\n as { time.perf_counter() - time_now}")
#
#     size = {}
#     print(f"{'soution with resursion':^39}")
#     time_now = time.perf_counter()
#     scan_mem_recursion(pth)
#     print(size, f"\n as { time.perf_counter() - time_now}")