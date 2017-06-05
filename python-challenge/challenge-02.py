# http://www.pythonchallenge.com/pc/def/map.html
import string
encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
      "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
      "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print ''.join([chr(97 + (ord(c)+2) % 26) for c in encrypted if c.isalpha()])
print ord('g')