my_set = {'jk','pineapple','jackfruits','jk'}
another_set={"pineapple","tj","jk"}

try:
    my_set.remove('tanvir')
except KeyError:
    print('data not exist to remove')

