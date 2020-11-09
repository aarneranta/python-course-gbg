
# Om man vill byta värden mellan två variabler måste man i många språk 
# göra såhär
x = 1
y = 2
tmp = x
x = y
y = tmp

# Men python har "simultanious assignment". Det innebär att man kan skriva
x, y = 1, 2
# eller
x, y = (1, 2)
# eller
x, y = [1, 2]

# Och det som är nice är att python utvärderar högerledet helt innan vänsterledet assignas, vilket gör att ett uttryck som 
x, y = y, x
# Fungerar precis som vi förväntar oss. 
