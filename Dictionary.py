                                                      #DICTIONARY:

"""----->dict is a key:value pair separated by:,and keys are unique.
----->in the place of keys we have use immutable data type.
------>
                  
eg:Details_={"name":"lavi",1:"number",(6,7):[1,2]}
print(Details_)

                                         methods:
                                             
 1.keys()------>used to get all the keys from the dict
                            syntax:variable_name.keys()
                            
2.values()---->used to get all the values from the dict
                            syntax:variable_name.values()
                            
                            eg:details_={"name":"lavi",
                                         "age":"23,
                                         "gender":"female"}
                            print(details_.values())

 3.items()----->used to get both key and values in a pair
                            syntax:variable_name.items()

                            eg:details_={"name":"lavi",
                                         "age":"23,
                                         "gender":"female"}
                            print(details_.items())

                            eg:any_=[22,45,6,7,14,25]
                            print(any_[0])
                            details_={"name":"lavi",
                                      "age":23,
                                      "gender":"female"}
                            print(details_['name'])

                            4.clear()------>
                            details_={"name":"lavi",
                                         "age":"23,
                                         "gender":"female"}
                            details_.clear()
                            print(details_)
                            
                            5.update------>
                            egdetails_={"name":"lavi",
                                         "age":"23,
                                         "gender":"female"}
                            detail_.update({"name":"lavanya"})
                            detail_.update({"mob":123456789})
                            print(details_)

                                            Set:
                                ----->set is a collection unordered elements that are separated by ,
                                ----->set is muttable
                                ----->can remove duplicate value by itself...
                                
                                   eg:go=[1,2,3,4,2}
                                   print(go)

                                                    method:
                                   1.union()(|)------>command the elements from both sets
                                   
                                   syntax:set_1.union(set_2)
                                   
                                    eg:go=[1,2,3,4}
                                       so={5,6,7,8}
                                       print(go|so) or
                                       print(go.union(so))
                                       
2.intersection() &------>common elements from both sets
                                    
syntax:set_1.intersection(set_2)
                                    
eg:go=[1,2,3,4}
so={5,6,7,8}
                                       print(go&so) or
                                       print(go.intersection(so))

3.symmetric difference()------>all different elements from both sets
syntax::set_1.symmertic difference(set_2)
                                    
eg:go=[1,2,3,4}
so={5,6,7,8}
print(go^so) or
print(go.symmetric difference(so))

4.add()------>used to add new elements into set

go={1,2,3,4}
go.add(5)
print(go)

5.remove()------>to del the elements from sets

go={1,2,3,4}
go.remove(1)
print(go)

6.discard()------->"""

go={1,2,3,4}
go.discard(3)
print(go)




























                            
                            


                           
                            
                                                      
