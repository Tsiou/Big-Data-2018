from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class wordFrequency(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word, 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (sum(counts*len(word)), sum(counts))


if __name__ == '__main__':
     wordFrequency.run()