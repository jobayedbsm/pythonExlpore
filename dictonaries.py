thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# accessing item
print(thisdict['brand'])
print(thisdict.get('year'))
# update item
thisdict["year"]=1999
print(thisdict)
# remove item from dictonaries
thisdict.pop('year')
print(thisdict)
# remove last item from dictonaries
thisdict.popitem()
print(thisdict)
thisdict['year']=1998
thisdict['model']='jk'
# only retrive value from dictonaries
val=thisdict.values()
for sval in val:
    print(sval)

# only retrive kyes from dictonaries

key=thisdict.keys()
for skey in key:
    print(skey)
# items function return index and value
item=thisdict.items()
for i,v in item:
    print(i,v)