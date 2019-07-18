def stars(fn):
    def inner_fun(*args):
        out = "*" + fn(*args) + "*"
        return out
    return inner_fun


def colorize(color_name):
    colormap = {'red': 1, 'green': 2, 'yellow': 3, 'blue': 4, 'purple': 5, 'cyan': 6, 'grey': 7}
    def color(fn):
        def inner(*args):
            res = fn(*args)
            color_code = colormap[color_name]
            res = "\033[3" + str(color_code) + ";1m" + res + "\033[0m"
            return res
        return inner
    return color



# res = stars(echo)("Hello")
@stars
def echo(s):
    return s


# res = colorize('red')(echo)("Hello")
@colorize('red')
def echo(s):
    return s


# res = stars(colorize('red')(echo))("Hello")
@stars
@colorize('red')
def echo(s):
    return s


# res = colorize('red')(red(echo))("Hello")
@colorize('red')
@stars
def echo(s):
    return s

res = echo("Hello")
print(res)

# print(echo("Hello"))