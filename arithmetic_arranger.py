import re

def arithmetic_arranger(problems, display_answer=False):
  """
  This function receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function optionally takes a second argument. When the second argument is set to True, the answers will be displayed.
  """

  if len(problems) > 5:
    return 'Error: Too many problems.'

  top = bottom = divider = answer = str()

  for problem in problems:
    try:
      operator = re.findall('\ ([+-])\ ', problem)[0]
    except:
      return "Error: Operator must be '+' or '-'."

    values_str = list(i.strip() for i in problem.split(operator))

    try:
      values_int=[int(i) for i in values_str]
    except:
      return 'Error: Numbers must only contain digits.'

    if len(values_str[0]) > 4 or len(values_str[1]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    
    ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}
    
    result = ops[operator](values_int[0], values_int[1])


    n = 2 + max(len(values_str[0]), len(values_str[1]))
    top = top + " "*(n - len(values_str[0])) + values_str[0] + " "*4
    bottom = bottom + operator + " "*(n - 1 - len(values_str[1])) + values_str[1] + " "*4
    divider = divider + "-"*n + " "*4
    answer = answer + " "*(n - len(str(result))) + str(result) + " "*4
    

  arranged_problems = top.rstrip() + "\n" + bottom.rstrip() + "\n" + divider.rstrip()

  if display_answer:
    arranged_problems = arranged_problems + "\n" + answer.rstrip()
  
  return arranged_problems