
def export_layers(img, parent, cat, num = 0, t = ''):
	name = parent.name.replace("'", '`')
	res = t + "{name:'" + name + "', w:" + str(parent.width) + ', h:' + str(parent.height) + ', x:' + str(parent.offsets[0]) + ', y:' + str(parent.offsets[1])
	if hasattr(parent, 'layers'):
		res = res + ', items: ['
		os.makedirs(cat + '/' + str(num))
		ttt = False
		n = 0
		for layer in parent.layers:
			if ttt: res = res + ','
			ttt = True
			res = res + '\n' + export_layers(img, layer, cat + '/' + str(num), n, t + '    ')
			n = n + 1
		res = res + ']'
	else:
		src = cat + '/' + str(num) + '.png'
		pdb.file_png_save(img, parent, src, '', 0, 9, 1, 1, 1, 1, 1)
		res = res + ', img:"' + src + '"'
	res = res + '}'
	return res

def export_img(img, cat):
	res = ''
	n = 0
	for layer in img.layers:
		if not res == '': res = res + ',\n'
		res = res + export_layers(img, layer, cat, n)
		n = n + 1
	with open(cat + "/index.js", "w") as text_file:
		text_file.write('var psd = [' + res + '];')

export_img(dupe, 'psd')

dupe = gimp.image_list()[0].duplicate()

print(export_layers(dupe, dupe.layers[0], 'psd2png'))
export_layers(dupe, dupe.layers[0], 'psd2png')		
for layer in dupe.layers:
	export_layers(dupe, layer, 'psd2png')