from django import template

register = template.Library()

def getAmountContext(amount, word, infix=''):
    if amount:
        if abs(amount) > 1:
            if word.endswith('y'):
                word = '{name}ies'.format(word=word[-1])
            else:
                word += 's'
        amount_string = '{amount} {infix} {word}'.format(amount=amount, infix=infix, word=word)
        return amount_string

@register.simple_tag
def getAmount(amount, word, infix=''):
    amountContext = getAmountContext(amount, word, infix=infix)
    if amountContext:
        return amountContext
    amount_string = 'no {infix} {word}s'.format(word=word, infix=infix)
    return amount_string
