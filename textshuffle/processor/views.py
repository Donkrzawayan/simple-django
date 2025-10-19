from django.shortcuts import render
from .utils import shuffle_text


def upload_view(request):
    if request.method == "POST" and request.FILES.get("textfile"):
        file = request.FILES["textfile"]
        text = file.read().decode("utf-8")
        result_text = shuffle_text(text)
        return render(request, "processor/result.html", {"result_text": result_text})
    return render(request, "processor/upload.html")
