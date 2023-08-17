import json, os

class FileReaderService:

    
    
    def get_file_contents(file_name):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
        file = open(os.path.join( __location__ , str(file_name)),'r').read()
        return file

class JsonFileReaderService(FileReaderService):
    pass

class XmlFileReaderService(FileReaderService):
    pass

fr = FileReaderService
print(fr.get_file_contents('demo.json'))
