from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import os

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


questions = [
  {
    'type': 'checkbox',
    'message': 'Select toppings',
    'name': 'toppings',
    'choices': [
      Separator('= The Meats ='),
      {
          'name': 'ls command'
      },
      {
          'name': 'create dir'
      },
      {
          'name': 'poetry init'
      },
    ],
    'validate': lambda answer: 'You must choose at least one topping.'
    if len(answer) == 0 else True
  }
]

answers = prompt(questions, style=style)

if 'ls command' and 'create dir' and 'poetry init' in answers['toppings']:
  os.system('mkdir dir')
  os.system('cd dir/ && poetry init')