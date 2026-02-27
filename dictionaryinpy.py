# IN THIS THE OPERATIONS OR FUNCTIONS OF DICTIONARY LIKE CREATING,UPDATING AND MANUPILATING IS DONE.

# CREATING A DICTIONARY. 
dictionary = {
    101 : {"NAME":"SAM" , "GRADE":"A+" , "ATTENDANCEE":90},
    102 : {"NAME":"SANJU" , "GRADE":"A" , "ATTENDANCE":85},
    103 : {"NAME":"VIRAT" , "GRADE":"B" , "ATTENDANCE":87},
    104 : {"NAME":"ROHIT" , "GRADE":"B+" , "ATTENDANCE":84},
    105 : {"NAME":"DUBE" , "GRADE":"C" , "ATTENDANCE":80} 
}
print(dictionary)

# UPDATING THE DICTIONARY.
dictionary[102]={"NAME":"TILAK" , "GRADE":"A+" , "ATTENDANCE":89}
print(dictionary)

# INSERTING THE DICTIONARY.
dictionary[106]={"NAME":"AKSHAR" , "GRADE":"B+" , "ATTENDANCE":92}
print(dictionary)

# DELETING THE DICTIONARY.
del dictionary[106]["ATTENDANCE"]
print(dictionary)

# UPDATING THE DICTIONARY.
dictionary.update({101 : {"NAME":"KULDIP" , "GRADE":"A+" , "ATTENDANCEE":90}})
print(dictionary)