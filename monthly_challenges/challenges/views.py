from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for 30 minutes every day!",
    "april": "Read a new book every week!",
    "may": "Practice meditation for 10 minutes every day!",
    "june": "Go for a run every morning!",
    "july": "Take a photo every day!",
    "august": "Write in a journal every night!",
    "september": "Learn a new language for 30 minutes every day!",
    "october": "Cook a new recipe every week!",
    "november": None,
    "december": "Reflect on the year and set goals for the next year!"
}

def index(request):
    response_data = """
    <ul>
    """
    for month in monthly_challenges.keys():
        month_path = reverse("monthly-challenge", args=[month])
        response_data += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"
    response_data += "</ul>"
    return render(request, "challenges/index.html", {"monthly_challenges": monthly_challenges})

def monthlyChallenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return render(request, "404.html")
    return render(request, "challenges/challenge.html", {"challenge": challenge_text, "month_name": month })

def monthlyChallengeByNumber(request, month):
    months = list(monthly_challenges.keys())
    if month > 0 and month <= len(months):
        redirect_month = months[month - 1]
        return monthlyChallenge(request, redirect_month)
    else:
        return HttpResponseNotFound("This month is not supported!")

