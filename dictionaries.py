# dictionary = a changeable, unordered collection of unique  key : value pairs
#              Fast because they are hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}
#print(capitals['Russia']):
#print(capitals.get('USA')) : tchouf est ce mawjouda walla f dic
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'nammama'})
capitals.pop('China')
capitals.clear()
for key,value in capitals.items():
   print(key,value)