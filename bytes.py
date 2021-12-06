um = b'data'
print(um)
print(type(um))

norsk =  "Maten vår ble ikke servert på samme tid, derfor begynte jeg å spise min før"
data = norsk.encode('utf-8')
print(data)

norwegian = data.decode('utf-8')
print(norwegian)

# True
print(norwegian == norsk)