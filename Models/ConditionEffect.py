from Constants.StatusEffects import *

def hasEffect(condition, *effects):
    bits = 0
    for effect in effects:
        bits |= 1 << effect-1
    return (condition & bits) != 0
