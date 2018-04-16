from keras.models import load_model  
import re
import numpy as np
#from models import model_from_json
model = load_model('antigen.h5')  


json_string = model.to_json()
print(json_string)

def word2vector(seq):
    aai = {}
    aas = "ACDEFGHIKLMNPQRSTVWY"
    aa2ary = {}
    i = 0
    for aa in list(aas):
    	aai[aa] = i
    	i = i+1
    ori = [0] * 20
    aa2ary[" "] = ori
    for aa in list(aas):
    	tmp = ori[:]
    	tmp[aai[aa]] = 1
    	# print(tmp)
    	aa2ary[aa] = tmp
    seq = seq.upper()
    if not re.match('^[ACDEFGHIKLMNPQRSTVWY]+$', seq):
        print("Invalid sequence")
        return 
    seq = list(seq)
    if len(seq)>30:
        print("Lenght is greater than 30aa")
        return
    tmp = []
    seq = seq + [" "] * (30-len(seq))
    for aa in seq:
        tmp = tmp + aa2ary[aa]
    return tmp

def get_score(xx):
    values = [5.5,5.4,5.3,5.2,5.1,5.0,4.9,4.8,4.7,4.6,4.5,4.4,4.3,4.2,4.1,4.0,3.9,3.8,3.7,3.6,3.5,3.4,3.3,3.2,3.1,3.0,2.9,2.8,2.7,2.6,2.5,2.4,2.3,2.2,2.1,2.0,1.9,1.8,1.7,1.6,1.5,1.4,1.3,1.2,1.1,1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0,-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1.2,-1.3]
    ary = list(xx)
    for i in range(len(ary)):
        if ary[i] == max(ary):
            return values[i]
   
X_test = word2vector("ALTLVAGKLTH")
# #print(X_test)
X = np.array(X_test)
data = [X,]
XX = np.array(data)
#print(XX)
xx = model.predict(XX)
for x in xx:
    #print(x)
    print(get_score(x))
    break;
