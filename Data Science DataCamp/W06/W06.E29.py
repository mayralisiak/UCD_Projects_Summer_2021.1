#"""For instance, you could tag a bunch of image transforming functions, and then write code that searches for all of the functions that transform images and apply them, one after the other, on a given input image."""

from functools import wraps

def tag(*tags):
      # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)