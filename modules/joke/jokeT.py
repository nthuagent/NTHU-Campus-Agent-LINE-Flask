from API import AndxAPI

def get_joke():
    andx = AndxAPI()
    anecdote, err = andx.getOne()
    if err:
        return None
    return anecdote
