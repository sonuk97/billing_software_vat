from .models import *
from datetime import datetime, date, timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from .views import *
from django.contrib.auth.models import User, auth

def checkTrialStatus(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        if not user.is_staff:
            status = ClientTrials.objects.get(user = request.user)
            if status.purchase_status == 'null' and status.trial_status == True:
                exp_days = (status.end_date - date.today()).days
                if exp_days < 0:
                    status.trial_status = False
                    status.save()
                    messages.warning(request, 'Your Trail Period has been expired, Contact Admin..!')
                    auth.logout(request)
                    return redirect(login)
            elif status.purchase_status == 'null' and status.trial_status == False:
                messages.warning(request, 'Your Trail Period has been expired, Contact Admin..!')
                auth.logout(request)
                return redirect(login)
            elif status.purchase_status == 'cancelled':
                messages.warning(request, 'Your Subscription has been cancelled, Contact Admin..!')
                auth.logout(request)
                return redirect(login)
            elif status.purchase_status == 'valid':
                sub_exp_days = (status.purchase_end_date - date.today()).days
                if sub_exp_days < 0:
                    status.purchase_status = 'expired'
                    status.save()
                    messages.warning(request, 'Your Subscription Period has been expired, Contact Admin..!')
                    auth.logout(request)
                    return redirect(login)
            return {'status':True}
        return {'status':False}
    return {'status':False}

def checkTrialStatusAdmin(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        if user.is_staff:
            trials = ClientTrials.objects.all()
            for status in trials:
                if status.purchase_status == 'null' and status.trial_status == True:
                    exp_days = (status.end_date - date.today()).days
                    if exp_days < 0:
                        status.trial_status = False
                        status.save()
                        # return {'status':True}
                elif status.purchase_status == 'valid':
                    sub_exp_days = (status.purchase_end_date - date.today()).days
                    if sub_exp_days < 0:
                        status.purchase_status = 'expired'
                        status.save()
                        # return {'status':True}
                # return {'status':True}
        return {'status':False}
    return {'status':False}

def trial_status(request):
    if request.user.is_authenticated:
        # status = ClientTrials.objects.get(user=User.objects.get(id = request.user.id))
        user = User.objects.get(id = request.user.id)
        if not user.is_staff:
            status = ClientTrials.objects.get(user = request.user)
            if status.purchase_status == 'null' and status.trial_status == True and status.subscribe_status != 'yes':
                exp_days = (status.end_date - date.today()).days
                if exp_days <= 10:
                    context = {
                        'notification':True,
                        'days':exp_days,
                    }
                    return context
                else:
                    return {'notification':False}
            elif status.purchase_status == 'null' and status.trial_status == True and status.subscribe_status == 'yes':
                exp_days = (status.end_date - date.today()).days
                if exp_days <= 10:
                    context = {
                        'notification':True,
                        'days':exp_days,
                        'subscribe':True,
                    }
                    return context
                else:
                    return {'notification':False}
            else:
                return {'notification':False}
        return {'notification':False}
    else:
        context = {
            'notification':False,
        }
        return context
    
def renewStatus(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        if user.is_staff:
            renewals = ClientTrials.objects.filter(subscribe_status = 'yes')
            if not renewals:
                return {'notification':False}
            else:
                context = {
                    'notification':True,
                    'renewals':renewals,
                }
                return context
        return {'status':False}
    else:
        return {'notification':False}
    
def endDate(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        if not user.is_staff:
            status = ClientTrials.objects.get(user = request.user)
            if status.purchase_status == 'valid':
                date = status.purchase_end_date    
                return {'endDate':date}
            else:
                return {'endDate':False}
        return {'endDate':False}
    else:
        return {'endDate':False}