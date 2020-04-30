st = 'i havent worked out yet'
ar = {}
for ch in st.upper(): # .upperconverts all the characters to uppercase
     ar.setdefault(ch,0)
     ar[ch] += 1

print(ar)
