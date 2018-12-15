# author => vishnugopireddy
# Binary Representation of Number with 14 bits
def binary(num):
    '''

    :param num: num which has to be converted to binary
    :return: Binary Representation
    '''
    return(format(num,'014b')) #convert to binary


kases = int(input())
for kase in range(kases):
    num = int(input())
    print(binary(num))
