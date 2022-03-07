# import ReGex module
import re

# read file 
def read_template(file):
    """F() to take data from template file"""
    with open(file, 'r') as f:
        template = (f.read())
        return template

# call read_file() to read the template_madlib file
template_file = read_template('assets/template.txt')

# akes in a template string and returns 
# a string with language parts removed and a separate list of those language parts.
def parse_template(pattern, template):
    """F()to run regex pattern over the template and extract all words to array prompts"""
    prompts = re.findall(pattern, template)
    return prompts

def empty_template(pattern, template):
    """F() to extract all {words} from the template using pattern"""
    template = re.sub(pattern, "{}", template)
    return template



# returns a string with the language parts inserted into the template.
#also called in the handle IO the hand
def merge():
    """Print prompts to user and return array of users inputs"""
    user_words = []
    for el in parse_template("\{[a-zA-Z0-9\' -]*\}", template_file):
        user_word = input(f'Give me {el[1:-1]}: -----> ')
        user_words.append(user_word)
    return user_words

# merge takes in a “bare” template and a list of user entered language parts, 
# calls the merge function
def handle_IO():
    """F() to output welcome message and rules of the game to the screen"""

    # ask if user wants to play
    if input("\n***************************************\n**** Welcome to the Mad Libs Game! ****\n \n Mad Libs is a phrasal template word game\n where user(you) need to input different\n words following prompts. At the end you\n will get a story that was created\n using your inputs.\n \nPlease type 'y' if you want to play:\n") == "y":

        # store return from print_promts()
        user_words = merge()

        # store the empty template in new var
        template = empty_template("\{[a-zA-Z0-9\' -]*\}", template_file)

        # return template formated with users inputs
        formatted_template = f'\nHere is your story:\n-------------------\n{template.format(*user_words)[22:]}'

        # print results to user
        print(formatted_template)

        return formatted_template



def write_file(file, contents):
    """F() to write program results to the file"""
    with open(file, 'w') as f:
        template = (f.write(contents))

# write the completed story template to the new file
write_file('madlib_result.txt', handle_IO())