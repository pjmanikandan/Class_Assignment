class mani1stFunction():
    
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    
    def OddEven():
        num=int(input("Enter a number:")) 
        if num%2==0:
            print(num ,"is Even number")

        else:
            print(num ,"is Odd number")
    
        return num
    
    
    def Elegible():
        gender=(input("Your Gender:"))
        age=int(input("your Age:"))
        if age<19:
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")
            
            
    def percentage ():
        A=int(input("Subjec1:"))
        B=int(input("Subjec2:"))
        C=int(input("Subjec3:"))
        D=int(input("Subjec4:"))
        E=int(input("Subjec5:"))
        num=A+B+C+D+E
        print("Total:",num)
        X=(num/500)*100
        print("Percentage:",X)
    
     
    def triangle ():
            A=int(input("Height:"))
            B=int(input("Breadth:"))
            print("Area formula: (Height*Breadth)/2")
            c=(A*B)
            area=c/2
            print("Area of Triangle:",area)
            D=int(input("Height1:"))
            E=int(input("Height2:"))
            F=int(input("Breadth:"))
            print("Perimeter formula: Height1+Height2+Breadth")
            tri=D+E+F
            print("Perimeter of Triangle:",tri)