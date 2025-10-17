
from django.shortcuts import render

def shuffle_word(word):
	if len(word) <= 3:
		return word
	middle = list(word[1:-1])
	import random
	random.shuffle(middle)
	return word[0] + ''.join(middle) + word[-1]

def shuffle_text(text):
	import re
	def repl(match):
		return shuffle_word(match.group(0))
	return re.sub(r'\b\w+\b', repl, text)

def upload_view(request):
	if request.method == 'POST' and request.FILES.get('textfile'):
		file = request.FILES['textfile']
		text = file.read().decode('utf-8')
		result_text = shuffle_text(text)
		return render(request, 'processor/result.html', {'result_text': result_text})
	return render(request, 'processor/upload.html')

