import json, sys, rb
# ins.py name:assetId ...
for pair in sys.argv[1:]:
    name, aid = pair.split(":")
    r = rb.send({"name": "insert_asset", "arguments": {"assetId": aid, "assetName": name, "assetType": "Model", "parentPath": "game.ServerStorage.MTLib", "studio_id": rb.sid}})
    print(name, aid, rb.text(r)[:160].replace("\n", " "))
