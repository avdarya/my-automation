import pytest
from string_utils import StringUtils

@pytest.mark.capitilize_positive
@pytest.mark.parametrize('string, result', [
  ('word', 'Word'),
  ('hello, world!', 'Hello, world!'),
  ('hello, World!', 'Hello, World!'),
  ('12345', '12345')
])
def test_capitilize_positive(string, result):
  utils = StringUtils()
  assert utils.capitilize(string) == result

@pytest.mark.capitilize_negative
@pytest.mark.parametrize('string, result', [
  ('Text', 'Text'),
  (' first', ' first'),
  ('', ''),
  (' ', ' ')
])
def test_capitilize_negative(string, result):
  utils = StringUtils()
  assert utils.capitilize(string) == result

@pytest.mark.capitilize_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string', [
  (1),
  (None),
])
def test_capitilize_negative_type(string):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.capitilize(string)

@pytest.mark.trim_positive
@pytest.mark.parametrize('string, result', [
  (' word', 'word'),
  ('   hello', 'hello'),
  (' hello, world!', 'hello, world!'),
  (' 123', '123')
])
def test_trim_positive(string, result):
  utils = StringUtils()
  assert utils.trim(string) == result

@pytest.mark.trim_negative
@pytest.mark.parametrize('string, result', [
  ('word', 'word'),
  ('hello ', 'hello '),
  ('', ''),
  (' ', ''),
])
def test_trim_negative(string, result):
  utils = StringUtils()
  assert utils.trim(string) == result

@pytest.mark.trim_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string', [
  (1),
  (None),
])
def test_trim_negative_type(string):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.trim(string)

@pytest.mark.to_list_positive
@pytest.mark.parametrize('string, delimeter, result', [
    ('hello,world', ',', ['hello', 'world']),
    ('hello, world', ',', ['hello', ' world']),
    ('alex;mike;eva', ';', ['alex', 'mike', 'eva']),
    ('1.23.457', '.', ['1', '23', '457']),
    ('a,b,', ',', ['a', 'b', '']),
    ('string1text', '1', ['string', 'text']),
    ('abc', ' ', ['abc']),
    ('a b', None, ['a', 'b']),
  ]
)
def test_to_list_positive(string, delimeter, result):
  utils = StringUtils()
  assert utils.to_list(string, delimeter) == result

@pytest.mark.to_list_positive
@pytest.mark.parametrize('string, result', [
    ('a,b', ['a', 'b'])
  ]
)
def test_to_list_positive_without_sep(string, result):
  utils = StringUtils()
  assert utils.to_list(string) == result

@pytest.mark.to_list_negative
@pytest.mark.parametrize('string, delimeter, result', [
    ('hello,world', '.', ['hello,world']),
    ('', ',', []),
    (' ', ',', []),
    ('abc', '', ['abc']),
  ]
)
def test_to_list_negative(string, delimeter, result):
  utils = StringUtils()
  assert utils.to_list(string, delimeter) == result

@pytest.mark.to_list_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string, delimeter', [
    (None, ','),
    (1234, '.'),
    ('a,b,c', 1)
  ]
)
def test_to_list_negative_type(string, delimeter):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.to_list(string, delimeter)

@pytest.mark.contains_positive
@pytest.mark.parametrize('string, symbol, result', [
    ('some text', 'x', True),
    ('Upper', 'U', True),
    ('Upper', 'p', True),
    ('year 2024', '0', True),
    ('text with key words', 'key', True),
    ('with space', ' ', True)
  ]
)
def test_contains_positive(string, symbol, result):
  utils = StringUtils()
  assert utils.contains(string, symbol) == result

@pytest.mark.contains_negative
@pytest.mark.parametrize('string, symbol, result', [
    ('some text', 'X', False),
    ('Upper', 'w', False),
    ('', 'a', False),
    (' ', 'a', False),
    ('some text', '', False),
  ]
)
def test_contains_negative(string, symbol, result):
  utils = StringUtils()
  assert utils.contains(string, symbol) == result

@pytest.mark.contains_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol', [
    (None, 'a'),
    (384, '1'),
    ('alex', None),
    ('1234', 1)
  ]
)
def test_contains_negative_type(string, symbol):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.contains(string, symbol)

@pytest.mark.delete_symbol_positive
@pytest.mark.parametrize('string, symbol, result', [
    ('some text', 'x', 'some tet'),
    ('Upper', 'U', 'pper'),
    ('Upper', 'p', 'Uer'),
    ('year 2024', '0', 'year 224'),
    ('text with key words', 'key', 'text with  words'),
    ('word', 'word', ''),
    ('year 2024', ' ', 'year2024'),
  ]
)
def test_delete_symbol_positive(string, symbol, result):
  utils = StringUtils()
  assert utils.delete_symbol(string, symbol) == result

