from num2words import num2words

print(sum([len(num2words(n).replace(',', '').replace('-', '').replace(' ', '')) for n in range(1, 1001)]))