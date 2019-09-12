
osnovica = 40000
polugodisnjiK = 0.17+1.9+0.13+1.02+0.78+0.67
print("Polugodisnji koeficijent iznosi: "+str(polugodisnjiK))
july = 0.67
august = 0.35
september = 1.18
october = 0.20
november = 0.66
december = 1

total = polugodisnjiK + july + august + september + october + november + december

print("Ukupni godisnji koeficijent iznosi: "+str(total))

bonus = total * osnovica/10

print("Bonus iznosi: "+str(bonus))
   
