import os
import importlib

def banner():
    print("""
====================================
   CYBER FRAMEWORK PRO (SAFE MODE)
   Modular Security Toolkit
====================================
""")

def list_modules():
    print("\n[MODULES]")
    for file in os.listdir("modules"):
        if file.endswith(".py"):
            print("-", file.replace(".py",""))

def run_module(name):
    try:
        module = importlib.import_module("modules." + name)
        module.run()
    except Exception as e:
        print("Error:", e)

def menu():
    while True:
        print("""
1. List Modules
2. Run Module
3. Exit
""")

        c = input("Select: ")

        if c == "1":
            list_modules()
        elif c == "2":
            m = input("Module name: ")
            run_module(m)
        elif c == "3":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    banner()
    menu()
