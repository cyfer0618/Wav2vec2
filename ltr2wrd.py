file_name = "train.ltr"
tfile = open("train.wrd", 'w+', encoding='utf-8')
with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
	for line in f:
		word = line.replace(" ","")
		new_word = word.replace("|"," ")
		word = new_word.replace("  "," ")
		tfile.write(word)

