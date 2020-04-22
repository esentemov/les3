products = "skovorodki skovorodka chainick kniga pampersi"

sizes = ['xs', 'xl', 'xxl']

product_arr = products.split()
print(product_arr)
skovorodki = []
skovorodki_all_sizes = []
for word in product_arr:
    if word.startswith("sko") == True:
        skovorodki.append(word)

print(skovorodki)
for skovorodka in skovorodki:
    for size in sizes:
        skovorodki_all_sizes.append(skovorodka+"_"+size)

print(skovorodki_all_sizes)