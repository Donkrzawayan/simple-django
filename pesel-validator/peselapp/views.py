from django.shortcuts import render

from .utils import validate_pesel
from .forms import PeselForm


def pesel_validator_view(request):
    result = None
    details = None
    if request.method == "POST":
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data["pesel"]
            details = validate_pesel(pesel)
            if details:
                result = "Poprawny numer PESEL"
            else:
                result = "Niepoprawny numer PESEL"
        else:
            result = "Niepoprawny format PESEL"
    else:
        form = PeselForm()
    return render(request, "peselapp/index.html", {"form": form, "result": result, "details": details})
