str = 'X-DSPAM-Confidence: 0.8475'

colon_index = str.find(':')     
float_str = str[colon_index+1:]
float_val = float(float_str)

print(float_val)
