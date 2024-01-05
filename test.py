from backend import _db_helper, _Admin_helper

amdin = _Admin_helper()

data = amdin.SaveData(data="4d0dacb16570b8c82b6bd5bd01342dd2b7b63c7bf95b9e9bbe2d41eca8bf59d61820b161d596693443d7e2ea84f1a3a6abddeb9b6eb0c1730b8910db53b2a04f")

print(data)