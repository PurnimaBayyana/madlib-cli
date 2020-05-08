from madlib_cli.madlib import file_initial_read, split_content,merge

def test_file_initial_read():
    actual = file_initial_read('madlib_cli/assets/inputfile.txt')
    expected = "A {Adjective} and {Noun}"
    assert actual == expected

def test_split_content():
    actual = split_content('A {Adjective} and  {Noun}')
    expected = ['Adjective', 'Noun'],"A {} and  {}"
    assert actual == expected

def test_merge():
    actual = merge(['Rose', 'Beautifull'],'A {} and  {}')
    expected = "A Rose and  Beautifull"
    assert actual == expected