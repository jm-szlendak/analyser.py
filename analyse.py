import xml.etree.ElementTree as ET
from analysers import analyse_votes, analyse_posts


HANDLERS = {
    'posts': analyse_posts,
    'votes': analyse_votes
}


def extract_data_type(xmlIterator):
    _, topLevelElement = next(xmlIterator)
    return topLevelElement.tag


def analyse(stream):

    xmlIterator = ET.iterparse(stream, events=['start'])
    
    data_type = extract_data_type(xmlIterator)

    return HANDLERS[data_type](xmlIterator)
