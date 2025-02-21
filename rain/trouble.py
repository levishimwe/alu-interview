def triple_trouble(num1, num2):
    
    str1 = str(num1)
    str2 = str(num2)
    
    
    for digit in '0123456789':
        
        for i in range(len(str1)-2):
            if str1[i] == str1[i+1] == str1[i+2] == digit:
                
                for j in range(len(str2)-1):
                    if str2[j] == str2[j+1] == digit:
                        return 1
    
    return 0


def test_triple_trouble():
    test_cases = [
        (451999277, 41177722899),  
        (1222345, 12345),          
        (12345, 12345),            
        (888, 77),                 
        (88888, 88888),           
        (12312312, 123),           
    ]
    
    for num1, num2 in test_cases:
        result = triple_trouble(num1, num2)
        print(f"triple_trouble({num1}, {num2}) -> {result}")


if __name__ == "__main__":
    test_triple_trouble()