# main.py
import sys
from todo.commands import add_task, list_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>")
        return
    print(f"Got command: {sys.argv[1]}")

if __name__ == "__main__":
    main()
elif cmd == "list":
        list_tasks()