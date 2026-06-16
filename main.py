# main.py
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage:\n  python main.py add 'title'\n  python main.py list\n  python main.py done ID\n  python main.py remove ID")
        return
    print(f"Got command: {sys.argv[1]}")

if __name__ == "__main__":
    main()