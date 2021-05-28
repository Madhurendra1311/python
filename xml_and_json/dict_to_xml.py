from dicttoxml import dicttoxml
  
  
# Data to be parsed
data = {'a': 2, 
        'b': {
               'c': 'as', 
               'f': True}, 
        'd': 7, 
        }
  
xml = dicttoxml(data)
print(xml)