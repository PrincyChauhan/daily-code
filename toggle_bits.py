# Josephislearningdigitallogicsubjectwhichwillbeforhisnextsemester.Heusually
#  triestosolveunitassignmentproblemsbeforethelecture.Todayhegotonetrickyquestion.
#  Theproblemstatementis“Apositiveintegerhasbeengivenasaninput.Convertdecimal
#  valuetobinaryrepresentation.Toggleallbitsofitafterthemostsignificantbitincludingthe
#  mostsignificantbit.Printthepositiveintegervalueaftertogglingallbits”.
#  Constrains
# 1<=N<=100
#  Example1:
#  Input:
# 10 -> Integer
#  Output :
#  5  ->result- Integer
#  Explanation:
#  Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which
#  represents “5”. Hence output will print “5”.


def toggle_bits(n):
    binary_representation = bin(n)[2:]
    print(binary_representation)
    
    toggled_binary = ""
    for bit in binary_representation:
        if bit == '0':
            toggled_binary += '1'
        else:
            toggled_binary += '0'
            
    result = int(toggled_binary, 2)
    return result


# Example usage
input_value = 10
output_result = toggle_bits(input_value)
print(output_result) 