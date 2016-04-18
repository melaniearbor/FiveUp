from django import template
import random

register = template.Library()

@register.simple_tag
def pet_name():
    pet_names = ['happy little shark', 'shimmery merperson', 'delicous ham sandwich',
    'button-nosed field mouse', 'shiny little june bug', 'titan, you', 'sweet little croissant',
    'lovely little poppy', 'graceful forrest moose', 'champion of the day', 'hero of tomorrow']
    pet_name = random.choice(pet_names)
    return pet_name


@register.simple_tag
def adjective():
    adjectives = ['an unbelievably snazzy', 'a romp-roarin\'', 'a fresh-smelling', 'a fantastic',
    'a stupendous', 'a shockingly awesome', 'a super terrific']
    adjective = random.choice(adjectives)
    return adjective

@register.simple_tag
def compliment():
    compliments = ['amazing', 'spectacular', 'dashing, like a superhero', 'svelt',
    'lovely', 'terribly attractive', 'so very smart', 
    'wise, like an owl', 'sparkly' ]
    compliment = random.choice(compliments)
    return compliment

