#Assignment 1, Implement Apriori 
def readCSV(path):
    Trans = []
    file = open(path,'r')
    for line in file:
        line = line.replace('\n','')
        Trans.append(line.split(';'))
    return Trans

def generateC1(Trans):
    C1 = {}
    for record in Trans:    
        for item in record:
            if C1.has_key(item):
                C1[item] =C1[item] + 1
            else:
                C1[item] = 1
    return C1

def generateL1(Items):
    L1 = {}
    for item in Items:
        if(Items[item] > 771 ):
            L1[item] = Items[item]
    return L1

def generateCk(key_ksub1,k):
    Ck = []
    for i in range(len(key_ksub1)):
        l1 = key_ksub1[i]
        for j in range(i+1,len(key_ksub1)):
            l2 = key_ksub1[j]
            if k>2 :
                if l1[0:k-2] == l2[0:k-2] :
                    Ck_item = list(set(l1) | set(l2))
                    Ck_item.sort()
                    if isPruned(Ck_item,key_ksub1) == False :
                        Ck.append(Ck_item)
            else:
                item = []
                item.append(l1)
                item.append(l2)
                item.sort()
                Ck.append(item)
    return Ck
                

def isPruned(Ck_item,Lksub1):
    Items = Lksub1
    for item in Items:
        item.sort()
        if Ck_item[1:] == item:
            return False
    return True

def generateLk(Cksub1,Trans,min_support):
    Cksub1_count = []
    tmp = 0
    for comb in Cksub1:
        tmp+=1
        print(tmp)
        count = 0
        sC = set(comb)
        for record in Trans:
            sR =  set(record)
            if(sC.issubset(sR)):
                count += 1
        Cksub1_count.append(count)
    Cksub1_Freq = []
    Cksub1_count_Freq = []
    for i in range(len(Cksub1)):
        if (Cksub1_count[i] >= 771) :
            Cksub1_Freq.append(Cksub1[i])
            Cksub1_count_Freq.append(Cksub1_count[i])
    return Cksub1_Freq,Cksub1_count_Freq


if __name__ == '__main__':
    L2 = []
    Trans = readCSV('data/categories.txt')
    Ele1_Freq = open('1Ele-temp','r')
    for line in Ele1_Freq:
        L2.append(line.replace('\n',''))
    # C2 = generateCk(L2,2)
    # L2, L2_count = generateLk(C2,Trans,771)
    # print(len(L2))
    # print(L2)

    L2 = [['American (New)', 'Restaurants'], ['Beauty & Spas', 'Nail Salons'], ['Beauty & Spas', 'Hair Salons'], ['Breakfast & Brunch', 'Restaurants'], ['Restaurants', 'Sandwiches'], ['Pet Services', 'Pets'], ['Burgers', 'Fast Food'], ['Fast Food', 'Restaurants'], ['Home Services', 'Real Estate'], ['Restaurants', 'Sushi Bars'], ['Italian', 'Pizza'], ['Pizza', 'Restaurants'], ['Shopping', "Women's Clothing"], ['Home & Garden', 'Shopping'], ['Fashion', 'Shopping'], ['Coffee & Tea', 'Food'], ['Auto Repair', 'Automotive'], ['Active Life', 'Fitness & Instruction'], ['Nightlife', 'Pubs'], ['Bars', 'Pubs'], ['Nightlife', 'Sports Bars'], ['Bars', 'Sports Bars'], ['Doctors', 'Health & Medical'], ['Italian', 'Restaurants'], ['Event Planning & Services', 'Hotels & Travel'], ['Hotels', 'Hotels & Travel'], ['Bakeries', 'Food'], ['Food', 'Grocery'], ['Fashion', "Women's Clothing"], ['Cafes', 'Restaurants'], ['Burgers', 'Restaurants'], ['Dentists', 'General Dentistry'], ['General Dentistry', 'Health & Medical'], ['Food', 'Restaurants'], ['Food', 'Ice Cream & Frozen Yogurt'], ['Food', 'Specialty Food'], ['Nightlife', 'Restaurants'], ['Bars', 'Nightlife'], ['Dentists', 'Health & Medical'], ['Bars', 'Restaurants'], ['Mexican', 'Restaurants'], ['Chinese', 'Restaurants'], ['American (Traditional)', 'Restaurants'], ['Japanese', 'Restaurants'], ['Event Planning & Services', 'Hotels']]
    
    # C3 = generateCk(L2,3)
    # print(C3)
    
    C3 = [['Burgers', 'Fast Food', 'Restaurants'], ['Italian', 'Pizza', 'Restaurants'], ['Fashion', 'Shopping', "Women's Clothing"], ['Bars', 'Nightlife', 'Pubs'], ['Bars', 'Nightlife', 'Sports Bars'], ['Event Planning & Services', 'Hotels', 'Hotels & Travel'], ['Dentists', 'General Dentistry', 'Health & Medical'], ['Bars', 'Nightlife', 'Restaurants']]
    
    # L3,L3_Count= generateLk(C3,Trans,771)
    # print(L3,L3_Count)


    L3 = [['Burgers', 'Fast Food', 'Restaurants'], ['Italian', 'Pizza', 'Restaurants'], ['Fashion', 'Shopping', "Women's Clothing"], ['Bars', 'Nightlife', 'Pubs'], ['Bars', 'Nightlife', 'Sports Bars'], ['Event Planning & Services', 'Hotels', 'Hotels & Travel'], ['Dentists', 'General Dentistry', 'Health & Medical'], ['Bars', 'Nightlife', 'Restaurants']]
    
    C4 = generateCk(L3,4)
    print(C4)