import pickle
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import re
import gender_guesser.detector as gender
from multiprocessing import Pool
from tqdm import tqdm
from functools import partial

d = gender.Detector()

def find_first_woman_index(gender_list, gender = "female"):  #returns the index or nan if there are no women in the credits
    try:
        index_f = (gender_list.index(gender))
    except:
        index_f = np.inf
    try:
        index_mf = (gender_list.index("mostly_"+gender))
    except:
        index_mf = np.inf

    if index_f < index_mf:
        index = index_f
    else:
        index = index_mf

    if index == np.inf:
        index = np.nan

    return index

def get_gender_list(imdb_id, gender = "female"):
    r = requests.get(f"https://www.imdb.com/title/{imdb_id}/fullcredits?ref_=tt_ov_st_sm")
    soup = bs(r.text, 'html.parser')
    table = soup.find('table', class_='cast_list')
    first_name = 'img alt="[\w]+'
    if table is not None:
        m = re.findall(first_name, table.decode())
        gender_list = [d.get_gender(s.replace('img alt="', "")) for s in m]  #we find the gender of the person using a gender detector package
        return [imdb_id, find_first_woman_index(gender_list, gender)+1]

    else:
        return [imdb_id, "no-cast"]


data_folder = '../data/'
pickle_folder = data_folder + 'pickles/'

movies = pickle.load(open(pickle_folder + 'movies.p', 'rb'))

imdb_id = movies.IMDB_id.dropna()
imdb_id = list(imdb_id)[:1000]
total_len = len(imdb_id)

if __name__ == '__main__':
    with Pool(4) as p:
        collection = list(tqdm(p.imap(partial(get_gender_list, gender="male"), imdb_id), total=total_len, smoothing=1.0))
    pickle.dump(collection, open(pickle_folder + f'women_appearance.p', 'wb'))


if __name__ == '__main__':
    with Pool(4) as p:
        collection = list(tqdm(p.imap(get_gender_list, imdb_id), total=total_len, smoothing=1.0))
    pickle.dump(collection, open(pickle_folder + 'women_appearance.p', 'wb'))