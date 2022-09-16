from jsonFileReader import JsonFileReader
from service import PygameService 


if __name__ == "__main__": 
  
    reader = JsonFileReader("cmain/menu.json")
    list = reader.read() 
    pgService = PygameService(800, 600, list)
    pgService.run()