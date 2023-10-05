def solution(string, ending):
    return string[-len(ending):] == ending

# Exemples de test
print(solution('abc', 'bc'))  # True
print(solution('abc', 'd'))   # False
