def parse_column_headers(res):
    return [r[0] for r in res.description]