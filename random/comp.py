import json, requests, Queue
from threading import Thread
from itertools import izip
from xml.etree import ElementTree
from copy import copy


class scheduler:
    def __init__(self):
        self.q = Queue.Queue()
        self.flag = True

    def dictify(self, r, root=True):
        if root:
            return {r.tag: self.dictify(r, False)}
        d = copy(r.attrib)
        if r.text:
            d["_text"] = r.text
        for x in r.findall("./*"):
            if x.tag not in d:
                d[x.tag] = []
            d[x.tag].append(self.dictify(x, False))
        return d

    def read_response(self, url):
        data = requests.get(url)
        if data.text.startswith('{'):
            j = json.loads(data.text)
            return j
        else:
            root = ElementTree.fromstring(data.text)
            return self.dictify(root)

    def reader(self, f1, f2):
        file1 = open(f1)
        file2 = open(f2)
        for f, g in izip(self.read_lines(file1), self.read_lines(file2)):
            self.q.put((self.read_response(f), self.read_response(g)))
        self.flag = False

    def read_lines(self, f):
        for line in f:
            yield line.strip()

    def comparator(self):
        while self.flag or not self.q.empty():
            t = self.q.get()
            if t[0] == t[1]:
                print('True')
            else:
                print('False')


def go():
    s = scheduler()
    file1 = 'file1'
    file2 = 'file2'
    Thread(target=s.reader, args=(file1, file2)).start()
    Thread(target=s.comparator).start()


if __name__ == '__main__':
    go()
