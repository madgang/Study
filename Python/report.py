def get_descript():
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain','snow','sleet','fog','sun','who knows']
    
    return choice(possibilities)
