#Operational Precendence

x = 4
y = 7
z = 6

'''
hasil = x+y+z
print(hasil)
print (x,'+',y,'+',z,'=', hasil)

hasil = x**10+20/5-y*z
print(x,'**',10,'+',20,'/',5,'-',y,'*',z,'=',hasil)
'''

'''  ---------------------------------------------------------------------------
1. ()
2. Exponen **
3. Multiply  and Division * / ** % //
4. sum and sub + -
'''

'''  ---------------------------------------------------------------------------

#Contoh Conversi Suhu
suhu_c = float(input('berapa suhunya ? :'))
print('suhu sekarang adalah', suhu_c,'celcius')

suhu_r = round((4/5) * suhu_c)
print('dalam reamur adalah :', suhu_r, 'reamur')

#rumus suhu => F = (9/5*celcius)+32
suhu_f = ((9/5)*suhu_c)+32
print ('((9/5)*',suhu_c,')+32','=',suhu_f)
print ('suhu dalam satuan Fahrenheit adalah ',suhu_f,' Fahrenheit')

#rumus C ke K            K=C+273.15          C=K-273.15

suhu_k = suhu_c + 275.15
print(suhu_c,'Celcius','+ ''275.15','=',suhu_k,"Kelvin")

'''

#F to K
#F = (9/5*celcius)+32
f=float(input("Suhu dalam F? "))
#f = (9/5*c)+32
#(f-32)*5/9 = c
c = (f-32)*5/9
print('dalam Celcius adalah',c,' Celcius')

#K to F
#K=C+273.15
k=(c+273.15)
print('kalau dalam Kelvin suhunya :',k,'Kelvin')

print('Suhu :',f,'Fahrenheit','=',c,'Celcius','=',k,'Kelvin')