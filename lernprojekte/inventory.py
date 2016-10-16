inventory = {'Robe': 1, 'Fackeln': 1, 'Axt': 2, 'Schwarze Katze': 2 }

def listInventory(list):
    itemsTotal = 0
    print 'This is in your inventory:'
    print ''
    k = 0
    for i, j in list.items():
        print ('( '+ str(k)+' ) - ' + '# ' + str(j) + ' ' + i)
        itemsTotal += int(j)
        k += 1
    print 'total number of Items: ' + str(itemsTotal)

def howMany(list):
    print (list)
    print 'What Item are you looking for?'
    item = raw_input()
    if item in list.keys():
        print ('You have ' + str(list[item]) + ' items of ' + item)
    else:
        print 'Sorry you havn\'t a item with this name'

def addItem(list):
    print 'What Item should we add?'
    newItem = raw_input()
    print 'How many Items do you have?'
    numberOfItems = raw_input()
    list.update({newItem: numberOfItems})
    listInventory(list)

def delItem(list):
    listInventory(list)
    print ('What Item do you want to give away?')
    delItem = raw_input()
    if delItem in list.keys():
        del list[delItem]
    else:
        print 'here is no Item called . ' + str(delItem)
    listInventory(list)



#listInventory(inventory)
#howMany(inventory)
#addItem(inventory)
delItem(inventory)
