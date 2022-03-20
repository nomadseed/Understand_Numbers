# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:01:00 2022

Background:
Nowadays there are many AI models can counting number of objects, but they are mostly based on
object detection or segmentation. Therefore AI models are learning what are "objects" but not
"numbers". For example, a model can know what is apple and telling people there are two apples
in a picture, but it does not know what is "two". It was people defined what is "two" and AI
models just directly use the definition for presenting results. Hence we want to know whether 
it is feasible to let AI know the meaning of numbers.

Goal of this project:
We are trying to teach AI model to understand the meaning of numbers, starting with 1 and 2.
We expect to train a model being able to know there are "1 thing in a picture" or "2 thing
in a picture".  


@author: Wen Wen
"""

