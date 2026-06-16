# добавляем в todo/commands.py
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список пуст")
        return
    for t in tasks:
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{mark} {t['id']:>3}. {t['title']}")