def banner():
    """Display program name"""
    message = 'The wonderful camelCase program!!!!!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

def main():
    banner()

main()