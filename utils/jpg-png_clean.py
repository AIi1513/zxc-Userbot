import os

path = os.getcwd()
mas = []
for root, dirs, files in os.walk(path):
        for file in files:
                if(file.endswith('.jpg')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)
                elif(file.endswith('.png')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)
