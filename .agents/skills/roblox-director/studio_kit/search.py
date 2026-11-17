import json, sys, rb
qs = sys.argv[1:]
out = {}
for q in qs:
    args = {"query": q, "assetType": "Model", "scope": "creator_store", "priceFilter": "free", "maxResults": 12, "studio_id": rb.sid}
    r = rb.send({"name": "search_asset", "arguments": args})
    try: res = json.loads(rb.text(r))["results"]
    except Exception as e: print(q, "ERR", rb.text(r)[:200]); continue
    out[q] = res
    print("##", q)
    for a in res:
        d = (a.get("description") or "").replace("\n", " ")
        print(f'  {a["assetId"]} | {a["name"][:60]} | {a.get("creatorName","")[:22]} | {d[:150]}')
json.dump(out, open("search_" + str(abs(hash(" ".join(qs))) % 10000) + ".json", "w"), indent=1)
