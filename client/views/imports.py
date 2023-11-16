from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.http import JsonResponse

from client.models import User as ProjectUser

import datetime

User: ProjectUser = get_user_model()
