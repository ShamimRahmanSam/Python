w = 'Yo bro'                                            # text types words er upre ' ' or " " eta use korte hoy.

n = 50                                                  # numbers types int er number positive or negative hote pare. -50 holeo eta int.int er upor quotati on " " / ' ' lagena.
zf = 10.7                                               # numbers types e Float can also be scientific numbers with an "e" to indicate the power of 10.just like x = 35e3, y = 12E4, z = -87.7e100. egulo sob float...float mane ekhane dhoshomik bujhay onno language er mtoi.. pos & neg hote pare. -10.7 ow float e
c = 8487489747938478374974397494934j                    # numbers types e  Complex numbers are written with a "j" as the imaginary part:..complex variable e j chara r alphabet kaj krena. eksthe na likhe emn ekta j number er sthe use krle output show krbe. r number evabe jtot mon chay deya jay but agei dite hbe j er r hae extra eto nmbr use krle output ektu onnorokom ashe .check out, r hae x = 3+5j, y = 5j, z = -5j egulo sob e complex. majhe + ow use kora jay but last e j l;agbei as complex

b = True                                                # boolean types bool(jekono number dilei    TRue bolbe) but 0 dile false bolbe..r nahoyb evabe likhte hbe. er jnne evabe TRue False nite hoy. t r f must be capital hote hobe true likhle hbena. True likhlei hbe

by = b'jvgvgjcfdsfjsz'                                  # binary types bytes er jnne variable neyar por b diye ' ' / " " diye vitre ja mon chay lkha jabe
ba = bytearray(50)                                      # binary types er bytearray evabe likhe 1st bracket er vitre bakita likhte hbe.
mv = memoryview(bytes(30))                              # binary types er memoryview er jnne memoryview evabe likhe bytes likhte hbe then 1st bracket er vitre nmbr or words likhte hbe

r = range(8)                                            # Sequence Types er range er jnne etay output ashbe 0, 8

l = ['apple', 'banana', 'orange', 'mango']              # Sequence Types e list er jnne 3rd bracket

t = ('apple', 'banana', 'orange', 'mango')              # Sequence Types e tuple er jnne 1st bracket

s = {'apple', 'banana', 'orange', 'mango'}              # Set Types er set er jnne 2nd bracket

fs = frozenset({'apple', 'banana', 'orange', 'mango'})  # Set Types er frozenset er jnne aqage 1st bracket then emn 2nd bracket use korte hoy

d = {'name' : 'Sam', 'age' : 36}                        # Mapping type er dictionaryr jnne 2nd bracket use korte hoy and majhe emn kichu krte gele  :  usekorte hoy


print (w)                                               # variable set korle seta print er time " " use krte hoyna.
print (n)
print (zf)
print (c)
print (b)
print (by)
print(ba)
print(mv)
print (r)
print (l)
print (t)
print (s)
print (fs)
print (d)


print (type(w))                                          # kono variable or datar data type jante hole evabe ber korte hoy type keyword use kore.
print (type(n))
print (type(zf))
print (type(c))
print (type(b))
print (type(by))
print (type(ba))
print (type(mv))
print (type(r))
print (type(l))
print (type(t))
print (type(s))
print (type(fs))
print (type(d))


"""If we want to specify the data type, 
you can use the following constructor functions:

x = str("Hello World")	                                str
x = int(20)	                                            int
x = float(20.5)	                                        float
x = complex(1j)	                                        complex
x = list(("apple", "banana", "cherry"))    	            list
x = tuple(("apple", "banana", "cherry"))	            tuple
x = range(6)	                                        range
x = dict(name="John", age=36)	                        dict
x = set(("apple", "banana", "cherry"))	                set
x = frozenset(("apple", "banana", "cherry"))	        frozenset
x = bool(5)	bool
x = bytes(5)	                                        bytes
x = bytearray(5)	                                    bytearray
x = memoryview(bytes(5))	                            memoryview    """