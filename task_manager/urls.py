from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

tasks = []
completedTasks = []


def deleteTask(index):
    del tasks[index - 1]


def completeTask(index):
    completedTasks.append(tasks[index - 1])


def tasks_view(request):
    return render(request, "tasks.html", {"tasks": tasks})


def home_view(request):
    return render(request, "index.html", {"tasks": tasks, "completedTasks": completedTasks})


def completed_tasks_view(request):
    return render(request, "completedTasks.html", {
        "completedTasks": completedTasks})


def all_tasks_view(request):
    return render(request, "allTasks.html", {"tasks": tasks, "completedTasks": completedTasks})


def add_task_view(request):
    task_value = request.GET.get("task")
    tasks.append(task_value)
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, index):
    deleteTask(index)
    return HttpResponseRedirect("/tasks")


def complete_task_view(request, index):
    completeTask(index)
    deleteTask(index)
    return HttpResponseRedirect("/tasks")


urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path("manage/", admin.site.urls),
    path("", home_view),
    path("tasks/", tasks_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("complete_task/<int:index>/", complete_task_view),
    path("all_tasks/", all_tasks_view),
]
