class Sol:
    def remove_element(self,list,val):
        element=0
        for i in range(len(list)):
            if list[i]!=val:
                element+=1
        return element
if __name__ == '__main__':
    list=[3,2,2,2,3]
    val=3
    p1=Sol()
    print(p1.remove_element(list, val))
