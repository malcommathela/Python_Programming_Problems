capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Moscow',
            'Russia':'Moscow'}

#print(capitals['Russia'])

#print(capitals.get('Germany'))

#capitals.update({'Germany':'Berlin'})

#capitals.update({'USA':'Los Vegas'})

#capitals.pop('China')

#capitals.clear()

#print(capitals.keys())

#print(capitals.values())

#print(capitals.items())

for key,value in capitals.items():
    print(key,value)