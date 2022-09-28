def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    if ';' not in query and len(query) <= 1:
        return {}

    res = {}

    query_split = query.split(';')
    for task in query_split:
        if len(task) == 0 or '=' not in task:
            continue
        task_split = task.split('=', 1)
        task_name = task_split[0]
        task_value = task_split[1]
        res[task_name] = task_value
    return res


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie(';') == {}
    assert parse_cookie('name=Dima=User;age=28;job=developer;nationality=ukr') == {'name': 'Dima=User', 'age': '28',
                                                                                   'job': 'developer',
                                                                                   'nationality': 'ukr'}
    assert parse_cookie('name=====Dima=User=====;age=28;') == {'name': '====Dima=User=====', 'age': '28'}
    assert parse_cookie('name=====Dima=User=====;;;;;;;;age=28;') == {'name': '====Dima=User=====', 'age': '28'}
    assert parse_cookie('name=====Dima=User=====;;;;;;;;age=28;job-developer') == {'name': '====Dima=User=====',
                                                                                   'age': '28'}
    assert parse_cookie('name;Dima;') == {}
