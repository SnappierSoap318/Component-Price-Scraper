from vedantComputers import vedantComputers
from mdcomputer import mdComputers
def main():
    component = input('Enter component name: ')
    with open('price_list.txt', 'w') as file:
        file.write('-------Vedant Computers Price List---------\n')
        file.close()
    vedantComputers(component)
    with open('price_list.txt', 'a') as file:
        file.write('----------MD Computers Price List-----------\n')
        file.close()
    mdComputers(component)


if __name__ == "__main__":
    main()