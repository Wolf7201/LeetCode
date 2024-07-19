from collections import defaultdict


def build_tree(paths):
    tree = lambda: defaultdict(tree)
    root = tree()
    # Создаем дерево вложенности
    for path in paths:
        t = root
        for part in path.split('/'):
            t = t[part]
    return root


def print_tree(tree, indent=0):
    # Сортировка ключей и вывод
    for key in sorted(tree.keys()):
        print('  ' * indent + key)
        if tree[key]:  # если директория содержит вложенные элементы
            print_tree(tree[key], indent + 1)


def main():
    n = int(input())
    paths = [input() for _ in range(n)]
    tree = build_tree(paths)
    # Первый вызов функции печати дерева без отступа, т.к. это корень
    print_tree(tree[next(iter(tree))])  # next(iter(tree)) - это корневой элемент


main()
