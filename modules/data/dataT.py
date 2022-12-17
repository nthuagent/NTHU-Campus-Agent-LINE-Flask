from API import DataAPI

data = DataAPI()


def get_epid(by):
    res, err = data.getEpid(by)
    if err:
        return None
    return res


def get_rec_news(by):
    res, err = data.getrecNews(by)
    if err:
        return None
    return res
