def transform_recs(all_recs, dates):
    d = {date: [] for date in dates}

    for rec in all_recs:
        date = rec[1]
        if date in d:
            d[date].append(rec[2])

    return [[compute_score(d[date]) for date in dates]]

def compute_score(recs):
    score = 0
    if not recs:
        return score
    
    date_type = 1
    if -1 in recs: date_type = -1
    elif 0 in recs: date_type = 0

    if date_type == 1:
        score = len(recs)
    elif date_type == 0:
        score = 5 + recs.count(0)
    else:
        score = 10 + recs.count(-1)

    return score
