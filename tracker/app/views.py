from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app/index.html")

def calculate(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        time_spent = int(request.POST.get("time_spent"))
        life_expectancy = int(request.POST.get("life_expectancy"))

        years_left = life_expectancy - age
        hours_left = years_left * 8760
        hours_wasted = time_spent * 365 * years_left
        years_wasted = hours_wasted * 0.000114155

        return render(request, "app/results.html", {
            "age": age,
            "time_spent": time_spent,
            "life_expectancy": life_expectancy,
            "years_left": years_left,
            "years_wasted": years_wasted,
            "hours_left": hours_left,
            "hours_wasted": hours_wasted,
        })