#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render

def home(request, template='info/base.html'):
    return render(request, template, {'test' : 'test test test'})