@pytest.mark.delete_symbol_negative
@pytest.mark.parametrize('string, symbol, result', [
    ('word', 'words', 'word'),
    ('', 'a', ''),
    (' ', 'a', ' '),
    ('string', '', 'string'),
    ('string', ' ', 'string'),
  ]
)
def test_delete_symbol_negative(string, symbol, result):
  utils = StringUtils()
  assert utils.delete_symbol(string, symbol) == result

@pytest.mark.delete_symbol_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol', [
    (8485, '4'),
    (None, 'a'),
    ('delete1', 1),
    ('delete1', None)
  ]
)
def test_delete_symbol_negative_type(string, symbol):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.delete_symbol(string, symbol)

@pytest.mark.starts_with_positive
@pytest.mark.parametrize('string, symbol, result', [
    ('one symbol', 'o', True),
    ('One symbol', 'O', True),
    ('1 char', '1', True),
    ('first word', 'first', True),
    (' starts', ' ', True),
  ]
)
def test_starts_with_positive(string, symbol, result):
  utils = StringUtils()
  assert utils.starts_with(string, symbol) == result

@pytest.mark.starts_with_negative  
@pytest.mark.parametrize('string, symbol, result', [
    ('one symbol', 'p', False),
    ('one symbol', 'O', False),
    ('', 'a', False),
    (' ', 'a', False),
    ('string empty', '', False),
    ('string', ' ', False),
  ]
)
def test_starts_with_symbol_negative(string, symbol, result):
  utils = StringUtils()
  assert utils.starts_with(string, symbol) == result

@pytest.mark.starts_with_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol', [
    (8485, '8'),
    (None, 'a'),
    ('text', 1),
    ('text none', None)
  ]
)
def test_starts_with_symbol_negative_type(string, symbol):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.starts_with(string, symbol)

@pytest.mark.end_with_positive
@pytest.mark.parametrize('string, symbol, result', [
    ('one symbol', 'l', True),
    ('One symboL', 'L', True),
    ('char 1', '1', True),
    ('first word', 'word', True),
    ('end ', ' ', True)
  ]
)
def test_end_with_positive(string, symbol, result):
  utils = StringUtils()
  assert utils.end_with(string, symbol) == result

@pytest.mark.end_with_negative
@pytest.mark.parametrize('string, symbol, result', [
    ('one symbol', 'p', False),
    ('one symbol', 'L', False),
    ('', 'a', False),
    (' ', 'a', False),
    ('end empty', '', False),
    ('end space', ' ', False),
  ]
)
def test_end_with_symbol_negative(string, symbol, result):
  utils = StringUtils()
  assert utils.end_with(string, symbol) == result

@pytest.mark.end_with_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol', [
    (8485, '8'),
    (None, 'a'),
    ('end', 1),
    ('end', None)
  ]
)
def test_end_with_symbol_negative_type(string, symbol):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.end_with(string, symbol)

@pytest.mark.is_empty_positive
@pytest.mark.parametrize('string, result', [
    ('empty', False),
    (' text ', False),
    ('12345', False),
    ('some words', False),
    ('', True),
    (' ', True)
  ]
)
def test_is_empty_positive(string, result):
  utils = StringUtils()
  assert utils.is_empty(string) == result

@pytest.mark.is_empty_negative
@pytest.mark.xfail
@pytest.mark.parametrize('string', [
    (1234),
    (None),
  ]
)
def test_is_empty_negative_type(string):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.is_empty(string)

@pytest.mark.list_to_string_positive
@pytest.mark.parametrize('list, joiner, result', [
    (['ac', 'cd'], ',', 'ac,cd'),
    (['ac'], ',', 'ac'),
    (['t', 'r', 'u', 'e'], '.', 't.r.u.e'),
    (['1', '2', '3', '4'], '-', '1-2-3-4'),
    ([1, 2], '.', '1.2'),
    (['t', 'r', 'u', 'e'], '', 'true'),
  ]
)
def test_list_to_string_positive(list, joiner, result):
  utils = StringUtils()
  assert utils.list_to_string(list, joiner) == result

@pytest.mark.list_to_string_positive
@pytest.mark.parametrize('list, result', [
    (['ac', 'cd'], 'ac, cd'),
  ]
)
def test_list_to_string_positive_without_joiner(list, result):
  utils = StringUtils()
  assert utils.list_to_string(list) == result

@pytest.mark.list_to_string_negative
@pytest.mark.parametrize('list, joiner, result', [
    ([], ',', ''),
  ]
)
def test_list_to_string_negative(list, joiner, result):
  utils = StringUtils()
  assert utils.list_to_string(list, joiner) == result

@pytest.mark.list_to_string_negative
@pytest.mark.xfail
@pytest.mark.parametrize('list, joiner', [ 
    (['t', 'r', 'u', 'e'], 1),
  ]
)
def test_list_to_string_negative_type(list, joiner):
  utils = StringUtils()
  with pytest.raises(TypeError):
    utils.list_to_string(list, joiner)