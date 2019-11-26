# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4


def assert_cell(cell):
    """ Ensure it fits into the ipython notebook cell structure:
        {
            'cell_type': 'whatever',
            'source': ['whatever']
        }

    Otherwise raises AssertionError.

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    bool
        True if fits into the ipython notebook cell structure.
    """
    _is_cell =\
        isinstance(cell, dict)\
        and 'cell_type' in cell and isinstance(cell['cell_type'], str)\
        and 'source' in cell and isinstance(cell['source'], list)

    if not _is_cell:
        raise AssertionError('Wrong cell format.'
                             'Please check that it is a dict representing'
                             'a ipython notebook cell with, at least, '
                             "following structure:"
                             "{"
                             "    'cell_type': 'whatever'"
                             "    'source': ['whatever']"
                             "}")

    return _is_cell


def is_assert(cell):
    """ Ensure given cell contains the assert token.

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    bool
        True it is an assert cell. False otherwise.
    """
    try:
        return assert_cell(cell) and '# asserts' in cell['source'][0].lower()
    except IndexError:
        return False


def is_list(cell):
    """ Check if given cell correspond to a enumeration cell.

    The cell will be considered a list if it is a markdown cell
    and starts with the list markdown token: *

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    bool
        True if it is a list cell. False otherwise.
    """
    try:
        return assert_cell(cell) and cell['source'][0].strip()[0] == '*'
    except IndexError:
        return False


def is_title(cell):
    """ Check if given cell is a title cell.

    A cell will be considered a title if it is a markdown cell
    and starts with the title/subtitle markdown token: #

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    bool
        True if it is a title cell. False otherwise.
    """
    try:
        return assert_cell(cell) and cell['source'][0].strip()[0] == '#'
    except IndexError:
        return False


def is_markdown(cell):
    """ Ensure cell type is markdown.

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    bool
        True if it is a markdown cell. False otherwise.
    """
    return assert_cell(cell) and cell['cell_type'] == 'markdown'


def is_code(cell):
    """ Ensure cell type is code.

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    bool
        True if it is a code cell. False otherwise.
    """
    return assert_cell(cell) and cell['cell_type'] == 'code'


def get_first_line(cell):
    """ Get the first line from the source field.

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    str
        First line from source field.
    """
    if not assert_cell(cell) or 'source' not in cell:
        raise AssertionError('Wrong cell format: %s' % cell)
    try:
        return cell['source'][0].strip()
    except IndexError as e:
        raise IndexError('Cell source is empty. %s' % e)


def get_code(cell):
    """ Get all the code from the source field.

    Parameters
    ----------
    cell: dict
        iPython notebook cell representation.

    Returns
    -------
    str
        All the code from the source field.
    """
    if is_code(cell):
        return ''.join(cell['source'])
