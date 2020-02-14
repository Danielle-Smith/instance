class Website:
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title')# instance attribute belongs to the instance 
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)


class DifferentWebsite:
  title = 'My Class Title' # class attribute hard coded into the class 

dw = DifferentWebsite()
print(dw.title) # cant call print(dw.__dict__)

dw_two = DifferentWebsite()
print(dw_two.title)

# --------
# intro to inheritance- ability to create specialized versions of classes

class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self): # expects self as the only argument
    return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User): # to use inheritance ask yourself if this is new element a type of your other class. Pass in the other class you want to inherit in this case 'user'
  def active_users(self):
    return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
print(tiffany.greeting()) # this has access to the user class and greeting and all that the parent class has
print(kristine.active_users())

#  ------

# using polymorphism to build an html generator- poymorphism - Which means it can have many changes or one item can have many forms.

class Html: # don't want anyone to call this class. This is an abstract class and has the sole purpose of holding and storing shared behavior and the child classes are going to be the ones that are called.
    def __init__(self, content):
        self.content = content

    def render(self):             
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

for tag in tags:
    print(str(tag) + ': ' + tag.render()) # shows content with object/debugging
    #print(tag.render()) prints out content 

# ---------

# Building polymorphic functions
# without the abstract class- if you have a lot of shared behavior then use the inheritance method - if you don't then use code below

class Heading:
    def __init__(self, content):
      self.content = content

    def render(self):
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

div_one = Div('Some content')
heading = Heading('My Amazing Heading')
div_two = Div('Another div')

def html_render(tag_object):
  print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)