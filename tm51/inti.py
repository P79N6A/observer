a = [{"situation":1,"level":4,"description":"准妈妈很适合吃包子，包子皮是发面食品，富含B族维生素，而且很容易消化。包子搭配了多种蔬菜和肉类，能够为准妈妈提供各种营养。"},{"situation":2,"level":4,"description":"坐月子能吃包子，包子皮是发面食品，比较容易消化，适合月子期间食用。"},{"situation":3,"level":4,"description":"一般情况下，包子都会同时搭配多种蔬菜和肉类，能够做到基本的膳食平衡，适合哺乳妈妈。"},{"situation":4,"level":4,"description":"包子可以通过改变面皮和馅料，做出很多花样来，促排期间和移植后吃包子改善饮食搭配，为人体提供各种营养，所以试管期间是可以吃包子的！"}]

for i in a:
    i['title'] = '测试数据'

print(str(a).replace(' ',''))