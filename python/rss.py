import io, os, sys, types, shutil, json
from datetime import datetime

import feedparser, operator
from goose import Goose

import spacy
import spacy.en
from spacy.parts_of_speech import NOUN


# location on server for goose to write temp files
goose_dir = '/tmp/rss/'

# location on server for data files to be written
data_dir = './data/'

## take the url of a webpage that should be an article
## return the article and its metadata
def extractArticle(url):
    from goose.configuration import Configuration
    config = Configuration()
    config.local_storage_path = goose_dir
    return Goose(config).extract(url=url)

## bump up count of word in wordict
def addCount(wordict,word):
    if word not in wordict:
        wordict[word] = 1
    else:
        wordict[word] += 1


def build(rss):
    # prepare goose_dir
    if os.path.exists(goose_dir):
        shutil.rmtree(goose_dir)
    os.mkdir(goose_dir)
    # string to keep track of the files that are written
    filesWritten = ""
    # analyze the feed
    feed = feedparser.parse(rss)
    if (feed['feed'] == {}): #could not parse properly
        print "Error: input does not year a viable rss feed"
        sys.exit(0);
    # prepare spacy and entity metadata
    nlp = spacy.en.English()
    is_noun = lambda dok: tok.pos == NOUN
    entities = ['People','Nationalities, Organizations, Religions, and Political Parties','Facilities','Organizations','Geo-Political Entities','Locations','Products','Events','Works of Art','Laws','Languages','Dates','Times','Percents','Money','Quantities','Ordinal Numbers','Cardinal Numbers']
    entity_nums = [28061,1499631,164860,202115,85248,87482,86554,81537,1499633,39247,83611,55719,8206,112430,17764,341856,1499632,354826]
    # loop through items in feed
    # write a file for each analysis
    for item in feed["items"]:
        # initalize the dictionaries
        #   1 for words, 1 for entities
        wordcount = {}
        value_dicts = dict((x,{}) for x in entity_nums)
        # extract article from url and process with spacy
        body = extractArticle(item["link"]).cleaned_text
        tokens = nlp(body)
        ents = list(tokens.ents)
        # add ents to dictionaries
        for ent in ents:
            decoded = ent.orth_
            if type(ent.orth_) is not types.UnicodeType:
                decoded = ent.orth_.decode("utf-8")
            replaced = decoded.replace(u".", "").replace(u"\"", "'").replace(u"\n", "")
            cleaned = replaced.encode("utf-8")
            addCount(value_dicts[ent.label],replaced)
        # add words to dictionary
        for tok in tokens:
            if is_noun(tok):
                addCount(wordcount, tok.orth_)
        ## Save the data
        title = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
        filesWritten = filesWritten + title + ','
        with open(data_dir + title + '.json', 'w') as f:
            # format data for printing to comply with html file
            articleTitle = item["title"].decode("utf-8").replace(u"\"", "'").encode("utf-8")
            articleLink = item["link"]
            articleInfo = {'title': articleTitle, 'link': articleLink}
            data = [{'name': 'Articles', 'children': [articleInfo]}]
            nounInfo = [{'name': k, 'size': v} for k,v in wordcount.iteritems()]
            data.append({'name': 'Nouns', 'children': nounInfo})
            data += [{'name': entities[entity_nums.index(d)], 'children' : [{'name': k, 'size': v} for k,v in c.iteritems()]} for d,c in value_dicts.iteritems()]
            f.write(json.dumps(data))
    print filesWritten[:-1] ## Ignores the trailing comma



def main(argv):
    if len(argv) != 2:
        print "Error: impropert input length"
        return
    else:
        build(sys.argv[1])

if __name__ == "__main__":
    main(sys.argv)
