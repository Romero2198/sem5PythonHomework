def RLE(input_str):
    encoded_string = []
    i = 0
    while i <= (len(input_str) - 1):
        count = 1
        ch = input_str[i]
        j = i
        while j < (len(input_str) - 1):
            if input_str[j] == input_str[j + 1]:
                count += 1
                j += 1
            else: 
                break
        encoded_string.append((ch, str(count)))
        i = j + 1
    return encoded_string
def inverse_function(fin_list):
    inverse_str = ''
    for i in range(len(fin_list)):
        x = fin_list[i]
        inverse_str += x[0] * int(x[1])
    return inverse_str
input_str = open('sem1.txt').read()
fin_list = RLE(input_str)
inverse_str = inverse_function(fin_list)
data = open('sem2.txt', 'w')
data.writelines(str(fin_list))
data.close()
data = open('sem3.txt', 'w')
data.writelines(inverse_str)
data.close()