# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:01:00 2022

Background:
Nowadays there are many AI models can counting number of objects, but they are mostly based on
object detection or segmentation. Therefore AI models are learning what are "objects" but not
"numbers". For example, a model can know what is apple and telling people there are two apples
in a picture, but it does not know what is "two". It was people defined what is "two", such as
"having two bounding boxes means having two objects" and AI models just directly use the 
definition for presenting results. Hence we want to know whether it is feasible to let AI know 
the meaning of numbers.

Goal of this project:
We are trying to teach AI model to understand the meaning of numbers, starting with 1 and 2.
We expect to train a model being able to know there are "1 thing in a picture" or "2 things
in a picture".  

Possible experiment designs:
Design #1:
    1, Collect dataset with two classes: One class contain "One object", the other contains
    "Two objects". The objects should belong to different categories with very different feature, 
    like apple, boat, car, people.
    2, Train a classification model with the above two classes. The accuracy is expected to be ~0.5
    3, Adjust the feature extractor, target output, lost function, training strategy, etc. and 
    retry to get an accuracy >= 0.85


@author: Wen Wen
"""



