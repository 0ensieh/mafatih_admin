from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.db.models import Prefetch
from django.shortcuts import render, redirect, reverse

from prayer.models import *

import json
