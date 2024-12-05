from django.shortcuts import render, redirect


def chat_Box(request, chat_box_name):
    return render(request, "chatbox.html", {"chat_box_name" : chat_box_name})

