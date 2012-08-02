class patch :
    init_from_index=0
    init_distance=0
    final_from_index=0
    final_distance=0
    pre_string=""
    deleted_string=""
    inserted_string=""
    post_string=""


def diff(init_string, final_string) :
    p1=0
    p2=0
    spatch=[]
    maxp1=len(init_string)
    maxp2=len(final_string)

    while True :
        if p1==maxp1 :
            #insert p2 to maxp2

            pat=patch()
            pat.init_from_index=p1+1
            pat.init_distance=0
            pat.final_from_index=p2+1
            pat.final_distance=maxp2-p2
            pat.pre_string=""
            pat.deleted_string=""
            pat.inserted_string=final_string[p2:]
            pat.post_string=""
            spatch+=[pat]
            break

        elif p2==maxp2 :
            pat=patch()
            pat.init_from_index=p1+1
            pat.init_distance=maxp1-p1
            pat.final_from_index=p2+1
            pat.final_distance=0
            pat.pre_string=""
            pat.deleted_string=init_string[p1:]
            pat.inserted_string=""
            pat.post_string=""
            spatch+=[pat]
            break

        else :
            if init_string[p1]==final_string[p2] :
                p1+=1
                p2+=1
            else :
                ff=False
                for j in range(p2+1,maxp2) :
                    if(init_string[p1]==final_string[j]) :
                        ff=True
                        pat=patch()
                        pat.init_from_index=p1+1
                        pat.init_distance=0
                        pat.final_from_index=p2+1
                        pat.final_distance=j-p2
                        pat.pre_string=""
                        pat.deleted_string=""
                        pat.inserted_string=final_string[p2:j]
                        pat.post_string=""
                        spatch+=[pat]
                        p2=j
                        break
                if not(ff) :
                    pat=patch()
                    pat.init_from_index=p1+1
                    pat.init_distance=1
                    pat.final_from_index=p1+1
                    pat.final_distance=0
                    pat.pre_string=""
                    pat.deleted_string=init_string[p1]
                    pat.inserted_string=""
                    pat.post_string=""
                    spatch+=[pat]
                    p1+=1
                            
    return spatch

def merge(spatch, cpatch, original) :
    s_sz=len(spatch)
    c_sz=len(cpatch)

    temp=""				# the final string
    arr=[]
    prev_len=0
    len1=0

    temp=original[0:spatch[0].init_from_index-1]

    for i in range(0,s_sz-1) :
        p=spatch[i]
        l1=p.final_distance-p.init_distance
        arr+=[[p.init_from_index+len(p.pre_string),l1]]

        len1=p.init_from_index-1
        str_len=len1+len(p.pre_string)
        
        for j in range(len1,str_len) :
            """print "original ",
            print temp
	    """
            temp+=original[j]
        
        temp+=p.inserted_string
        temp+=p.post_string

        if(i<s_sz-2) :
            for j in range(p.init_from_index+p.init_distance-1,spatch[i+1].init_from_index-1) :
                temp+=original[j]
        
        
        prev_len=len1+p.init_distance

    for i in range(prev_len, len(original)) :
        temp+=original[i]
    
    #print temp
    original=temp
    temp=""
    
    prev_len=0
    for i in range(0,c_sz-1) :
        p=cpatch[i]
        
        len1=p.init_from_index-1
        """
        while j<s_sz :
            if(arr[j][0]<len1+len(p.pre_string)) :
                print("sss\n")
                len1+=arr[j][1]
                j+=1
            else :
                break;
        """
        l=0
        l2=0
        for j in range (0,s_sz-1) :
            if(arr[j][0]<=len1+len(p.pre_string)) :
                if arr[j][1]+arr[j][0]>len1 :
                    l+=len1-arr[j][0]
                else :
                    l+=arr[j][1]
            else :
                break;
        
        #print l
        str_len=len1-prev_len+len(p.pre_string)
        
        for j in range(prev_len,len1) :
           temp+=original[j]
        len1+=l
        temp+=p.inserted_string
        temp+=p.post_string
        prev_len=len1+p.init_distance
        #print(temp)
        
    l=0
    for j in range (0,s_sz-1) :
        if(arr[j][0]<=cpatch[c_sz-2].init_from_index-1+len(cpatch[c_sz-2].pre_string)) :
            l+=arr[j][1]
        else :
            break;
    
    for i in range(cpatch[c_sz-2].init_from_index-1+l, len(original)) :
        temp+=original[i]
    
    ##now set the temp
    return temp

def main() :
    str1=str(raw_input())
    str2=str(raw_input())
    str3=str(raw_input())
    arr=diff(str1,str2)
    arr2=diff(str1,str3)
    final=merge(arr,arr2,str1)
    print final

if __name__=="__main__" :
    main()
