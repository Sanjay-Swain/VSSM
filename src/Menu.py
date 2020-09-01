from commands import *

print("Welcome to VSSM v0.1")
print("Type help to see available commands")
print()


def main():
    running = True

    while running:
        try:
            command_input = input("VSSM > ").strip().lower().split()
            if command_input[0] == "exit":
                verify = input("Are you sure you want to leave without saving changes (Y|N) :")
                if verify[0].strip().lower() == 'y':
                    running = False
            execute(command_input)
        except IndexError:
            print("Please check the syntax of the command.")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
